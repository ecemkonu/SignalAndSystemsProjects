import numpy as np 
import matplotlib.pyplot as plt 

time = np.arange(0,3*np.pi,0.01)
x = np.exp(1.j*np.pi*time)

plt.plot(time,x)

plt.title("Question 4, part 2")
plt.xlabel('Time')
plt.ylabel('Function e^(j*pi*t)')

plt.show()