#include "WProgram.h"
#include <Servo.h>

Servo servo1;
Servo servo2;
int blinkenlite = 13;

void setup()
{
  servo1.attach(2);
  servo1.setMaximumPulse(2200);
//servo2.attach(15);
  Serial.begin(19200);
  Serial.print("Ready");
  pinMode(blinkenlite, OUTPUT);
}

void loop()
{
  static int v = 0;

  if ( Serial.available()) {
    digitalWrite(blinkenlite, HIGH);
    char ch = Serial.read();
    delay(40);
    digitalWrite(blinkenlite, LOW);
    switch(ch) {
      case '0'...'9':
        v = v * 10 + ch - '0';
        break;
      case 's':
        servo1.write(v);
        v = 0;
        break;
//      case 'w':
//        servo2.write(v);
//        v = 0;
//        break;
      case 'd':
        servo1.detach();
        break;
      case 'a':
        servo1.attach(15);
        break;
    }
  }

  Servo::refresh();
}
int main(void)
{
	init();

	setup();
    
	for (;;)
		loop();
        
	return 0;
}

