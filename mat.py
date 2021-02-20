import matplotlib.pyplot as plt
fig, ax = plt.subplots()

ax.plot(time, audio)
ax.set(xlabel='Time(s)', ylabel='Sound Amplitude')
plt.show()

