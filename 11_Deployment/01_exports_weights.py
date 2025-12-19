import numpy as np
import os
from dense_layer_class_help import DenseLayer


# 1. Get the folder where THIS script is running
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Join that folder with the filename
file_path = os.path.join(script_dir, "model_weights.h")

inputs_x = np.array([[0,0],[0,1],[1,0],[1,1]]) 
targets_Y = np.array([[0],[1],[1],[0]])

layer1 = DenseLayer(2, 3) 
layer2 = DenseLayer(3, 1)

for i in range(10000):
    out1 = layer1.forward(inputs_x)
    out2 = layer2.forward(out1)

    error = targets_Y - out2

    grad2 = layer2.backward(error, 0.1)
    grad1 = layer1.backward(grad2, 0.1)
    

with open(file_path, "w") as f:  #to keep .h file in the same folder where i ran it from 
    f.write("// Auto-generated Weights\n")

    f.write("float w1[2][3] = {\n") # C/C++ 2D array define garna start gareko, initializer { bata suru huncha
    for row in layer1.weights: # layer1 ko weights ko harek row ma loop
        text =  str(row.tolist()).replace('[','{').replace(']','}') #row.tolist() to convert numpy arrays to python list and make it string replacing [] with {} to format as needed for C
        f.write(text + ",\n") # C array ma harek row pachi comma chahincha
    f.write("};\n") # C array initializer close garne, final structure { {...}, {...} };

    f.write("float b1[1][3] = {\n")
    for row in layer1.biases:
        text = str(row.tolist()).replace('[', '{').replace(']', '}')
        f.write(text + ",\n")
    f.write("};\n")

    f.write("float w2[3][1] = {\n")
    for row in layer2.weights:
        text = str(row.tolist()).replace('[','{').replace(']','}')
        f.write(text + ',\n')
    f.write("};\n")

    f.write("float b2[1][1] = {\n")
    for row in layer2.biases:
        text = str(row.tolist()).replace('[','{').replace(']','}')
        f.write(text + ',\n')
    f.write("};\n")