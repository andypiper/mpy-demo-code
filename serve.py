# quick demo for EuroPython 2022
# based on @aallen Gist

import socket
import network
import machine


ssid = 'Explore-uPython'
password = 'Dublin2022'

led = machine.Pin("LED", machine.Pin.OUT)

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

html = """<!DOCTYPE html>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<html>
    <head> <title>Hello from Pico W</title> </head>
    <body style="font-family: sans-serif;"> <h1>EuroPython 2022</h1>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="150" height="150">
  <g fill="none">
    <path fill="#f18a00" d="M42 55.6a3 3 0 0 1 2.9 3 3 3 0 0 1-3 3.1 3 3 0 0 1-3-3 3 3 0 0 1 3-3zm8.9-38.5v7c0 5.6-4.7 10.2-10 10.2H25a8.1 8.1 0 0 0-8 8.1v15.3c0 4.3 3.8 6.8 8 8 5 1.6 9.9 1.8 16 0 4-1 7.9-3.4 7.9-8v-6.1h-16v-2h24c4.5 0 6.3-3.3 7.9-8.2 1.6-5 1.6-9.8 0-16.2-1.2-4.6-3.3-8.1-8-8.1z"/>
    <path fill="#3dae2b" d="M24 4.9a3 3 0 0 1 3 3 3 3 0 0 1-3 3 3 3 0 0 1-3-3 3 3 0 0 1 3-3zM32.6 0C30 0 27.3.2 25 .6c-6.7 1.2-8 3.8-8 8.4v6h16v2H11a10 10 0 0 0-9.9 8.2 30 30 0 0 0 0 16.2c1.2 4.8 3.9 8.1 8.5 8.1H15v-7.3c0-5.2 4.5-9.9 10-9.9h15.8a8 8 0 0 0 8-8.1V9c0-4.4-3.7-7.6-8-8.4-2.7-.4-5.6-.6-8.3-.6z"/>
    <path fill="#006e43" d="M48.9 12.7V8l-.1-.4c-.7-3.7-4-6.4-7.9-7a49 49 0 0 0-8-.7h-.3A45.5 45.5 0 0 0 23 1c-5 1.4-6 3.8-6 8v6h16v2H10.5l-.7.1h-.1l-.7.2h-.2l-.5.1-.3.1-.5.2h-.2l-.5.3-.3.1a7.5 7.5 0 0 0-.7.4l-.4.2-.3.3a16 16 0 0 0-1 .8l-.3.3-.2.2a10.1 10.1 0 0 0-.9 1.2l-.2.2-.3.6-.1.2-.3.7v.1a12.5 12.5 0 0 0-1 3v.1l-.1.8-.1.5v.4l-.2.6v.1a27 27 0 0 0-.3 6v1.5l.1.4v.5l.2.7V38.2l.6 2.6.1.6 1.1 3.1v.2h.1l.6 1.1.1.2.2.2.3.4v.1h.1c1 1.3 2.4 2.2 4 2.6h.2l.5.1h.2l1 .1h5.6v-7.3c0-5.2 4.5-9.9 9.9-9.9H40.9c.7 0 1.4-.1 2-.3h.2a6.7 6.7 0 0 0 1.1-.5h.3c2.6-1.4 4.4-4.2 4.4-7.3V12.7zm-24.2-1.8H23v-.1a2.5 2.5 0 0 1-.3-.1l-.2-.1a3 3 0 0 1-1.4-2V8A3 3 0 0 1 24 4.9h.6l.2.1h.1l.2.1h.1a1.9 1.9 0 0 1 .3.2h.1l.1.2h.2v.2h.2V6c.6.5.9 1.3.9 2a3 3 0 0 1-2.3 3zM1 38.6l1.3.5 1.5.4a13.8 13.8 0 0 0-2.4 1 37 37 0 0 1-.4-2zm40-6.8h-.5l.5-2.1a19 19 0 0 1 1.6 1.9l-1.7.2zm7.4-17.6-.6.5c-.6.7-.7 1.5-.4 2.3.2.6.5 1 1 1.2v6c0 3-1.9 5.7-4.5 7l-2.4-2c1.4-.3 2.7-.6 4-1.1.5-.3 1.1-.6 1.5-1 .6-.8.7-1.5.4-2.4-.3-.8-1-1.3-1.8-1.4H45V23a2.3 2.3 0 0 0-4.2-1.4c-.4.6-.6 1.3-.9 2l-.1.6A16 16 0 0 0 39 22c-.3-.6-.5-1.2-1-1.6-.7-.6-1.5-.7-2.3-.4-.9.3-1.3 1-1.5 1.8v.6H34c-1 0-2 .6-2.2 1.6-.4 1 0 2 .9 2.6.6.4 1.2.7 2 .9l1.4.4-1.4.5c-.6.2-1.2.5-1.6 1-.6.7-.7 1.5-.4 2.3H25c-2.7 0-5.4 1.2-7.4 3.2s-3 4.7-3 7.3V49h-5a7 7 0 0 1-4.8-1.7c.8 0 1.7-.3 2.1-1 .5-.6.7-1.3 1-2l.7-3c.6.6 1.8 1.9 2.2 2.8.6 1.1.5 1.3.5 1.3l1-1 1-1L12 43c-1-.4-2.2-1.6-2.9-2.2l4-1c.5-.3 1.1-.6 1.5-1.1.6-.7.7-1.5.4-2.3-.3-.8-.9-1.3-1.8-1.5h-.6v-.1a2.3 2.3 0 0 0-4.2-1.4c-.4.6-.6 1.3-.9 2l-.1.5-.7-2.2c-.3-.6-.5-1.2-1-1.6-.7-.6-1.5-.7-2.3-.4-.8.3-1.3.9-1.5 1.7v.6h-.2l-1.2.3c0-1.6 0-3.3.3-5l.5.1c1 .3 2 0 2.6-.9.4-.6.6-1.3.9-2l.7-3c.6.6 1.8 2 2.3 2.8.5 1.2.4 1.3.4 1.3l1-1 1-1-1.3-.4c-1-.5-2.2-1.7-2.8-2.3 1.3-.2 2.6-.5 3.8-1 .6-.3 1.2-.5 1.6-1 .6-.7.7-1.5.4-2.3l-.5-1H17l-.5 1.2v.6h-.2c-1 0-2 .6-2.2 1.6-.4 1 0 2 .8 2.6.6.4 1.3.7 2 .9l1.4.4-1.3.5c-.6.2-1.2.5-1.6 1-.6.7-.7 1.5-.4 2.3.3.8.9 1.3 1.7 1.5h.6v.1a2.3 2.3 0 0 0 4.2 1.4l1-2 .7-3c.6.6 1.8 1.9 2.2 2.8l.5 1.3 1-1 1-1-1.3-.4c-1-.5-2.3-1.7-2.9-2.3 1.3-.2 2.6-.5 3.9-1 .6-.3 1.2-.6 1.6-1 .6-.8.7-1.5.4-2.4-.3-.8-1-1.3-1.8-1.4h-.6V20a2.3 2.3 0 0 0-4.2-1.4c-.4.6-.6 1.3-.9 2l-.1.6-.7-2.3c-.2-.5-.4-1-.8-1.3H33l.6.2c1 .4 2 0 2.6-.9.5-.6.7-1.2 1-2l.7-3c.6.6 1.8 2 2.2 2.9l.5 1.2 1-1 1-1-1.3-.4c-1-.4-2.3-1.6-2.9-2.3 1.4-.2 2.7-.5 3.9-1 .6-.2 1.2-.5 1.6-1 .6-.7.7-1.5.4-2.3-.3-.8-1-1.3-1.8-1.5h-.6v-.2A2.3 2.3 0 0 0 37.6 4c-.4.6-.6 1.2-.9 2l-.1.5a16 16 0 0 0-.7-2.3l-1-1.6c-.8-.5-1.5-.7-2.4-.4-.8.3-1.3 1-1.4 1.8v.6h-.2c-1 0-2 .6-2.3 1.6-.3 1 .1 2 1 2.6.5.5 1.2.7 1.9 1 .5 0 1 .2 1.4.3l-1.3.5c-.6.2-1.2.5-1.6 1-.6.7-.7 1.5-.4 2.3l.3.6H17.5c.4-.1.7-.4 1-.8a22.4 22.4 0 0 0 1.6-5 22.6 22.6 0 0 1 2.2 2.9c.6 1 .5 1.3.5 1.3l1-1 .4-.4a3.5 3.5 0 0 0 3.2-3.6c0-1-.3-1.8-1-2.4.3-.5.3-1.1.1-1.7-.3-.8-1-1.3-1.8-1.5h-.6v-1l1-.2C27.3.7 30 .5 32.5.5h.3c2.7 0 5.4.2 8 .7 3.3.5 6.7 3 7.3 6.6-.8.1-1.4.7-1.7 1.5-.3 1 0 2 .9 2.6l1 .6z"/>
    <path fill="#ffcfa1" d="m65.2 37.4-.5 2.6c-.5.6-1.3 1-2 1.1a3 3 0 0 1-2.1-.2c-1.3-.7-1.4-2-.5-3a3.4 3.4 0 0 1 3.6-1.1V28l-3 .6-4.6.8c-.2 0-.2.1-.2.3V40c0 1.7-1 2.8-2.6 3 0 0-1.4 0-2.2-.4-.5-.2-.8-.6-.9-1.2a2 2 0 0 1 .5-1.7c1-1 2.1-1.3 3.5-1h.2v-13l9.5-1.6.4 1.3 1 4.8v7.3zM33 34.8c1 1.8 4.3 7.3 5.4 14.2h-3.3l-.5-2a27.6 27.6 0 0 0-3.4-7.7v23.4l1 1.7.3-.4c0-.1 3.2-5 3-12h3.3a27.8 27.8 0 0 1-.4 6.7 24.7 24.7 0 0 1-2.5 7.6 24.8 24.8 0 0 1-14.7-2.8l-2.5-7-1.1-3.3V42.4l.1-1.6a7.7 7.7 0 0 1 4.4-5.3c.6.5 1 .8 1.8.7.5 0 1.2-.6 2-1.4h7zm-12.6 4.5c-.8-.3-1.2-.6-1.4-.8v3l1.4 2.5v-4.7zm2.4.8c-.2 0-.5 0-.8-.2l-.6-.2v6l1.4 2.6V40zm2.5-.4-1.5.3v10l1.5 2.5zm2.4-1.2-1.4.8v15l1.4 2.4zm2.5-.5a4 4 0 0 0-.6-.5l-.2-.2-.2.2-.4.3v20.7l1.4 2.5V38zm13.5 5.8v.3h-1.3c-1 0-1.7.4-2.2 1.3-.6.8-.3 1.8.5 2.3a3 3 0 0 0 2 .3c1.5-.2 2.3-1.2 2.3-2.6V34.6c2.3.3 3.6 1.8 4.8 3.5a4.4 4.4 0 0 0-1.5-3l-1.9-1.4-.3-.3c-.8.4-1.6.8-2.4 1v9.4z"/>
  </g>
</svg>
        <p><br/>Enjoy exploring <a href="https://micropython.org">MicroPython</a>!<br/><br/>
        Thank you for coming! after the session, here are some places to learn more...
        <ul><li>Explore <a href="https://awesome-micropython.org">Awesome MicroPython</a></li>
        <li>Learn from <a href="https://https://bhave.sh/">Tutorials from Bhavesh</a></li>
        <li>Try the <a href="https://docs.wokwi.com/guides/micropython">Wokwi device simulator</a></li>
        <li>Read the <a href="https://forum.micropython.org">MicroPython forums</a></li>
        <li>Check out the <a href="https://twitter.com/search?q=micropython%20OR%20upython%20OR%20%22micro%20python%22%20OR%20mpython%20OR%20url%3Amicropython%20lang%3Aen&f=live">latest #MicroPython Tweets</a></li>
        </ul>
        Thanks again! -- <a href="https://andypiper.me">Andy</a>
        </p>
    </body>
</html>
"""

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

print('listening on', addr)
led.off()

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        led.on()
        print(request)

        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(html)
        cl.close()
        led.off()

    except OSError as e:
        cl.close()
        print('connection closed')
        

