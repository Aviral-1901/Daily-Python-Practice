import numpy as np
from conv_layer import ConvLayer
from relu_layer import ReLU_Layer
from max_pool import MaxPool
from flatten_layer import FlattenLayer
from dense_layer import DenseLayer
from model_layer import WakeWordModel

X = np.load(r"C:\Users\Dell\Desktop\PYTHON Daily\16_Optimization\Day61_Calibration\X_train.npy")
Y = np.load(r"C:\Users\Dell\Desktop\PYTHON Daily\16_Optimization\Day61_Calibration\Y_train.npy")
Y = Y.reshape(-1, 1)

model = WakeWordModel()
out_conv = model.conv.forward(X)
out_relu = model.relu.forward(out_conv)
out_pool = model.pool.forward(out_relu)
features = model.flat.forward(out_pool)

for i in range(10000):
    out_final = model.dense.forward(features)
    error = Y - out_final
    model.dense.backward(error, 0.01)
    
print("LayerName\tMinValue\t\tMaxValue")
print(f"ConvLayer\t{np.min(out_conv)}\t\t\t{np.max(out_conv)}")
print(f"ReLULayer\t{np.min(out_relu)}\t\t\t{np.max(out_relu)}")
print(f"PoolLayer\t{np.min(out_pool)}\t\t\t{np.max(out_pool)}")
print(f"DenseLayer\t{np.min(out_final)}\t\t\t{np.max(out_final)}")

range_conv_weight = np.max(model.conv.weights) - np.min(model.conv.weights)
CONV_WEIGHT_SCALE = range_conv_weight / 255
CONV_WEIGHT_ZEROPOINT = np.round(0.0 - (np.min(model.conv.weights) / CONV_WEIGHT_SCALE))
range_conv_out = np.max(out_conv) - np.min(out_conv)
CONV_OUT_SCALE = range_conv_out / 255
CONV_OUT_ZEROPOINT = np.round(0.0 - (np.min(out_conv) / CONV_OUT_SCALE))

range_input = np.max(X) - np.min(X)
INPUT_SCALE = range_input / 255
INPUT_ZERO_POINT = np.round(0.0 - (np.min(X) / INPUT_SCALE))

print("Convweight scale :",CONV_WEIGHT_SCALE)
print("Convweight zeropoint :",CONV_WEIGHT_ZEROPOINT)
print("Convout scale :",CONV_OUT_SCALE)
print("convout zero point:",CONV_OUT_ZEROPOINT)
print("input scale :",INPUT_SCALE)
print("input zeropoint :",INPUT_ZERO_POINT)