import numpy as np
import matplotlib.pyplot as plt

z = 3+4j
print(z)

x = z.real
y = z.imag
print(f"The real part is {x} and the imaginary part is {y}")

plt.quiver(0,0,x,y,angles='xy',scale_units='xy',scale=1)
plt.xlim(0,5)
plt.ylim(0,5)
plt.xlabel("real")
plt.ylabel("imaginary")
plt.grid()
plt.show()