import numpy as np
import matplotlib.pyplot as plt

z = 3+4j
z_rotated = z*1j
print("the rotated value is ",z_rotated)
plt.quiver(0,0,z.real,z.imag,angles='xy',scale_units='xy',scale=1,color='red',label='real')
plt.quiver(0,0,z_rotated.real,z_rotated.imag,angles='xy',scale_units='xy',scale=1,color='blue',label='real')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.grid()
plt.show()