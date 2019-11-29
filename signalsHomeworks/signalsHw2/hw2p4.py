import numpy as np
import matplotlib.pyplot as plt

def convolution(x, h):
    sizeH = np.size(h,0)
    hrev = np.zeros(h.shape)
    y = np.zeros((sizeH + np.size(x,0)-1))
    for i in range(sizeH):
        hrev[i] = h[sizeH-1-i]
    for j in range(np.size(x,0)):
        y[j:j+sizeH] +=np.multiply(x[j], hrev)
    return y

x_1 = np.array([1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,0])
x_1_range = np.arange(-10, 5)
h_1 = np.cos(np.pi/3 *(x_1_range)) 
y_1 = convolution(x_1, h_1)
plt.stem(y_1, linefmt='m-', markerfmt='co', basefmt='k-')
plt.show()

x_2 = np.array([1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1])
h_2 = np.array([0,0,0,0,-1,0,1,2,3,2,1,0,-1,0,0,0,0,0,0,0])
y_2 = convolution(x_2, h_2)
plt.stem(y_2, linefmt='m-', markerfmt='co', basefmt='k-')
plt.show()

alpha = 1.42
x_3_1st_range = np.arange(0,11, dtype = np.float64)
x_3_1st_range = (2*alpha**(x_3_1st_range+2)) *(1- alpha**(-1-x_3_1st_range))/(1-alpha**-1)
x_3_2nd_range = np.ones(2)
x_3_2nd_range *= (2 * alpha**12) *(1-alpha**-11)/(1-alpha**-1) 
x_3_3rd_range = np.arange(14,24,  dtype = np.float64)
x_3_3rd_range = (2 * alpha**12) * (1-alpha**(x_3_3rd_range-24))/(1-alpha**-1)
x_3 = np.concatenate((np.zeros(1), x_3_1st_range , x_3_2nd_range , x_3_3rd_range))
h_3_1st_range = np.arange(-1, 2)
h_3_1st_range = - h_3_1st_range + 2
h_3_2nd_range = np.arange(2,5)
h_3_2nd_range = h_3_2nd_range -4
h_3_3rd_range = np.zeros(5)
h_3_4th_range = np.arange(10,12)
h_3_4th_range = h_3_4th_range - 9
h_3_5th_range = np. arange(12,15)
h_3_5th_range = 15 - h_3_5th_range
h_3 = np.concatenate((h_3_1st_range, h_3_2nd_range, h_3_3rd_range, h_3_4th_range, h_3_5th_range))

y_3 = convolution(x_3, h_3)
plt.stem(y_3,linefmt='m-', markerfmt='co', basefmt='k-')
plt.show()


