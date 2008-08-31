/*The following code lets you send strings like "90s" and "80w" 
 *to position servos on pin a0 and a1 to 90 degrees and 80 degrees. 
 *You can also use "d" to detach the servo on pin 15 and "a" to reattach it. 
 */

#include <Servo.h>

Servo servo1;
Servo servo2;

void setup()
{
  servo1.attach(14);
  servo1.setMaximumPulse(2200);
  servo2.attach(15);
  Serial.begin(9600);
  Serial.println("Ready:");
}

void loop()
{
  static int v = 0;

  if ( Serial.available()) {
    Serial.println("Ready:");
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

