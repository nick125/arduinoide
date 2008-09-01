// From NearFuture Labs
// Control the DS1803 Digital Potentiometer

#include <Wire.h>

void setup()
{
  Wire.begin(); // join i2c bus (address optional for master)
}

byte val = 0;

void loop()
{
  Wire.beginTransmission(0x28); // transmit to device 0x28)
  Wire.send(0xAA);            // sends instruction byte,
                               // write to potentiometer-0
  Wire.send(val);             // sends potentiometer value byte
  Wire.endTransmission();     // stop transmitting

  val++;        // increment value
  if(val == 150) // if reached 64th position (max)
  {
    val = 0;    // start over from lowest value
  }
  delay(100);
}
