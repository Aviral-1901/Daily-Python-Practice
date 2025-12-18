import numpy as np
from dense_layer import DenseLayer

inputs_x = np.array([[0,0],[0,1],[1,0],[1,1]]) #vaneko input with 4 samples and 2 features
targets_Y = np.array([[0],[1],[1],[0]])

layer1 = DenseLayer(2, 3) 
layer2 = DenseLayer(3, 1)

for i in range(10000):
    out1 = layer1.forward(inputs_x)
    out2 = layer2.forward(out1)

    error = targets_Y - out2

    grad2 = layer2.backward(error, 0.1)
    grad1 = layer1.backward(grad2, 0.1)

print("Final Output is :",out2)