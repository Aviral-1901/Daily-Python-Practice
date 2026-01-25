import numpy as np
import matplotlib.pyplot as plt

signalA = np.array([1,1,1,1,0])
signalB = np.array([1,1,1,1,1])

window = np.hamming(5)
print(window)

windowed_signal = signalA * window
fft_output = np.fft.fft(windowed_signal)

print("magnitudes :",np.abs(fft_output))

plt.bar(range(5), np.abs(fft_output))
plt.show()



