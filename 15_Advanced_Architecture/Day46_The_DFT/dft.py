import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 100)
wave1 = np.sin(2 * np.pi * 5 * t)
wave2 = np.sin(2 * np.pi * 20 * t)

signal = wave1 + wave2

magnitudes = []
for k in range(50):
    reference = np.cos(2 * np.pi * k * t)
    real_score = np.sum(signal * reference)
    imag_reference = np.sin(2 * np.pi * k * t)
    imag_score = np.sum(signal * imag_reference)
    magnitudes.append(np.linalg.norm([real_score, imag_score]))

plt.plot(magnitudes)
plt.show()

