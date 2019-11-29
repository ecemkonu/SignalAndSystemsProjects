import numpy as np 
import matplotlib.pyplot as plt 

time = np.arange(0,2*np.pi,0.01)
x = np.cos(2*np.pi*time)**2

plt.plot(time,x)

plt.title("Question 4, part a")
plt.xlabel('Time')
plt.ylabel('Function cos^2(2*pi*t)')

plt.show()