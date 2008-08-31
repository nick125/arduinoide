/*
  SoftwareSerial example

  Sample of the SoftwareSerial library.  Listens for serial in on pin 2
  and sends it out again on pin 3.

  by Tom Igoe
  based on examples by David Mellis and Heather Dewey-Hagborg
  written: 6 Jan 2007


*/

// include the SoftwareSerial library so you can use its functions:
#include <SoftwareSerial.h>

#define rxPin 2
#define txPin 3
#define ledPin 13

// set up a new serial port
SoftwareSerial mySerial =  SoftwareSerial(rxPin, txPin);
byte pinState = 0;

void setup()  {
  // define pin modes for tx, rx, led pins:
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
}

void loop() {
  // listen for new serial coming in:
  char someChar = mySerial.read();
  // print out the character:
  mySerial.print(someChar);
  // toggle an LED just so you see the thing's alive.  
  // this LED will go on with every OTHER character received:
  toggle(13);

}


void toggle(int pinNum) {
  // set the LED pin using the pinState variable:
  digitalWrite(pinNum, pinState); 
  // if pinState = 0, set it to 1, and vice versa:
  pinState = !pinState;
}
