import scipy.io.wavfile as wav
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np


def convolution(x, h):
    sizeH = np.size(h,0)
    hrev = np.zeros(h.shape)
    y = np.zeros((sizeH + np.size(x,0)-1))
    for i in range(sizeH):
        hrev[i] = h[sizeH-1-i]
    for j in range(np.size(x,0)):
        y[j:j+sizeH] +=np.multiply(x[j], hrev)
    return y

def writeImpulseResponse(y_zero, y_one, samp_rate, filename):
    y_zero /= np.max(np.abs(y_zero))
    y_one /= np.max(np.abs(y_one))
    y_zero *= 32767
    y_one *= 32767
    y = np.vstack((y_zero, y_one)).T
    y = np.asarray(y, dtype= np.int16)
    wav.write(filename, samp_rate, y)
    time = 1
    x_axis = np.linspace(0, time, time*samp_rate, endpoint=False)
    plt.plot(x_axis,y[:time*samp_rate,0])
    plt.show()

time = 1
croppedy2rate, cropy2 =wav.read("cropped_y2.wav")
x_axis = np.linspace(0, time, time*croppedy2rate, endpoint=False)
plt.plot(x_axis,cropy2[:time*croppedy2rate,0])
plt.show()
#print(np.max(cropy2[:,0])) max value for each channel is taken, will multiply with that value after normalization. 
#print(np.max(cropy2[:,1]))

sample_rateIn, x = wav.read('input.wav')
sample_rateh1, h1 = wav.read('h1.wav')
sample_rateh2, h2 = wav.read('h2.wav')
sample_rateh3, h3 = wav.read('h3.wav')

y1_zero = convolution(x[:,0],h1[:,0])
y1_one = convolution(x[:,1],h1[:,1])
writeImpulseResponse(y1_zero,y1_one, sample_rateIn, 'y1.wav')

y1numpy_zero = sig.fftconvolve(x[:,0],h1[:,0])
y1numpy_one = sig.fftconvolve(x[:,1],h1[:,1])

writeImpulseResponse(y1numpy_zero, y1numpy_one, sample_rateIn, 'y1numpy.wav')

y2_zero = convolution(x[:,0],h2[:,0])
y2_one = convolution(x[:,1],h2[:,1])
writeImpulseResponse(y2_zero,y2_one, sample_rateIn, 'y2.wav')

y2numpy_zero = sig.fftconvolve(x[:,0],h2[:,0])

y2numpy_one = sig.fftconvolve(x[:,1],h2[:,1])

writeImpulseResponse(y2numpy_zero, y2numpy_one, sample_rateIn, 'y2numpy.wav')

y3_zero = convolution(x[:,0],h3[:,0])
y3_one = convolution(x[:,1],h3[:,1])
writeImpulseResponse(y3_zero,y3_one, sample_rateIn, 'y3.wav')

y3numpy_zero = sig.fftconvolve(x[:,0],h3[:,0])
y3numpy_one = sig.fftconvolve(x[:,1],h3[:,1])

writeImpulseResponse(y3numpy_zero, y3numpy_one, sample_rateIn, 'y3numpy.wav')
