import numpy as np
import matplotlib.pyplot as plt

inputs = np.array([0.8 , 0.9])

weights = np.array([[-1.5,1.0],[-0.1,2.0]])

bias = np.array([0.5, 0.1])

z_vector = weights @ inputs + bias

activation = 1 / (1 + np.exp(-z_vector))

print("The raw sum is :",z_vector)
print("Sigmoid value is :",activation)
