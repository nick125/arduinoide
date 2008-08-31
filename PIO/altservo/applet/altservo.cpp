#include "WProgram.h"
unsigned int servoPins[] = {0, 1};// Control pins for servo motor
int pulseWidth[] =  {0, 0};	// Amount to pulse the servo
long lastPulse[] = {0, 0};	// the time in millisecs of the last pulse
int minPulse = 700;		// minimum pulse width
int servoIdx = 0;

#define ARR_SIZE(arr) (sizeof(arr) / sizeof(*arr))

void servo_setup()
{
	unsigned int idx;
	for (idx = 0; idx < ARR_SIZE(servoPins); idx++) {
		pinMode(servoPins[idx], OUTPUT);
		pulseWidth[idx] = minPulse;
	}
}

void servo_update(unsigned int idx)
{
	unsigned int refreshTime = 20;
	if (millis() - lastPulse[idx] >= refreshTime) {
		digitalWrite(servoPins[idx], HIGH);	// Turn the motor on
		delayMicroseconds(pulseWidth[idx]);	// Length of the pulse sets the motor position
		digitalWrite(servoPins[idx], LOW);	// Turn the motor off
		lastPulse[idx] = millis();		// save the time of the last pulse
	}
}

void servo_loop()
{
	unsigned int idx;
	for (idx = 0; idx < ARR_SIZE(servoPins); idx++)
		servo_update(idx);
}


void setup() {
	Serial.begin(19200);
	servo_setup();
}

void loop() {
	int bytes = serialAvailable();

        while (bytes--) {
                char byte;
                int val;

                byte = serialRead();
                val = byte;
		switch(byte) {
			case '0' ... '9':
				val = val - '0';        // convert from character to number
				val = val * (180/9);    // convert from number to degrees
				pulseWidth[servoIdx] = (val * 9) + minPulse;  // convert angle to microseconds
				Serial.print(">>> Moving servo #");
				Serial.print(servoIdx);
				Serial.print(" to ");
				Serial.print(pulseWidth[servoIdx], DEC);
				Serial.println("");
				break;
			default:
				Serial.println("Unknown Command");
				break;
		}
	}

	/* Now we do the servo jazz */
	servo_loop();
}
int main(void)
{
	init();

	setup();
    
	for (;;)
		loop();
        
	return 0;
}

