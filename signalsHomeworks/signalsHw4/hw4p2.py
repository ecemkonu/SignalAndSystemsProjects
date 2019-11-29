import numpy as np 
import matplotlib.pyplot as plt
def firstAnalysis(k):
    return 1/(2*np.pi*1j*k)*(1-3*np.exp(-4j*k*np.pi/3)+2*np.exp(-1j*k*np.pi))

firstRange = np.arange(10, dtype = complex)
firstRangeCoefs = firstAnalysis(firstRange)
t = firstRange
value = np.zeros(t.shape, dtype=complex)
for i in range(10):
    firstRangeExponents= np.exp(-1/3j*firstRange*np.pi*i)
    print(firstRangeExponents)
    value[i] = np.sum(np.multiply(firstRangeExponents, firstRangeCoefs, dtype=complex),dtype = complex)

plt.plot(t,value)
plt.show()
