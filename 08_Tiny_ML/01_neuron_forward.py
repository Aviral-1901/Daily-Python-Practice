import numpy as np
import matplotlib.pyplot as plt

inputs = np.array([0.8,0.9])
weights = np.array([-1.5,1.0])

# bias = 0.0
# z = np.dot(weights,inputs) + bias

# if (z > 0):
#     output = 1
# else:
#     output = 0

# print("Weighted sum (z) value : ",z)
# print("Neuron decision value :",output)

###############################################
#now bias value is increase

# bias = 0.5
# z = np.dot(weights,inputs) + bias

# if (z > 0):
#     output = 1
# else:
#     output = 0

# print("Weighted sum (z) value : ",z)
# print("Neuron decision value :",output)



#################################################
#using sigmoid function instead of if/else block
bias = 0.5
z = np.dot(weights,inputs) + bias

activation = 1 / (1 + np.exp(-z))

print("raw sum is :",z)
print("confidence (sigmoid) :",activation)
