import RPi.GPIO as GPIO
import time

from sensorReadings import *

print(str(getWaterLevel()))
print(str(getSoilMoisture()))
print(str(getTemp()))
print(str(getHum()))
