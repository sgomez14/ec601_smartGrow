#include "lightsensor.h"

Adafruit_TSL2591 tsl = Adafruit_TSL2591(2591);

void light_sensor_init_info(void)
{
  /* Display the gain and integration time for reference*/  
  Serial.println(F("------------------------------------"));
  Serial.print  (F("Gain:         "));
  tsl2591Gain_t gain = tsl.getGain();
  switch(gain)
  {
    case TSL2591_GAIN_LOW:
      Serial.println(F("1x (Low)"));
      break;
    case TSL2591_GAIN_MED:
      Serial.println(F("25x (Medium)"));
      break;
    case TSL2591_GAIN_HIGH:
      Serial.println(F("428x (High)"));
      break;
    case TSL2591_GAIN_MAX:
      Serial.println(F("9876x (Max)"));
      break;
  }
  Serial.print  (F("Timing:       "));
  Serial.print((tsl.getTiming() + 1) * 100, DEC); 
  Serial.println(F(" ms"));
  Serial.println(F("------------------------------------"));
  Serial.println(F(""));
}

void init_light_sensor(void){
 /* 
  Set Gain option:
  TSL2591_GAIN_LOW  // 1x gain (bright light)
  TSL2591_GAIN_MED  // 25x gain
  TSL2591_GAIN_HIGH // 428x gain

  Set Timing option:
  TSL2591_INTEGRATIONTIME_100MS  // shortest integration time (bright light)
  TSL2591_INTEGRATIONTIME_200MS
  TSL2591_INTEGRATIONTIME_300MS
  TSL2591_INTEGRATIONTIME_400MS
  TSL2591_INTEGRATIONTIME_500MS
  TSL2591_INTEGRATIONTIME_600MS  // longest integration time (dim light)
*/

  tsl.setGain(TSL2591_GAIN_MED); 

  tsl.setTiming(TSL2591_INTEGRATIONTIME_300MS);

}


void print_light_data(void)
{
  // Read 32 bits with top 16 bits IR, bottom 16 bits full spectrum
  uint32_t lum = tsl.getFullLuminosity();
  uint16_t ir, full;
  ir = lum >> 16;
  full = lum & 0xFFFF;
  Serial.print(F("[ ")); Serial.print(millis()); Serial.print(F(" ms ] "));
  Serial.print(F("IR: ")); Serial.print(ir);  Serial.print(F("  "));
  Serial.print(F("Full: ")); Serial.print(full); Serial.print(F("  "));
  Serial.print(F("Visible: ")); Serial.print(full - ir); Serial.print(F("  "));
  Serial.print(F("Lux: ")); Serial.println(tsl.calculateLux(full, ir), 6);
}
