# Mini SAM M4 MicroPython example
# using @robert-hh SAMD improvements

# requires Matt Trentini's DotStar library
# gh repo clone mattytrentini/micropython-dotstar
from micropython_dotstar import DotStar
from machine import Pin, SoftSPI, LED

# setup the RGB LED on the left leg
# final param (miso) can be any unused pin
spi = SoftSPI(sck=Pin("DOTSTAR_CLK"), mosi=Pin("DOTSTAR_DATA"), miso=Pin(17)) 
dot = DotStar(spi, 1) # single LED (DotStar supports multiple, board has one)

# todo - some kind of rainbow cycle
dot[0] = (25, 128, 20, 0.1) # light the LED blue

# turn on the LED
led = LED("LED")

# todo - debounce button press
button = Pin("BUTTON", Pin.IN, Pin.PULL_UP)

while True:
    if button.value():
        print("Button pressed")
        led.on()
    else:
        led.off()

