import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,1,1000)

frequency = 5
signal = np.sin(2 * np.pi * frequency * time)

frequency_fault = 50
signal_fault = 0.3*np.sin(2 * np.pi * frequency_fault * time)

noise = np.random.normal(0,0.2,1000)
combined_signal = signal + signal_fault + noise

##############################################
cleaned_signal = combined_signal.copy()
cleaned_signal[cleaned_signal<0.8] = 0



plt.figure(figsize=(10,4))
plt.plot(time,combined_signal)

plt.xlabel("time")
plt.ylabel("Amplitude")

plt.show()

####################################################
plt.figure(figsize=(10,4))
plt.plot(time,cleaned_signal,color='green',label='Filtered Signal')
plt.axhline(y=0.8,color='red',linestyle='--',label='Threshold 0.8')
plt.title("After thresholding peak isolation")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.legend()
plt.show()