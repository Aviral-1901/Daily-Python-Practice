import numpy as np
import matplotlib.pyplot as plt

angles = np.linspace(0, 2*np.pi, 100)
points = np.exp(1j * angles)
plt.plot(points.real,points.imag)
plt.axis('equal')
plt.show()