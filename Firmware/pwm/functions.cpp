// 
// 
// 

#include "functions.h"

void PWM_Calibration(uint8_t gpio_pin, uint8_t min, uint8_t max)
{
	for (int i = min; i <= max; i += 5) {
		analogWrite(gpio_pin, i);
		delay(100);
	}
	for (int i = max; i >= min; i -= 5) {
		analogWrite(gpio_pin, i);
		delay(100);
	}
}



