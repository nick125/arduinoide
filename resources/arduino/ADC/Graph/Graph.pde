/*
 * Graph
 * Ian Daniher, 08.24.08
 * All Rights Reserved.
 * Outputs a csv string to serial, raw values of analog pin 0
 */

int value = 0;

void setup()
{
  Serial.begin(9600); //starts serial
  pinMode(12, OUTPUT); //sets pin 12 as output
  digitalWrite(12, HIGH); //sets pin 12 high
}

void loop()
{
  value +=1;
  delay(1000);
  Serial.print(value);
  Serial.print(",");
  Serial.println(analogRead(0));
}

