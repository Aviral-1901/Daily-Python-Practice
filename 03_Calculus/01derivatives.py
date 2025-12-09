"""
Day 03: Calculus - The Derivative
File: 03_derivatives.py
Goal: Visualize how the Derivative acts as a 'Sensor of Change'.
"""
import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,10,100)
temp = np.sin(time)
speed = np.gradient(temp)

plt.figure()
plt.subplot(2,1,1)
plt.plot(time,temp,color='red')
plt.title("Temperature")
plt.xlabel("time")
plt.ylabel("temp")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(time,speed,color='blue')
plt.title("Change Rate (Derivative)")
plt.xlabel("time")
plt.ylabel("speed")
plt.grid(True)

plt.show()