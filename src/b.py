import argparse
print("loading ..")
import numpy as np
print("Loaded")
import simpleaudio as sa

parser = argparse.ArgumentParser()
parser.add_argument("--fs", default=44100, help="Sampling Frequency")
parser.add_argument("--nbit", default=16, help="Number of Bit")

parser.add_argument("--dur", default=5., help="Duration")
parser.add_argument("--f", default=1000, help="Main Frequency")
parser.add_argument("--fbeat", default=2, help="Frequency of Beat")
parser.add_argument("--ntri", default=1, help="Number of Triangle")
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

dur = np.clip(dur, 1, 10)
f = np.clip(f, 30, 10000)
fbeat = np.clip(fbeat, 1, 100)
Ntri = np.clip(Ntri, 1, 100)
AMP = np.clip(AMP, 0, 1)

# Times
Nt = int(FS * dur)
t = np.linspace(0, dur, Nt, False, dtype=np.float)

# Tone
buf = np.zeros((Nt, Ntri), dtype=np.float)

for tr in range(Ntri):
    buf[:, tr] = np.sin(2 * np.pi * (2*tr+1)*f * t)

S = buf.mean(axis=1)

# Rhyzm (Harf sin)
S *= np.sin(2 * np.pi * fbeat * t).clip(0, 1)

# Normalize
S *= 32767 / np.max(np.abs(S)) 

# Protected from Clipping
S = 0.5 * S


# Integer space
audio = S.astype(np.int16)

play_obj = sa.play_buffer(audio, 1, int(Nbit/8), int(FS))

play_obj.wait_done()














