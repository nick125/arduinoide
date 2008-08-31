#include <PS2Keyboard.h>
#include <PS2KeyboardExt.cpp>

#define DATA_PIN 4
#define capslkLed 13                             // the capslock LED pin

PS2Keyboard keyboard;

void setup() {
  keyboard.begin(DATA_PIN);

  pinMode(capslkLed, OUTPUT);

  Serial.begin(9600);
  Serial.println("Hi :)\n");
  delay(1000);
}

void loop() {
  if(keyboard.available()) {
    byte dat = keyboard.read();                   // read one byte from the keyboard
    byte datType = getKeyType(dat);               // get the type of button that was pressed
                                                  // (function, number, letter or punctuation)
                                                  // will return 1, 2, 3, or 4

    if (datType == 1)                             // type came back as a function
    {
      byte funct = getKeyFunct(dat);              //   so get function number
      if (funct == 1) {                           //   function number came back as 1 for 'return'
        Serial.println();                         //     so print a new line
      } else if (funct == 2) {                    //   function number came back as 2 for 'space'
        Serial.print(' ');                        //     so print a space
      } else if (funct == 3) {                    //   function number came back as 3 for 'tab'
        for (int i = 0; i < 6; i++) {             //     so print 5 consecutive spaces
          Serial.print(' ');
        }
      } else if (funct == 4) {                    //   function number came back as 4 for 'backspace'
        Serial.print(8, BYTE);                    //     so go back one character
        Serial.print(" ");                        //     print a space over that character
        Serial.print(8, BYTE);                    //     and go back one character again
      } else if (funct == 5) {                    //   function number came back as 5 for 'capslock'
        if (capslk == 0)                          //      so invert the value of capslk and its LED
        {
          capslk = 1;
          digitalWrite(capslkLed, HIGH);
        } else {
          capslk = 0;
          digitalWrite(capslkLed, LOW);
        }
      } else if (funct == 6) {                    //   function number came back as 6 for 'escape'
        Serial.print("\[ESC]");                   //     so print '[ESC]'
      }
    } else {                                      // type came back as not a function
      char datChar = getKeyChar(dat, datType);    //   so get character the user was trying to type
      Serial.print(datChar);                      //   and print it
    }
  }
}
