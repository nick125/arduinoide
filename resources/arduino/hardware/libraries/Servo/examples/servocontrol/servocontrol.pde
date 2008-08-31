#include <Servo.h>

Servo servo1;
Servo servo2;

void setup()
{
  servo1.attach(14);
  servo1.setMaximumPulse(2200);
  servo2.attach(15);
  Serial.begin(19200);
  Serial.print("Ready");
}

void loop()
{
  static int v = 0;

  if ( Serial.available()) {
    char ch = Serial.read();

    switch(ch) {
      case '0'...'9':
        v = v * 10 + ch - '0';
        break;
      case 's':
        servo1.write(v);
        v = 0;
        break;
      case 'w':
        servo2.write(v);
        v = 0;
        break;
      case 'd':
        servo2.detach();
        break;
      case 'a':
        servo2.attach(15);
        break;
    }
  }

  Servo::refresh();
}

