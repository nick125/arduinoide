#include "WProgram.h"
long logTime;                      // For counting with millis()
int adcCount;
int shtClk=11;                        // Common clock for both SHT11's
int shtData=10;                       // Selectable data pin
int ioByte;
int ackBit;
unsigned int retVal;               // Return value from SHT11
int dly;
long msTimer;
int k;
int cmdByte;
int dataByte;
uint8_t bitmask;

void SHT_Write_Byte(void) {
  pinMode(shtData, OUTPUT);
  shiftOut(shtData, shtClk, MSBFIRST, ioByte);
  pinMode(shtData, INPUT);
  digitalWrite(shtData, LOW);
  digitalWrite(shtClk, LOW);
  digitalWrite(shtClk, HIGH);
  ackBit = digitalRead(shtData);
  digitalWrite(shtClk, LOW);
}

int shiftIn() {
  int cwt;
  cwt=0;
  bitmask=128;
  while (bitmask >= 1) {
    digitalWrite(shtClk, HIGH);
    cwt = cwt + bitmask * digitalRead(shtData);
    digitalWrite(shtClk, LOW);
    bitmask=bitmask/2;
  }
  return(cwt);
}

void SHT_Read_Byte(void) {
  ioByte = shiftIn();
  digitalWrite(shtData, ackBit);
  pinMode(shtData, OUTPUT);
  digitalWrite(shtClk, HIGH);
  digitalWrite(shtClk, LOW);
  pinMode(shtData, INPUT);
  digitalWrite(shtData, LOW);
}

void SHT_Connection_Reset(void) {
  shiftOut(shtData, shtClk, LSBFIRST, 255);
  shiftOut(shtData, shtClk, LSBFIRST, 255);
}

void SHT_Soft_Reset(void) {
  SHT_Connection_Reset();
  ioByte = 30;
  ackBit = 1;
  SHT_Write_Byte();
  delay(15);
}

void SHT_Wait(void) {
  delay(5);
  dly = 0;
  while (dly < 600) {
    if (digitalRead(shtData) == 0) dly=2600;
    delay(1);
    dly=dly+1;
  }
}

void SHT_Start(void) {
  digitalWrite(shtData, HIGH);
  pinMode(shtData, OUTPUT);
  digitalWrite(shtClk, HIGH);
  digitalWrite(shtData, LOW);
  digitalWrite(shtClk, LOW);
  digitalWrite(shtClk, HIGH);
  digitalWrite(shtData, HIGH);
  digitalWrite(shtClk, LOW);
}

void SHT_Measure(int vSvc) {
  SHT_Soft_Reset();
  SHT_Start();
  ioByte = vSvc;
  SHT_Write_Byte();
  SHT_Wait();
  ackBit = 0;
  SHT_Read_Byte();
  int msby;
  msby = ioByte;
  ackBit = 1;
  SHT_Read_Byte();
  retVal = msby;
  retVal = retVal * 0x100;
  retVal = retVal + ioByte;
  if (retVal <= 0) retVal = 1;
}

int SHT_Get_Status(void) {
  SHT_Soft_Reset();
  SHT_Start();
  ioByte = 7;
  SHT_Write_Byte();
  SHT_Wait();
  ackBit = 1;
  SHT_Read_Byte();
  return(ioByte);
}

void SHT_Heater(void) {
  SHT_Soft_Reset();
  SHT_Start();
  ioByte = 6;
  SHT_Write_Byte();
  ioByte = 4;
  SHT_Write_Byte();
  ackBit = 1;
  SHT_Read_Byte();
  delay(500);
  SHT_Soft_Reset();
  SHT_Start();
  ioByte = 6;
  SHT_Write_Byte();
  ioByte = 0;
  SHT_Write_Byte();
  ackBit = 1;
  SHT_Read_Byte();
}

void setup()
{
  pinMode(11, OUTPUT);
  digitalWrite(11, HIGH);
  pinMode(10, OUTPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);        // open serial
  SHT_Connection_Reset();
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  Serial.println("Hi");
}

void loop()
{
  while (Serial.available() > 1) {
    cmdByte = Serial.read();
    dataByte = Serial.read();
    switch (cmdByte) {
    case 65:  // C
      {
        if (dataByte == 66) k=1;
        break;
      }
    case 68:
      {
        k=0;
        break;
      }
    }
  }
  if (k==1) {
    msTimer=millis();
    if (msTimer <= logTime) {
      logTime = 0;
    }
    if (msTimer > (logTime + 1000)) {
      logTime = millis();
      SHT_Measure(3);
      Serial.print(" T ");
      Serial.print(retVal, DEC);
      Serial.print(" H ");
      SHT_Measure(5);
      Serial.print(retVal, DEC);
      Serial.println();
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

