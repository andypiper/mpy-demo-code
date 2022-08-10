# Mini SAM M4 MicroPython example
# using @robert-hh SAMD improvements

# requires Matt Trentini's DotStar library
# gh repo clone mattytrentini/micropython-dotstar
from micropython_dotstar import DotStar
from machine import Pin, SoftSPI, LED
import time

# setup the RGB LED on the left leg
# final param (miso) can be any unused pin
spi = SoftSPI(sck=Pin("DOTSTAR_CLK"), mosi=Pin("DOTSTAR_DATA"), miso=Pin(17)) 
dot = DotStar(spi, 1) # single LED (DotStar supports multiple, board has one)

# todo - some kind of rainbow cycle to run in background
dot[0] = (5, 12, 59, 0.3) # light the LED 

# turn on the red chest LED
led = LED("LED")
button = Pin("BUTTON", Pin.IN, Pin.PULL_UP)

# trivial button press debounce could be improved
while True:
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    if first and not second:
        led.toggle()
        print('Button pressed, toggle LED')



