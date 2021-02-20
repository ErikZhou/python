import librosa
import sys
import numpy as np
import matplotlib.pyplot as plt
#apt-get install ffmpeg

audio = sys.argv[1]
audio, freq = librosa.load(audio)
time = np.arange(0, len(audio)) / freq
print(len(audio), type(audio), freq, sep="\t")

'''
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='Time(s)', ylabel='Sound Amplitude')
plt.show()
'''

import  librosa.display
audio, _ = librosa.effects.trim(audio)#Trim leading and trailing #silence from an audio signal.
librosa.display.waveplot(audio, sr=freq)
plt.show()

