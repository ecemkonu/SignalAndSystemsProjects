import scipy.io.wavfile as wav
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import cv2
import moviepy.editor as mpe

matplotlib.use("Agg")

fps = 10
sample_rateIn, x = wav.read('SilentKnight.wav')
visualInterval = sample_rateIn/fps
fullSize = math.ceil(x.shape[0]/sample_rateIn)*sample_rateIn
x_padded = np.zeros((fullSize,2))
x_padded[:x.shape[0], :x.shape[1]] = x

visSize = fullSize//4410
ft = np.zeros(x_padded.shape,dtype=complex)

for i in range(visSize):
    ft[i*4410:(i+1)*4410] = 10*(np.log(np.fft.fft(x_padded[i*4410:(i+1)*4410])+0.002))



fig, ax = plt.subplots( nrows=1, ncols=1,figsize=(10, 6))
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (1000,600))
for i in range(visSize):
    ax.plot(x_padded[i:i*4410])
    plt.savefig('snap.png', format='png')
    ax.clear()
    X = cv2.imread("snap.png")
    out.write(X)
out.release()

my_clip = mpe.VideoFileClip("output.avi")
audio_background = mpe.AudioFileClip("SilentKnight.wav")
final_clip = my_clip.set_audio(audio_background)
final_clip.write_videofile('total_output.mp4')