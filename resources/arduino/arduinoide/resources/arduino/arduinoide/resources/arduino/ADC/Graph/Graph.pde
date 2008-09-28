/*
 * Graph
 * Ian Daniher, 08.24.08
 * All Rights Reserved.
 * Outputs a csv string to serial, raw values of analog pins 0-3
 * $(PIN)p,$(VALUESEQUENCE),$(RAWVALUE)
 */

int value = 0;

void setup()
{
  Serial.begin(9600); //starts serial
  pinMode(12, OUTPUT); //sets pin 12 as output
  digitalWrite(12, HIGH); //sets pin 12 high
  //reverse-bias LED for light sensor
}

void loop()
{
  value +=1;
  delay(1000);
  Serial.print("0p");
  Serial.print(",");
  Serial.print(value);
  Serial.print(",");
  Serial.println(analogRead(0));
  Serial.print("1p");
  Serial.print(",");
  Serial.print(value);
  Serial.print(",");
  Serial.println(analogRead(1));
  Serial.print("2p");
  Serial.print(",");
  Serial.print(value);
  Serial.print(",");
  Serial.println(analogRead(2));
  Serial.print("3p");
  Serial.print(",");
  Serial.print(value);
  Serial.print(",");
  Serial.println(analogRead(3));
          
                
}

