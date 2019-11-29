from pydub import AudioSegment
from scipy import signal
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np
from mp3Read import convert

def createFrames(sample, hop, frame):
    print(np.size(sample, 0))
    sliceNum = np.floor(np.size(sample, 0)-frame)/hop
    roundedIndexValue = (sliceNum * hop + frame).astype(np.int64)
    print(roundedIndexValue)
    sample = sample[:roundedIndexValue]
    vecFrameIndex = int(np.size(sample, 0)/hop)
    vecFrames = np.zeros((vecFrameIndex, frame))

    for index in range(sliceNum.astype(np.int64)):
        beginTime = (index)*hop
        endTime = (index)*hop + frame
        vecFrames[index, :] = sample[beginTime:endTime]
    return vecFrames, sliceNum.astype(np.int64)

def fuseFrames(y, hop):
    numFrames = np.size(y,0)
    frameSize = np.size(y,1)
    hop = hop.astype(np.int64)
    strectedOutput = np.zeros(numFrames *hop - hop + frameSize)
    timeIndex = 0
    for i in range(numFrames):
        strectedOutput[timeIndex:timeIndex+frameSize] = strectedOutput[timeIndex:timeIndex+frameSize] + y[i,:].T
        timeIndex = timeIndex + hop
    return strectedOutput
    
def pitchShift(sample, frame_size, hopA, step):
    step_size = 2**(step/12)  # scaling factor that will lengthen the signal
    hopOut = np.round(step_size*hopA )  # hopOut will be used in synthesis stage.
    wn = np.hanning(frame_size*2+1)
    wn = wn[2::2]  # downsampling hanning window.

    zeroIndex = hopA*3
    print(np.shape(sample))

    samples = np.concatenate([np.zeros((zeroIndex)), sample])
    print(np.shape(samples))
    y, numFramesInput = createFrames(samples, hopA, frame_size)
    outputY = np.zeros((numFramesInput, frame_size))
    CumulativePhase = 0
    prevPhase = 0
    for i in range(numFramesInput):
        currFrame = y[i, :]
        currFrameWindowed = np.multiply(currFrame, wn.T) / np.sqrt(frame_size/(2*hopA))
        currFrameWindowedFFT = np.fft.fft(currFrameWindowed)
        magFrame = np.abs(currFrameWindowedFFT)
        phaseFrame=np.angle(currFrameWindowedFFT)
        deltaPhi = phaseFrame - prevPhase
        prevPhase = phaseFrame
        deltaPhiPrime = deltaPhi - hopA*2 * np.pi *np.arange(0, frame_size)/frame_size  #remove wbin, bin frequency
        deltaPhiPrimeWrapped = np.mod(deltaPhiPrime+np.pi, 2*np.pi) - np.pi #to remove unwrapped energy, since it wont matter
        trueFreq = 2 * np.pi * np.arange(0, frame_size) / frame_size +  deltaPhiPrimeWrapped/hopA   #wbin /frameSize + wrappedPhi

        CumulativePhase=CumulativePhase + hopOut * trueFreq  #phaseAdjustmentforSynthesis
        magFrame = np.real(np.fft.ifft(np.multiply(magFrame, np.exp(1j*CumulativePhase))))
        outputY[i,:] = np.multiply(magFrame, wn) / np.sqrt(frame_size/(2*hopA))
    strechedOutput = fuseFrames(outputY, hopOut)

    finalPitched = np.interp( np.arange(0, np.size(strechedOutput,0)-1,step_size), np.arange(0,np.size(strechedOutput,0)),strechedOutput)
    return finalPitched

convert("TheProdigy-Omen.mp3", "firstFile.wav")

sample_rate, sample=wav.read("firstFile.wav")
print(type(sample[0][0]))
leftChannel=sample[:, 0]
rightChannel=sample[:, 1]
averageChannel=(leftChannel + rightChannel)/2
pitchedAudio  = pitchShift(averageChannel, 1024, 256, 2)
time = 10
x_axis = np.linspace(0, time, time*sample_rate, endpoint=False)
plt.plot(x_axis,pitchedAudio[:time*sample_rate])
plt.show()
pitchedAudio = np.asarray(pitchedAudio, dtype=np.int16)
wav.write('pitchedAudio.wav', sample_rate,pitchedAudio[:])