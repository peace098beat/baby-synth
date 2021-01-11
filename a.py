import numpy as np
import simpleaudio as sa

FS = 44100

T = 20.0
f = 6000
fbeat = 2.8
tri = 9


Nt = int(FS * T)
n = np.arange(Nt)

# Tone
# S = np.sin(2 * np.pi * f * n / FS)
S = 0
for tr in range(tri):
    S += np.sin(2 * np.pi * (2*tr+1)*f * n / FS)

# Rhyzm
S *= np.sin(2 * np.pi * fbeat * n / FS).clip(0, 1)

# Integer
Bit = (2**16)/2
sig = Bit * np.clip(S, -1, 1)

AMP = 1e-2
sig = AMP * sig

# Integer space
audio = sig.astype(np.int16)
print(S.min(), S.max())

play_obj = sa.play_buffer(audio, 1, 2, FS)

play_obj.wait_done()

print("done")

