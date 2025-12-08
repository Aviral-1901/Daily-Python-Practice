import numpy as np
import matplotlib.pyplot as plt



#task 1 - magnitude
robot_pos = np.array([3,4])
squared_values = robot_pos ** 2
sum_of_squares = np.sum(squared_values)
distance = np.sqrt(sum_of_squares)

print("the distance is ", distance)


#task 2 - movement
start = np.array([3,4])
movement = np.array([1,-2])
end_position = start + movement

print("the final distance is ",end_position)


#task 3 data visualizaton
plt.quiver(0, 0, 3, 4, angles='xy', scale_units='xy', scale=1, color='red')
plt.quiver(0, 0, 4, 2, angles='xy', scale_units = 'xy', scale=1, color='blue')

plt.xlim(0,6)
plt.ylim(0,6)
plt.grid()
plt.show()



#task 4 dot product
target = np.array([1,1])
vectorA = np.array([2,2])
vectorB = np.array([-2,2])
vectorC = np.array([2,0])

scoreA = np.dot(target,vectorA)
scoreB = np.dot(target,vectorB)
scoreC = np.dot(target,vectorC)

print("the scores are : ",scoreA, scoreB, scoreC)
