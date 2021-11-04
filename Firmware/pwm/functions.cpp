// 
// 
// 

#include "functions.h"

void PWM_Calibration(PWM_Pump pwm_pump)
{
	uint8_t gpio_pin, min, max;
	gpio_pin = pwm_pump.pin;
	min = pwm_pump.min;
	max = pwm_pump.max;
	
	for (int i = min; i <= max; i += 5) {
		analogWrite(gpio_pin, i);
		delay(100);
	}
	for (int i = max; i >= min; i -= 5) {
		analogWrite(gpio_pin, i);
		delay(100);
	}
	analogWrite(gpio_pin,0);
}

void PWM_set_percent(PWM_Pump pwm_pump, uint8_t percent)
{
	uint8_t gpio_pin, min, max, pulse_width, working_range;
	gpio_pin = pwm_pump.pin;
	min = pwm_pump.min;
	max = pwm_pump.max;
	working_range = max - min;

	if (percent == 0)
	{
		analogWrite(gpio_pin, 0);
	}
	else if (percent == 100)
	{
		analogWrite(gpio_pin, max);
	}
	else if ((percent < 100) && (percent > 0)) {
		pulse_width = min + ((percent/100) * working_range);
		Serial.println(pulse_width);
		analogWrite(gpio_pin, pulse_width);
	}
	else
	{
		return;
	}
	return;
}



