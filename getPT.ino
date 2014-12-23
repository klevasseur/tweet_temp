#include <Wire.h>
#include <Adafruit_MPL115A2.h>

Adafruit_MPL115A2 mpl115a2;

void setup(void) 
{
  Serial.begin(9600);
  Serial.println("Starting\n");
 
  mpl115a2.begin();
}

void loop(void) 
{
  float pressureKPA = 0, pressureINHG=0,temperatureC = 0,temperatureF=0;    

  mpl115a2.getPT(&pressureKPA,&temperatureC);
  pressureINHG=0.295301*pressureKPA;
  temperatureF=9*temperatureC/5+32.;
  Serial.print(pressureINHG, 4); Serial.print(" ");
  Serial.print(temperatureF, 1); Serial.println("\n");
   
  delay(500);
}
