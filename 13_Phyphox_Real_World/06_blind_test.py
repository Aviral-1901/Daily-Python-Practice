import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dense_layer_class import DenseLayer

def process_file(filename):
    df = pd.read_csv(filename)
    time_diff = df["Time (s)"].diff().mean()  
    frequency = 1 / time_diff 

    print(f"Detected Frequency for {filename}: {frequency:.2f} Hz")
    seconds_to_cut = 1 
    rows_to_cut = int(seconds_to_cut * frequency)
    if len(df) > (rows_to_cut * 2):
        df = df.iloc[rows_to_cut : -rows_to_cut] 
    else:
        print("ERROR: File is too short to cut 10 seconds!")
    df["gravity"] = df["Acceleration z (m/s^2)"].rolling(window=50,min_periods=1).mean()
    df["user_acc"] = df["Acceleration z (m/s^2)"] - df["gravity"]

    clean_data = np.array(df["user_acc"])
    window_size = 50
    stride = 10
    x = []

    for i in range(0, len(clean_data)-window_size, stride):
        window = clean_data[i:i+window_size]
        x.append(window)

    x = np.array(x)
    x /= 20.0 
    return x

X = np.load( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\X_train.npy")
Y = np.load( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\Y_train.npy")

Layer1 = DenseLayer(50,10)
Layer2 = DenseLayer(10,1)

#05_train_walk jhai train gareko today also 
for i in range(2000):
    out1 = Layer1.forward(X)
    out2 = Layer2.forward(out1)

    error = Y - out2

    grad2 = Layer2.backward(error, 0.001)
    grad1 = Layer1.backward(grad2, 0.001)

#loop complete = training complete now neural network have adjusted its weights and bias to differentiate sit and walk

X_test = process_file( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\Test Neuron.csv")
#X-test now became the input and with trained weights and bias we try to predict the output
hidden_output = Layer1.forward(X_test)
final_prediction = Layer2.forward(hidden_output)

plt.figure(figsize=(10,4))
plt.plot(final_prediction, label="AI confidence", color='blue')
plt.axhline(y=0.5, color='red', linestyle='--')
plt.title("Blind Test Results")
plt.xlabel("Window Number")
plt.ylabel("Probability (Walk=1)")
plt.legend()
plt.grid(True)
plt.show()