import numpy as np
import simpleaudio as sa

CH = 1

FS = 44100 / 2
Nbit = 16

dur = 5.0
f = 440.
amp = 0.5

# times
Nt = int(dur * FS)
t = np.linspace(0, dur, Nt, False)

# signal
S = np.sin(2 * 3.14 * f * t)

# Volume
S = amp * S

# Normalize
S *= 32767 / max(abs(S)) 
S = S.astype(np.int16)


# Stereo
if CH == 1:
	audio = S

	audio = audio.astype(np.int16)

	play_obj = sa.play_buffer(audio, 1, int(Nbit/8), int(FS))
	play_obj.wait_done()

elif CH == 2:
	
	audio = np.zeros((Nt, 2))

	audio[:, 0] = +1 * S   # GPIO13
	audio[:, 1] = -1 * S   # GPIO18

	audio = audio.astype(np.int16)

	play_obj = sa.play_buffer(audio, 2, int(Nbit/8), int(FS))
	play_obj.wait_done()

print("Done test")

