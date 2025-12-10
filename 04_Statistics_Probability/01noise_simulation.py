import numpy as np
import matplotlib.pyplot as plt

sensor_readings = np.random.normal(20,2,1000)
plt.hist(sensor_readings,bins=30)

plt.show()