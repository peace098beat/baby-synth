from gpiozero import MCP3008, PWMLED
from signal import pause

light = MCP3008(channel=0)
led = PWMLED(17)

led.source = light.values

pause()