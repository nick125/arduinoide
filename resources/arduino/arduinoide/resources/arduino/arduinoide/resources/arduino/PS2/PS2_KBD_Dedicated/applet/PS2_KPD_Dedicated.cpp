#include "WProgram.h"
#include <PS2Keyboard.h>

#define DATA_PIN 4
PS2Keyboard keyboard;

void setup() {
  keyboard.begin(DATA_PIN);

  Serial.begin(9600);
  Serial.println("hi");
  delay(1000);
}

void loop() {
  if(keyboard.available()) {
    byte dat = keyboard.read();
    byte val = dat - '0';

    if(val >= 0 && val <= 9) {
      Serial.print(val, DEC);
    } else if(dat == PS2_KC_ENTER) {
      Serial.println();
    } else if(dat == PS2_KC_ESC) {
      Serial.println("[ESC]");
    } 
  }
}
int main(void)
{
	init();

	setup();
    
	for (;;)
		loop();
        
	return 0;
}

