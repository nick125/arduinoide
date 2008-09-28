/*
  PS2Keyboard.cpp - PS2Keyboard library
  Copyright (c) 2007 Free Software Foundation.  All right reserved.
  Written by Christian Weichel <info@32leaves.net>

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2.1 of the License, or (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*/

#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/pgmspace.h>
#include "WProgram.h"
#include "PS2Keyboard.h"



/*
 * The lookup table used by the read() method. Change this in order to
 * support more or different keys. But be aware that the more keys are in
 * this table, the longer the lookup will take and the more space will be
 * consumed.
 * The default implementation understands the numblock numbers only. See
 * http://www.computer-engineering.org/ps2keyboard/scancodes2.html for a list
 * of possible scancodes.
 */
#define PS2_KC_LUT_CAPACITY 10
PROGMEM prog_uchar PS2_KC_LUT_DATA[PS2_KC_LUT_CAPACITY] = {0x70, 0x69, 0x72, 0x7a, 0x6b, 0x73, 0x74, 0x6c, 0x75, 0x7d};
PROGMEM prog_uchar PS2_KC_LUT_CHAR[PS2_KC_LUT_CAPACITY] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};


/*
 * I do know this is so uncool, but I just don't see a way arround it
 * REALLY BAD STUFF AHEAD
 *
 * The variables are used for internal status management of the ISR. The're
 * not kept in the object instance because the ISR has to be as fast as anyhow
 * possible. So the overhead of a CPP method call is to be avoided.
 *
 * PLEASE DO NOT REFER TO THESE VARIABLES IN YOUR CODE AS THEY MIGHT VANISH SOME
 * HAPPY DAY.
 */
int ps2Keyboard_DataPin;
byte ps2Keyboard_CurrentBuffer;
volatile byte ps2Keyboard_CharBuffer;
byte ps2Keyboard_BufferPos;
bool ps2Keyboard_BreakActive;



// The ISR for the external interrupt
ISR(INT1_vect) {
  int value = digitalRead(ps2Keyboard_DataPin);
  
  if(ps2Keyboard_BufferPos > 0 && ps2Keyboard_BufferPos < 9) {
    ps2Keyboard_CurrentBuffer |= (value << (ps2Keyboard_BufferPos - 1));
  }
  
  ps2Keyboard_BufferPos++;
  
  if(ps2Keyboard_BufferPos == 11) {
    if(ps2Keyboard_CurrentBuffer == PS2_KC_BREAK) {
      ps2Keyboard_BreakActive = true;
    } else if(ps2Keyboard_BreakActive) {
      ps2Keyboard_BreakActive = false;
    } else {
      ps2Keyboard_CharBuffer = ps2Keyboard_CurrentBuffer;
      
    }
    ps2Keyboard_CurrentBuffer = 0;
    ps2Keyboard_BufferPos = 0;
  }
}

PS2Keyboard::PS2Keyboard() {
  // nothing to do here	
}

void PS2Keyboard::begin(int dataPin) {
  // Prepare the global variables
  ps2Keyboard_DataPin = dataPin;
  ps2Keyboard_CurrentBuffer = 0;
  ps2Keyboard_CharBuffer = 0;
  ps2Keyboard_BufferPos = 0;
  ps2Keyboard_BreakActive = false;

  // initialize the pins
  pinMode(PS2_INT_PIN, INPUT);
  digitalWrite(PS2_INT_PIN, HIGH);
  pinMode(dataPin, INPUT);
  digitalWrite(dataPin, HIGH);
  
  // Global Enable INT1 interrupt
  EIMSK |= ( 1 << INT1);
  // Falling edge triggers interrupt
  EICRA |= (0 << ISC10) | (1 << ISC11);
}

bool PS2Keyboard::available() {
  return ps2Keyboard_CharBuffer != 0;
}

byte PS2Keyboard::read() {
  byte result = ps2Keyboard_CharBuffer;
  
  for(int i = 0; i < PS2_KC_LUT_CAPACITY; i++) {
    if(ps2Keyboard_CharBuffer == pgm_read_byte_near(PS2_KC_LUT_DATA + i)) {
      result = pgm_read_byte_near(PS2_KC_LUT_CHAR + i);
    }
  }
  ps2Keyboard_CharBuffer = 0;
  
  return result;
}
