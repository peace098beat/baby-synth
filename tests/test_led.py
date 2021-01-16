import time
from gpiozero import LED

led = LED(17)

while True:
    led.toggle()
    time.sleep(0.1)
