# shamelessly borrowed from Les Pounder's Tweet
# requires urequests to be installed
# (a default library on Pico W)

import network
import urequests

from sekrit import SSID, PW 

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(SSID, PW)

astronauts = urequests.get("http://api.open-notify.org/astros.json").json()

number = astronauts['number']

print(f'There are {number} humans in space at the moment!\r\n')

for i in range(number):
    print(astronauts['people'][i]['name'] + ' - ' + astronauts['people'][i]['craft'])

