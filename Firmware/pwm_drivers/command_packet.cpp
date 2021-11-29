// 
// 
// 

#include "command_packet.h"

/*
uint32_t read_command(uint32_t* command_buffer)
{
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
			if (int(command_packet[0]) == 1)
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
				dose_food(&water_pump1, 10);
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
}
*/