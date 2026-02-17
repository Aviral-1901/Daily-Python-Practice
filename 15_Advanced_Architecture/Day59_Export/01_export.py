import numpy as np
import os
from model_layer import WakeWordModel

np.random.seed(42)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "audio_model_int.h")

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
    f.write(f"const uint8_t {name}[{filters}][{rows}][{cols}] = {{\n")
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
    file.write(f"const uint8_t {name} [{data.shape[0]}][{data.shape[1]}] = {{\n")
    for row in data:
        text =  str(row.tolist()).replace('[','{').replace(']','}') 
        file.write(text + ",\n")
    file.write("};\n")

# S = 0.00281, Z = 115 for cnn got from day 61 and revisted this again for int weights export
q_conv_weights = np.round(model.conv.weights / 0.00281) + 115
q_conv_weights = np.clip(q_conv_weights, 0, 255).astype(np.uint8)

# S = 0.02303, Z = 130 for dense layer
q_dense_weights = np.round(model.dense.weights / 0.02303) + 130
q_dense_weights = np.clip(q_dense_weights, 0, 255).astype(np.uint8)

# Effective Scale for the Bias (Input_Scale * Weight_Scale)
EFFECTIVE_SCALE = 0.04978 * 0.02303 
q_dense_bias = np.round(model.dense.biases / EFFECTIVE_SCALE).astype(np.int32)


with open(file_path,"w") as f:
    f.write(f"#ifndef AUDIO_MODEL_H\n")
    f.write(f"#define AUDIO_MODEL_H\n")
    f.write(f"#include <inttypes.h>\n")
    write_3d_array(f, "conv_weights", q_conv_weights)
    write_dense(f, "dense_weights", q_dense_weights)
    f.write(f"const int32_t dense_bias_int = {q_dense_bias[0][0]};\n\n")
    f.write("#endif")