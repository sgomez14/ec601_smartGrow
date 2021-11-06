// 
// 
// 
#include "pwm_functions.h"

/* {Pin Number, min voltage, max voltage} */
PWM_device water_pump1 = { 33, 145, 255 };
PWM_device water_pump2 = { 36, 180, 255 };
PWM_device food_pump = { 36, 180, 255 };
PWM_device air_pump = { 23, 50, 200 };
PWM_device LED = { 37, 145, 255 };
String command_packet = "";

/* Use PWM_Calibration to find the operating range for your motors and devices. This is used to set up your PWM_device structs' min and max value. */
void PWM_calibration(PWM_device *pwm_device)
{
	/* Making local copies for code readability. */
	uint8_t gpio_pin, min, max;
	gpio_pin = pwm_device->pin;
	min = pwm_device->min;
	max = pwm_device->max;
	
	/* Runs through entire operating range for PWM device. */
	for (int i = min; i <= max; i += 5) {
		analogWrite(gpio_pin, i);
		delay(100);
	}
	for (int i = max; i >= min; i -= 5) {
		analogWrite(gpio_pin, i);
		delay(100);
	}

	/* Ensures PWM device is off at end of function. */
	analogWrite(gpio_pin,0);
}

/* Sets a PWM device to a specific pulse width, determined by percent. 0% turns off device, and 100% turns it to the device's max. */
void PWM_set_percent(PWM_device *pwm_device, uint8_t percent)
{
	/* Making local copies for code readability. */
	uint8_t gpio_pin, min, max, pulse_width, working_range;
	gpio_pin = pwm_device->pin;
	min = pwm_device->min;
	max = pwm_device->max;
	working_range = max - min;

	/* If percent is 0, turn device off. */
	if (percent == 0)
	{
		analogWrite(gpio_pin, 0);
	}
	/* If percent is 100, turn device to max. */
	else if (percent == 100)
	{
		analogWrite(gpio_pin, max);
	}
	/* In between, calculate pulse_width based on offset and percent of max working range for the specific pump. */
	else if ((percent < 100) && (percent > 0)) {
		pulse_width = min + ((percent/100) * working_range);
		analogWrite(gpio_pin, pulse_width);
	}
	else
	{
		Serial.println("Parameter Error: Outside range (0 - 100).");
		return;
	}
	return;
}

/* Doses food from a food source via a small (~250 ms) delay based on mL input. Needs the global macro FILL_RATE set depending on physical system measurements. */
void dose_food(PWM_device *pwm_device, uint8_t ml)
{
	/* Making local copies for code readability. */
	/* dose_run_time is in milliseconds. */
	uint32_t dose_run_time;
	uint8_t gpio_pin, min, max, pulse_width, working_range;
	gpio_pin = pwm_device->pin;
	min = pwm_device->min;
	max = pwm_device->max;
	working_range = max - min;

	dose_run_time = 1000*(ml / FILL_RATE); //(ml / (ml/s) == ml * (s/ml)
	/* Printing for debug */
	Serial.print("dose_run_time: ");
	Serial.println(dose_run_time);

	/* Setting 10% duty cycle for more accurate dosing. Compiler should simplify this. */
	pulse_width = min + ((10 / 100) * working_range);

	//Need to do: Calibrate pump by measuring how long it takes to does 100 ml of water.

	/* Starts pump for time based on dose_run_time. */
	Serial.println("Timer Started.");
	analogWrite(gpio_pin, pulse_width);
	delay(dose_run_time);
	Serial.println("Timer Expired.");
	analogWrite(gpio_pin, 0);

	return;
}	

