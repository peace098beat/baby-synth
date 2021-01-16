import time
from gpiozero import MCP3008


adc1 = MCP3008(channel=0)
adc2 = MCP3008(channel=1)
adc3 = MCP3008(channel=2)
adc4 = MCP3008(channel=3)
adc5 = MCP3008(channel=4)
adc6 = MCP3008(channel=5)
adc7 = MCP3008(channel=6)
adc8 = MCP3008(channel=7)


while True:
    
    s = "1:{:0.1f}2:{:0.1f}3:{:0.1f}4:{:0.1f}5:{:0.1f}6:{:0.1f}7:{:0.1f}8:{:0.1f}".format(
        adc1.value, adc2.value, adc3.value, adc4.value,
        adc5.value, adc6.value, adc7.value, adc8.value,
        )

    print(s)

    time.sleep(0.1)