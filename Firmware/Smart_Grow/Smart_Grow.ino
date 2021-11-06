/*
 Name:		Smart_Grow.ino
 Created:	10/7/2021 7:58:56 PM
 Author:	bmk

 Notes:
 Motor & MOSFET Wiring: https://www.youtube.com/watch?v=3PkpOeHTnfo
 Air Pump: https://www.youtube.com/watch?v=nGVykVrly9g


*/

#include "pwm_functions.h"

// the setup function runs once when you press reset or power the board

/*  Sample data packet (8 bits command, 24 bits data): 0000000 00000000 00000000 00000000

   |0.Fill|1.Empty|2.Airpump|3.Food|4.LED|5|6|7|   |8-31 data|

*/

PWM_Pump pump1 = { 33, 145, 255 };
PWM_Pump pump2 = { 36, 180, 255 };
PWM_Pump air_pump = { 23, 50, 200 };
PWM_Pump LED = { 37, 145, 255 };

elapsedMillis time_to_fill;
//Convert this command_packet to a byte. https://www.arduino.cc/en/Tutorial/Foundations/BitMask
String command_packet;


void setup() {
	Serial.begin(9600);
	while (!Serial) {
		; // wait for serial port to connect. Needed for native USB
	}

	pinMode(13, OUTPUT);
	pinMode(LED.pin, OUTPUT);
	digitalWrite(13, HIGH);

	Serial.println("Initial 2 sec delay:");
	delay(2000);

	//PWM_Calibration(pump2);
}

// the loop function runs over and over again until power down or reset
void loop() {

	//PWM_Calibration(&air_pump);
	PWM_set_percent(&air_pump, 1);

	if (Serial.available() > 0) {
		// read the incoming byte:
		command_packet = Serial.readString();

		//Serial.println(command_packet.length());
		//Rough error catching. Needs to actually check input is binary, so probably just accept a character input and convert it to an 8-bit bitmask.
		if (command_packet.length() != 8)
		{
			Serial.println("Incorrect Command Packet!");
		}
		else
		//Enter Command Center
		{
			if (int(command_packet[0])==1)
			{
				Serial.println(command_packet[0]);
			}
			if (int(command_packet[1]) == 1)
			{
				Serial.println(command_packet[1]);
			}
			if (int(command_packet[2]) == 1)
			{
				Serial.println(command_packet[2]);
			}
			if (int(command_packet[3]) == 1)
			{
				Serial.println(command_packet[3]);
				Dose_food(&pump1, 10);
			}
			if (int(command_packet[4]) == 1)
			{
				Serial.println(command_packet[4]);
			}
			if (int(command_packet[5]) == 1)
			{
				Serial.println(command_packet[5]);
			}
			if (int(command_packet[6]) == 1)
			{
				Serial.println(command_packet[6]);
			}
			if (int(command_packet[7]) == 1)
			{
				Serial.println(command_packet[7]);
			}
		}

		Serial.println(command_packet);
	}
	


	digitalWrite(13, HIGH);
	delay(1000);
	digitalWrite(13, LOW);
	delay(1000);
}
