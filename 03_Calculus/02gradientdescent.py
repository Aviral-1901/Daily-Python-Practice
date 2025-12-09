import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,100)
y = x**2

plt.plot(x,y,color='black')
plt.grid()

current_x = 4
current_y = current_x**2
slope = 2*current_x#slope at x = 4 [derivative of y at x=4]
plt.scatter(current_x,current_y,color='red')
plt.quiver(current_x,current_y,1,slope,angles='xy',scale_units='xy',scale=1,color='green')
#plt.quiver(start_x,start_y,step_right,step_up,.........)
plt.show()


