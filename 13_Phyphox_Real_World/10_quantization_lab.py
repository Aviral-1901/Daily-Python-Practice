import numpy as np
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


def quantize_and_reconstruct(weights):
     #find the minimum and maximum value in the weights array
    min_weight = weights.min()
    max_weight = weights.max()

    #special case: if all weights are the same
    #there is no range, so we just return the original weights
    if max_weight == min_weight:
        scale = 1.0
        zero_point = 0
        int_weights = np.zeros_like(weights, dtype=np.uint8)
        dequantized_weight = weights.copy()
        return dequantized_weight

    scale = (max_weight - min_weight) / 255.0 #how much one integer step represents in float
    # Example: if min=-1 and max=1, then scale = (1 - (-1)) / 255 ≈ 0.00784

    zero_point = round(0 - min_weight / scale) #zero_point: the integer that represents float 0
    #zero_point ensures negative and positive weights are centered correctly
    int_weights = np.clip(np.round((weights / scale) + zero_point), 0, 255)
    #convert float weights to integers
    # 1. Divide by scale → how many steps
    # 2. Add zero_point → shift so 0 in float maps to correct integer
    # 3. Round to nearest integer
    # 4. Clip between 0 and 255 to stay in 8-bit range

    dequantized_weight = (int_weights - zero_point) * scale #reconstruct float weights from integers
    #to check how much accuracy we lost due to quantization
    return dequantized_weight

out1 = Layer1.forward(X[0:1])
original_prediction = Layer2.forward(out1)
print("Original Prediction:",original_prediction) #prediction before quantized weights and biases

#replace original weights and biases with reconstructed values after quantization
Layer1.weights = quantize_and_reconstruct(Layer1.weights)
Layer1.biases = quantize_and_reconstruct(Layer1.biases)
Layer2.weights = quantize_and_reconstruct(Layer2.weights)
Layer2.biases = quantize_and_reconstruct(Layer2.biases)

output1 = Layer1.forward(X[0:1])
quantized_prediction = Layer2.forward(output1)
print("Quantized Prediction:",quantized_prediction) #prediction with reconstructed weights to see accuaracy

