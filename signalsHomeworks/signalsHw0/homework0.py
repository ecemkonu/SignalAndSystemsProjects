import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import signal
from scipy.io import wavfile
import vispy.visuals.spectrogram as spectrogram

A = np.random.randn(4,3)
B = np.sum(A, axis = 1, keepdims = True)
print(B.shape)
time = np.arange(-100*np.pi,100*np.pi,0.01) 
theta = 2* time+np.pi/2
x = np.sin(theta)
expX = (np.exp(1j*theta)-np.exp(-1j*theta))/(2j)


sample_rate, samples = wavfile.read('spec.wav')
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

plt.pcolormesh(times, frequencies, spectrogram)
plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
plt.clf()

plt.figure('different')

plt.subplot(211)
plt.title('Sinusoidal Function')
plt.plot(time, x)
plt.xlabel('time')
plt.ylabel('value')

plt.subplot(212)
plt.title('Eulerian Representation')
plt.plot(time,expX)
plt.xlabel('time')
plt.ylabel('value')
plt.show()

plt.close()


x1 = (np.sin(3*theta+np.pi/2))
x2 = (np.sin(3*theta+np.pi/3))
x3 = (np.sin(theta+np.pi/2))
x4 = (np.sin(theta+np.pi/4))
x5 = (np.cos(theta+np.pi/6))
x6 = (np.cos(3*theta))
x7 = (np.cos(2*theta+np.pi/4))
x8 = (np.cos(3*theta+np.pi/3))
x9 = (np.cos(theta+np.pi))

wavfile.write('summedSignalR1.wav', 44100, x1+x2+x3+x4+x5+x6+x7+x8+x9)
wavfile.write('summedSignalR2.wav', 22050, x1+x2+x3+x4+x5+x6+x7+x8+x9)
wavfile.write('summedSignalR3.wav', 11025, x1+x2+x3+x4+x5+x6+x7+x8+x9)

fs1, data1 = wavfile.read('summedSignalR1.wav')
fs2, data2 = wavfile.read('summedSignalR2.wav')
fs3, data3 = wavfile.read('summedSignalR3.wav')


input_data = wavfile.read('summedSignalR3.wav')
audio = input_data[1]
# plot the first 1024 samples
plt.plot(audio[0:1024])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Sample Wav")
# display the plot
plt.show()
