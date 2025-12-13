import numpy as np
import matplotlib.pyplot as plt

n = 1000
t = 1.0/ 800     #sampling rate

x = np.linspace(0.0,n*t, n, endpoint=False)

time = np.linspace(0,n*t,n,endpoint=False)

frequency = 5
signal_motor = np.sin(2 * np.pi * frequency * time)

frequency_fault = 50
signal_fault = 0.3*np.sin(2 * np.pi * frequency_fault * time)

noise = np.random.normal(0,0.2,1000)
y = signal_motor + signal_fault + noise

yf = np.fft.fft(y)   #gives the value for the given signal of its constituent complex numbers represnting magnitude and direction
xf = np.fft.fftfreq(n,t) #gives x-axis means from our sampling it gives equally divided spacing of frequencies
print("yf is : ",yf)
print("xf is ,",xf)

plt.plot(xf[:n//2], 2.0/n*np.abs(yf[:n//2]))  #n//2 garesi hamle negative part hatainxa
plt.grid()                                  #y wala 2* garinxa kinaki magnitude equally divided into + and - parts so - ma hateko lai retain garna
plt.show()







