import numpy as np 
import matplotlib.pyplot as plt 

time = np.arange(0,0.25,0.0008)
x = 1+5*np.cos(2257*np.pi*time + np.pi/4) +2*np.cos(2440*np.pi*time+3*np.pi/2)

plt.plot(time,x)

plt.title("Question 4, part c")
plt.xlabel('Time')
plt.ylabel('Function 1+5cos()+cos')

plt.show()