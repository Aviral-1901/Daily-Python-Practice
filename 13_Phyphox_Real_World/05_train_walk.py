import numpy as np
from dense_layer_class import DenseLayer

#x is training input data
#each row is one motion window (50 time samples)
X = np.load( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\X_train.npy")

#y labeling ho for x like 0 for sit and 1 for walk
Y = np.load( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\Y_train.npy")

print("The shape of x is",X.shape)

layer1 = DenseLayer(50,10) #hidden layer that has 10 neurons and takes 50 data
layer2 = DenseLayer(10,1) #final layer that has 1 neuron and takes output of 10 hidden layer neurons

for i in range(2000):
    out1 = layer1.forward(X)
    out2 = layer2.forward(out1)

    error = Y - out2

    grad2 = layer2.backward(error,0.001)
    grad1 = layer1.backward(grad2,0.001)

    if(i % 100 ==0):
        mean_error = np.mean(np.abs(error))
        print(f"Epoch {i}: Mean Error = {mean_error:.4f}")
