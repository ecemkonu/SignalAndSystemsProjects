import numpy as np 
import matplotlib.pyplot as plt
arr1 =np.array([0,0,0,0,1,1,1,1,0])
convArr = np.convolve(arr1,arr1)

plt.title("First degree convolution of first a&b values f*f")
plt.plot(convArr)
plt.show()

plt.title("Second degree convolution of first a&b values f*f*f")
conv2Arr = np.convolve(arr1,convArr)
plt.plot(conv2Arr)
plt.show()

plt.title("Third degree convolution of first a&b values f*f*f*f")
conv3Arr = np.convolve(arr1,conv2Arr)
plt.plot(conv3Arr)
plt.show()

arr2 = np.array([0,1,1,1,0,0])
convArr2 = np.convolve(arr2,arr2)

plt.title("First degree convolution of second a&b values f*f")
plt.plot(convArr2)
plt.show()


plt.title("Second degree convolution of second a&b values f*f*f")
conv2Arr2 = np.convolve(convArr2,arr2)
plt.plot(conv2Arr2)
plt.show()

plt.title("Third degree convolution of second a&b values f*f*f*f")
conv3Arr2 = np.convolve(conv2Arr2,arr2)
plt.plot(conv3Arr2)
plt.show()

arr3 = np.array([0,1,1,1,1,1,0])
inarr3 = np.arange(-3,2*np.size(arr3)-4)
convArr3 = np.convolve(arr3,arr3)
plt.title("First degree convolution of third a&b values f*f")
plt.plot(inarr3, convArr3)
plt.show()


plt.title("Second degree convolution of third a&b values f*f*f")
conv2Arr3 = np.convolve(convArr3,arr3)
plt.plot(conv2Arr3)
plt.show()

plt.title("Third degree convolution of third a&b values f*f*f*f")
conv3Arr3 = np.convolve(conv2Arr3,arr3)
plt.plot(conv3Arr3)
plt.show()

arr4 = np.ones(42)
arr4[0] = 0
arr4[41] = 0
plt.title("First degree convolution of fourth a&b values f*f")
convArr4 = np.convolve(arr4,arr4)
plt.plot(convArr4)
plt.show()

plt.title("Second degree convolution of fourth a&b values f*f*f")
conv2Arr4 = np.convolve(convArr4,arr4)
plt.plot(conv2Arr4)
plt.show()

plt.title("Third degree convolution of fourth a&b values f*f*f*f")
conv3Arr4 = np.convolve(conv2Arr4,arr4)
plt.plot(conv3Arr4)
plt.show()