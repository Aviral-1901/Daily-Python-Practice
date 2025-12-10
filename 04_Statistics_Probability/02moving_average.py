import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,10,100)
clean = np.sin(time)

noise = np.random.normal(0,0.5,100)

noisy_signal = clean + noise
filtered_signal = np.zeros(100)

for i in range(1,100):
    average_value = (noisy_signal[i] + noisy_signal[i-1]) / 2
    filtered_signal[i] = average_value

plt.plot(noisy_signal, color='lightgreen',label='Noisy')
plt.plot(filtered_signal, color='red',label='Filtered')
plt.show()

