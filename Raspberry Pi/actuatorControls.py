from os import system
import time
from datetime import datetime
import requests

waterUrl = 'https://speeve-ponics.herokuapp.com/conditions/watering'

light = 3
motor = 5
for i in [light, motor]:
    system('gpio -1 mode '+str(i)+' out')

def motorOn():
    system('gpio -1 write '+str(motor)+' 1')

    data = {
        "timestamp": datetime.now(),
        "plant": 1,
        "pond": 1,
        "motor": True
    }

    r = requests.post(waterUrl, data)

def motorOff(condition = ''):
    if condition is "initial":
        system('gpio -1 write '+str(motor)+' 0')
    else:
        system('gpio -1 write '+str(motor)+' 0')

        data = {
            "timestamp": datetime.now(),
            "plant": 1,
            "pond": 1,
            "motor": False
        }

        r = requests.post(waterUrl, data)

def lightOn():
    system('gpio -1 write '+str(light)+' 1')

def lightOff():
    system('gpio -1 write '+str(light)+' 0')
