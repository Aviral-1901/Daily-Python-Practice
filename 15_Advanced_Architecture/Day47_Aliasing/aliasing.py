import numpy as np
import matplotlib.pyplot as plt

fs = 100
t = np.linspace(0, 1, 100, endpoint=False)
signal = np.sin(2 * np.pi * 90 * t) #90hz signal

spectrum = np.fft.fft(signal) #gives 100 complex numbers as i gave it 100 values
freqs = np.fft.fftfreq(len(signal), 1/fs) #labels frequency to the given complex numbers

index = np.argmax(np.abs(spectrum)) #gives the index at which magnitude is highest
print("The max spectrum is at",freqs[index])

plt.plot(np.abs(spectrum[:50]))
plt.show()