import argparse

import numpy as np
import simpleaudio as sa

parser = argparse.ArgumentParser()
parser.add_argument("--fs", default=44100, help="Sampling Frequency")
parser.add_argument("--nbit", default=16, help="Number of Bit")

parser.add_argument("--dur", default=5., help="Duration")
parser.add_argument("--f", default=300, help="Main Frequency")
parser.add_argument("--fbeat", default=2, help="Frequency of Beat")
parser.add_argument("--ntri", default=100, help="Number of Triangle")
parser.add_argument("--amp", default=1, help="amplitude")

args = parser.parse_args()

# Constant
FS = int(args.fs)
Nbit = int(args.nbit)

dur = float(args.dur)
f = float(args.f)
fbeat = float(args.fbeat)
Ntri = int(args.ntri)
AMP = float(args.amp)


def clip(v, a, b):
    if v < a:
        return a
    elif b < v:
        return b
    return v
assert clip(-1, 0, 1) == 0.
assert clip(0.5, 0, 1) == 0.5
assert clip(1.1, 0, 1) == 1.

dur = clip(dur, 1, 10)
f = clip(f, 30, 10000)
fbeat = clip(fbeat, 1, 100)
Ntri = clip(Ntri, 1, 100)
AMP = clip(AMP, 0, 1)

# Times
Nt = int(FS * dur)
n = np.arange(Nt)

# Tone
S = 0
for tr in range(Ntri):
    S += np.sin(2 * np.pi * (2*tr+1)*f * n / FS)
S /= Ntri

# Rhyzm (Harf sin)
S *= np.sin(2 * np.pi * fbeat * n / FS).clip(0, 1)

# Clip
S = np.clip(S, -1, 1)

# Convert to Integer
Bit = (2**Nbit)/2
S = Bit * S

# Volume
S = AMP * S

# Integer space
audio = S.astype(np.int16)

play_obj = sa.play_buffer(audio, 1, int(Nbit/8), int(FS))

play_obj.wait_done()


