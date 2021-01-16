import array
import math
import simpleaudio as sa

FS = 44100/2/2
Nbit = 16

dur = 2.0
f = 1000.
AMP = 0.8


def clip(x, xmin, xmax):
	_y = [xi if xi>=xmin else xmin for xi in x]
	_z = [yi if yi<=xmax else xmax for yi in _y]
	return _z

def sin(a, ts):
	return [math.sin(a*t) for t in ts]


ts = range(int(FS * dur))
Nts = len(ts)

S = [ math.sin(2*3.14*f*n/FS) for n in ts ]
S = [ int( AMP * (2**16 / 2) * si ) for si in S ]

print(min(S))
print(max(S))
print("len", len(S))

ary = array.array("i") # H is unsigned short 2Byte=16bit
ary.fromlist(S)
audio = ary.tobytes()

play_obj = sa.play_buffer(audio, 1, int(Nbit/8), int(FS))
play_obj.wait_done()

print("Done test")
