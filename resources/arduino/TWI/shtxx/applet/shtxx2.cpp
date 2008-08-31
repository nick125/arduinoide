#include "WProgram.h"
/*
 * Serial TTY
 * -----------------
 * This is a simple example of how to use serial communication to
 * poll analog input values
 *
 * Created 26 December 2007
 * copyleft 2007 Wayne Prasek <wprasek@gmail.comm>
 * http://ragingreality.thotbot.com/
 * 
 */

int dataPin = 10;
int sckPin = 11;

void resetSHT()
{
  pinMode(dataPin,OUTPUT);
  pinMode(sckPin,OUTPUT);
  
  shiftOut(dataPin, sckPin, LSBFIRST, 255);
  shiftOut(dataPin, sckPin, LSBFIRST, 255);
  
  digitalWrite(dataPin,HIGH);
  for(int i = 0; i < 15; i++){
     digitalWrite(sckPin, LOW);
     digitalWrite(sckPin, HIGH);
  }
}

//Specific SHT start command
void startSHT()
{
  pinMode(sckPin,OUTPUT);
  pinMode(dataPin,OUTPUT);
  digitalWrite(dataPin,HIGH);
  digitalWrite(sckPin,HIGH);
  digitalWrite(dataPin,LOW);
  digitalWrite(sckPin,LOW);
  digitalWrite(sckPin,HIGH);
  digitalWrite(dataPin,HIGH);
  digitalWrite(sckPin,LOW);
}

void writeByteSHT(byte data)
{ 
  pinMode(sckPin,OUTPUT);
  pinMode(dataPin,OUTPUT);  
  
//  digitalWrite(dataPin,LOW);
  shiftOut(dataPin,sckPin,MSBFIRST,data);
  
  pinMode(dataPin,INPUT);

  //Wait for SHT15 to acknowledge by pulling line low
  while(digitalRead(dataPin) == 1);
  
  digitalWrite(sckPin,HIGH);
  digitalWrite(sckPin,LOW);  //Falling edge of 9th clock
  
  //wait for SHT to release line
  while(digitalRead(dataPin) == 0 );
 
  //wait for SHT to pull data line low to signal measurement completion
  //This can take up to 210ms for 14 bit measurments
  int i = 0;
  while(digitalRead(dataPin) == 1 )
  {
    i++;
    if (i == 255) break;
    
    delay(10);
  } 
  
  //debug
  i *= 10;
  Serial.print("Response time = ");
  Serial.println(i);
}

//Read 16 bits from the SHT sensor
int readByte16SHT()
{
  int cwt = 0;
  unsigned int bitmask = 32768;
  int temp;
  
  pinMode(dataPin,INPUT);
  pinMode(sckPin,OUTPUT);
  
  digitalWrite(sckPin,LOW);
  
  for(int i = 0; i < 17; i++) {
    if(i != 8) {
      digitalWrite(sckPin,HIGH);
      temp = digitalRead(dataPin);
//      Serial.print(temp,BIN);
      cwt = cwt + bitmask * temp;
      digitalWrite(sckPin,LOW);
      bitmask=bitmask/2;
    }
    else {
      pinMode(dataPin,OUTPUT);
      digitalWrite(dataPin,LOW);
      digitalWrite(sckPin,HIGH);
      digitalWrite(sckPin,LOW);
      pinMode(dataPin,INPUT); 
    }
  }
  
  //leave clock high??
  digitalWrite(sckPin,HIGH);
  
//  Serial.println();
  
  return cwt;
}

int getTempSHT()
{
  startSHT();
  writeByteSHT(B0000011);
  return readByte16SHT();
}

int getHumidSHT()
{
  startSHT();
  writeByteSHT(B00000101);
  return readByte16SHT();
}


void setup() {
  pinMode(dataPin,OUTPUT);
  pinMode(sckPin,OUTPUT);

  Serial.begin(9600);        // connect to the serial port
  
  Serial.println("Resetting SHT...");
  resetSHT();
}

void loop () {
  delay(2000);
  Serial.println("Starting Temperature/Humidity reading...");
  int temp = getTempSHT();
  Serial.print("Temprature:");
  Serial.println(temp);

  temp = getHumidSHT();
  Serial.print("Humidity:");
  Serial.println(temp);  
}
int main(void)
{
	init();

	setup();
    
	for (;;)
		loop();
        
	return 0;
}

