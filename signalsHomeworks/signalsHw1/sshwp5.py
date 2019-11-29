import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy import signal as sci

sampRate = 5000
f11 = 1100
f12 = 1099

f21 = 1100
f22 = 1094
time = 10

x_axis = np.linspace(0, time, time*sampRate, endpoint=False)
bSignal1 = np.cos(2*np.pi*f11* x_axis)*np.cos(2*np.pi*f12 *x_axis)
bSignal2 = np.cos(2*np.pi*f21* x_axis)* np.cos(2*np.pi*f22 *x_axis)

plt.figure('beatSignal')
plt.subplot(211)
plt.title('First beat signal- 1100 1099hz')
plt.plot(x_axis,bSignal1)

plt.subplot(212)
plt.title('Second beat signal- 1100 1094hz')
plt.plot(x_axis,bSignal2)

plt.show()

wav.write('firstBeat.wav',sampRate,bSignal1)
wav.write('secondBeat.wav',sampRate,bSignal2)
