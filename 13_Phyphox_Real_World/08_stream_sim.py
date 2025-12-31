import numpy as np
import pandas as pd
import time
from collections import deque
from dense_layer_class import DenseLayer

X = np.load( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\X_train.npy")
Y = np.load( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\Y_train.npy")

Layer1 = DenseLayer(50,10)
Layer2 = DenseLayer(10,1)

for i in range(2000):
    out1 = Layer1.forward(X)
    out2 = Layer2.forward(out1)

    error = Y - out2

    grad2 = Layer2.backward(error, 0.001)
    grad1 = Layer1.backward(grad2, 0.001)

print("Neural networks ready!")

df = pd.read_csv( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\Test Neuron.csv")
df["Gravity"] = df["Acceleration z (m/s^2)"].rolling(window=50,min_periods=1).mean()
df["user_acc"] = df["Acceleration z (m/s^2)"] - df["Gravity"]

stream = df["user_acc"].values #stream ma just values basxa from user_acc column of dataframe, stream is numpy array

buffer = deque(maxlen=50)
for idx, value in enumerate(stream):  #from stream array get the index and values 
    buffer.append(value)
    if(len(buffer)==50):
        np_buffer = np.array(buffer).reshape(1, 50) /20.0 #converts buffer(deque) to numpy array then reshape to 2d array and normalize
        out1 = Layer1.forward(np_buffer)
        prediction = Layer2.forward(out1)
        val = prediction[0][0]
        if(val>0.8):
            print(f"Sample {idx}: [||||||||||] WALKING ({val})")
        else:
            print(f"Sample {idx}: [........ ] Sitting ({val})")

        time.sleep(0.005)