
import time
import numpy as np
import simpleaudio as sa

import random

from gpiozero import MCP3008, LED

adc1 = MCP3008(channel=0)
adc2 = MCP3008(channel=1)
adc3 = MCP3008(channel=2)
adc4 = MCP3008(channel=3)
adc5 = MCP3008(channel=4)
adc6 = MCP3008(channel=5)
adc7 = MCP3008(channel=6)
adc8 = MCP3008(channel=7)

led1 = LED(17)



def r(a, b):
    return random.uniform(a, b)



def scale(s, vmin, vmax):
    a = (vmax-vmin) * s
    v = a + vmin
    return v


def read_ad():
    params = {}
    params["fs"] = 44100/2/2 # FIX
    params["n_bit"] = 16 # FIX

    params["dur"] = 8 #scale(adc1.value, 1, 3)
    params["f"] = 220 * scale(adc2.value, 1, 4)  * r(0.95, 1.05) #scale(adc2.value, 400, 1000)
    params["f_beat"] = 2 * scale(adc3.value, 1, 2)
    params["n_tri"] = int(scale(adc4.value, 1, 20))
    params["tempo_dur"] = (params["dur"] / 4) + r(-0.15, 0.15) # scale(adc5.value, 1, 4)

    params["amp"] = 1 # scale(adc6.value, 0., 1.)

    return params


def play_sound(params):
    fs = params["fs"]
    n_bit = params["n_bit"]
    assert n_bit == 16, n_bit
    dur = params["dur"]
    f = params["f"]
    f_beat = params["f_beat"]
    n_tri = params["n_tri"]
    amp = params["amp"]

    Nt = int(fs * dur)
    t = np.linspace(0, dur, Nt, False, dtype=np.float)

    # Tone
    buf = np.zeros((Nt, n_tri), dtype=np.float)
    for tr in range(n_tri):
        buf[:, tr] = (1./(tr+1)) * np.sin(2 * np.pi * (2*tr+1)*f * t)
    S = buf.mean(axis=1)

    # Beat
    S *= np.sin(2 * np.pi * f_beat * t).clip(0, 1)

    S *= 32767 / np.max(np.abs(S)) 
    S = amp * S
    audio = S.astype(np.int16)

    play_obj = sa.play_buffer(audio, 1, int(n_bit/8), int(fs))

    return play_obj



def main():

    hundlers = []

    while True:

        led1.toggle()

        for h in hundlers:
            if h.is_playing():
                pass
            else:
                hundlers.remove(h)
                pass

        Nh = len(hundlers)
        print(Nh)

        params = read_ad()

        Na = max(3, Nh)
        params["amp"] = 1./ (Na)
        print(params)

        hundler = play_sound(params)

        hundlers.append(hundler)

        time.sleep(params["tempo_dur"])


if __name__ == "__main__":
    main()






