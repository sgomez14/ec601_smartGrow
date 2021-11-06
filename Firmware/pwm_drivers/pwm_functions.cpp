// 
// 
// 

#define FILL_RATE 10 //ml per second

#include "pwm_functions.h"

void PWM_Calibration(PWM_Pump *pwm_pump)
{
	uint8_t gpio_pin, min, max;
	gpio_pin = pwm_pump->pin;
	min = pwm_pump->min;
	max = pwm_pump->max;
	
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

void PWM_set_percent(PWM_Pump *pwm_pump, uint8_t percent)
{
	uint8_t gpio_pin, min, max, pulse_width, working_range;
	gpio_pin = pwm_pump->pin;
	min = pwm_pump->min;
	max = pwm_pump->max;
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
		analogWrite(gpio_pin, pulse_width);
	}
	else
	{
		return;
	}
	return;
}

void Dose_food(PWM_Pump* pwm_pump, uint8_t ml)
{
	uint32_t dose_run_time;
	uint8_t gpio_pin, min, max, pulse_width, working_range;
	gpio_pin = pwm_pump->pin;
	min = pwm_pump->min;
	max = pwm_pump->max;
	working_range = max - min;
	/* dose_run_time is in milliseconds. */
	dose_run_time = 1000*(FILL_RATE / ml); 
	

	/* Setting 10% duty cycle for more accurate dosing. Compiler should simplify this. */
	pulse_width = min + ((10 / 100) * working_range);

	//Need to do: Calibrate pump by measuring how long it takes to does 100 ml of water at 20% duty cycle.

	/* Dosing is measured by calling a global variable in main of type elapsedMillis*/
	Serial.println("Timer Started.");
	analogWrite(gpio_pin, pulse_width);
	delay(dose_run_time);
	Serial.println("Timer Expired.");
	analogWrite(gpio_pin, 0);

	return;
}	

