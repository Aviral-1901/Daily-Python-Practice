import numpy as np
import os
from model_layer import WakeWordModel

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "audio_model.h")

X = np.load(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day58_Training\X_train.npy")
Y = np.load(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day58_Training\Y_train.npy")

model = WakeWordModel()

out = model.conv.forward(X)
out = model.relu.forward(out)
out = model.pool.forward(out)
features = model.flat.forward(out)

print("Features shape :",features.shape)
features = features / np.max(features)
Y = Y.reshape(-1, 1)

print("Features Shape:", features.shape)
print("Weights Shape:", model.dense.weights.shape)
print("Y Shape:", Y.shape)

for i in range(10000):
    pred = model.dense.forward(features)
    error = Y - pred
    model.dense.backward(error, 0.01)
    if i% 1000 == 0:
        print(f"mean at epoch {i} is {np.mean(np.abs(error))}")


def write_3d_array(f, name, data):
    filters, rows, cols = data.shape
    f.write(f"const float {name}[{filters}][{rows}][{cols}] = {{\n")
    for flt in range(filters):
        f.write("  {\n")
        for row in range(rows):
            f.write("    {")
            text = str(data[flt][row].tolist()).replace('[', '').replace(']', '')
            f.write(text)
            f.write("},\n")
        f.write("  },\n")
    f.write("};\n")

def write_dense(file, name, data):
    file.write(f"const float {name} [{data.shape[0]}][{data.shape[1]}] = {{\n")
    for row in data:
        text =  str(row.tolist()).replace('[','{').replace(']','}') 
        file.write(text + ",\n")
    file.write("};\n")

with open(file_path,"w") as f:
    f.write(f"#ifndef AUDIO_MODEL_H\n")
    f.write(f"#define AUDIO_MODEL_H\n")
    write_3d_array(f, "conv_weights", model.conv.weights)
    write_dense(f, "dense_weights", model.dense.weights)
    write_dense(f, "dense_biases", model.dense.biases)
    f.write("#endif")