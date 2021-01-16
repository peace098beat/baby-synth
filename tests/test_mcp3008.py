from gpiozero import MCP3008

adc = MCP3008(channel=0)

a = 0.5
buf = 0
while True:
	buf = a*buf + (1-a)*adc.value
	print(buf)
