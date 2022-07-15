# shamelessly borrowed from Les Pounder's Tweet
# requires urequests to be installed

import network
import urequests
import time
from sekrit import SSID, PW 

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(SSID, PW)

print(wlan.isconnected())

astronauts = urequests.get("http://api.open-notify.org/astros.json").json()

number = astronauts['number']

for i in range(number):
    print(astronauts['people'][i]['name'])

