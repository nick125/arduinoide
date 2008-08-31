/*
 * wii_nunchuck_sevo -- Use a Wii Nunchuck to control a servo
 *
 * Tod E. Kurt, http://todbot.com/blog/
 *
 * The Wii Nunchuck reading code is taken from Windmeadow Labs
 *   http://www.windmeadow.com/node/42
 */
 
#include <Wire.h>
#include <string.h>
#include <stdio.h>

uint8_t outbuf[6];		// array to store arduino output
int cnt = 0;
int ledPin = 13;

int servoPin = 7;      // Control pin for servo motor
int pulseWidth = 0;    // Amount to pulse the servo
long lastPulse = 0;    // the time in millisecs of the last pulse
int refreshTime = 20;  // the time in millisecs needed in between pulses
int minPulse = 700;   // minimum pulse width

#define pwbuffsize 4   
int pwbuff[pwbuffsize]; // buffer for smoothing pulseWidths
int pwbuffpos = 0;      // position in pwbuff

void setup()
{
  beginSerial (19200);
  Wire.begin ();		// join i2c bus with address 0x52
  nunchuck_init (); // send the initilization handshake
  pinMode(servoPin, OUTPUT);  // Set servo pin as an output pin
  pulseWidth = minPulse;      // Set the motor position to the minimum
  Serial.print ("Finished setup\n");
}

void nunchuck_init()
{
  Wire.beginTransmission (0x52);	// transmit to device 0x52
  Wire.send (0x40);		// sends memory address
  Wire.send (0x00);		// sends sent a zero.  
  Wire.endTransmission ();	// stop transmitting
}

void send_zero()
{
  Wire.beginTransmission (0x52);	// transmit to device 0x52
  Wire.send (0x00);		// sends one byte
  Wire.endTransmission ();	// stop transmitting
}

int t = 0;  // when it gets to 25, read nunchuck
void loop()
{
  t++;
  if( t == 25 ) {
    t = 0;
    Wire.requestFrom (0x52, 6);	// request data from nunchuck
    while (Wire.available ()) {
      // receive byte as an integer
      outbuf[cnt] = nunchuk_decode_byte (Wire.receive ());
      digitalWrite (ledPin, HIGH);	// sets the LED on
      cnt++;
    }
    // If we recieved the 6 bytes, then go print them
    if (cnt >= 5) {
      //printNunchuckData();            // uncomment this for debug
      // update servo pulseWidth
      float tilt = outbuf[4];            // z-axis, in this case ranges from ~75 - ~185
      tilt = (tilt - 70) * 1.5;          // convert to degrees angle, approximately
      pulseWidth = (tilt * 9) + minPulse; // convert angle to microseconds
      pwbuff[pwbuffpos] = pulseWidth;    // save for averaging
      if( ++pwbuffpos == pwbuffsize ) pwbuffpos = 0;

      pulseWidth=0;                      // reset so we can  
      for( int p=0; p<pwbuffsize; p++ )  // do the smoothing
        pulseWidth += pwbuff[p];         // sum up them all
      pulseWidth /= pwbuffsize;          // divide to get average
      
      // uncomment this for debug
      //Serial.print("tilt: ");   Serial.print((int)tilt);
      //Serial.print(" pulseWidth: ");  Serial.println(pulseWidth);
    }
    cnt = 0;
    send_zero(); // send the request for next bytes
    
  } // if(t==)

  updateServo();   // update servo position

  delay(1);
}

// called every loop().
// uses global variables servoPin, pulsewidth, lastPulse, & refreshTime
void updateServo() {
  // pulse the servo again if rhe refresh time (20 ms) have passed:
  if (millis() - lastPulse >= refreshTime) {
    digitalWrite(servoPin, HIGH);   // Turn the motor on
    delayMicroseconds(pulseWidth);  // Length of the pulse sets the motor position
    digitalWrite(servoPin, LOW);    // Turn the motor off
    lastPulse = millis();           // save the time of the last pulse
  }
}

// Print the input data we have recieved
// accel data is 10 bits long
// so we read 8 bits, then we have to add
// on the last 2 bits.  That is why I
// multiply them by 2 * 2
int i=0;
void printNunchuckData()
{
  int joy_x_axis = outbuf[0];
  int joy_y_axis = outbuf[1];
  int accel_x_axis = outbuf[2]; // * 2 * 2; 
  int accel_y_axis = outbuf[3]; // * 2 * 2;
  int accel_z_axis = outbuf[4]; // * 2 * 2;

  int z_button = 0;
  int c_button = 0;

  // byte outbuf[5] contains bits for z and c buttons
  // it also contains the least significant bits for the accelerometer data
  // so we have to check each bit of byte outbuf[5]
  if ((outbuf[5] >> 0) & 1) 
    z_button = 1;
  if ((outbuf[5] >> 1) & 1)
    c_button = 1;

  if ((outbuf[5] >> 2) & 1) 
    accel_x_axis += 2;
  if ((outbuf[5] >> 3) & 1)
    accel_x_axis += 1;

  if ((outbuf[5] >> 4) & 1)
    accel_y_axis += 2;
  if ((outbuf[5] >> 5) & 1)
    accel_y_axis += 1;

  if ((outbuf[5] >> 6) & 1)
    accel_z_axis += 2;
  if ((outbuf[5] >> 7) & 1)
    accel_z_axis += 1;

  Serial.print (i,DEC);
  Serial.print ("\t");

  Serial.print (joy_x_axis, DEC);
  Serial.print ("\t");
  Serial.print (joy_y_axis, DEC);
  Serial.print ("\t");

  Serial.print (accel_x_axis, DEC);
  Serial.print ("\t");
  Serial.print (accel_y_axis, DEC);
  Serial.print ("\t");
  Serial.print (accel_z_axis, DEC);
  Serial.print ("\t");

  Serial.print (z_button, DEC);
  Serial.print (" ");
  Serial.print (c_button, DEC);

  Serial.print ("\r\n");
  i++;
}

// Encode data to format that most wiimote drivers except
// only needed if you use one of the regular wiimote drivers
char nunchuk_decode_byte (char x)
{
  x = (x ^ 0x17) + 0x17;
  return x;
}
