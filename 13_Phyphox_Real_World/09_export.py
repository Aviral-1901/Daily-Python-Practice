import numpy as np
import pandas as pd
import os
from dense_layer_class import DenseLayer

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "model_weights.h")

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


def export_to_cpp(f, variable_name, data):
    f.write(f"const float {variable_name} [{data.shape[0]}] [{data.shape[1]}] = {{\n")
    for row in data:
        text =  str(row.tolist()).replace('[','{').replace(']','}') 
        f.write(text + ",\n")
    f.write("};\n")


with open(file_path, "w") as f:  #to keep .h file in the same folder where i ran it from 
    f.write("#ifndef MODEL_WEIGHTS_H\n")
    f.write("#define MODEL_WEIGHTS_H\n")
    export_to_cpp(f, 'w1', Layer1.weights)
    export_to_cpp(f, 'b1', Layer1.biases)
    export_to_cpp(f, 'w2', Layer2.weights)
    export_to_cpp(f, 'b2', Layer2.biases)
    f.write("#endif\n")

