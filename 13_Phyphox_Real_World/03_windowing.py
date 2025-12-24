import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\Raw Data.csv")
df["Gravity"] = df["Acceleration z (m/s^2)"].rolling(window=50,min_periods=1).mean() #low pass filter
df["user_acc"] = df["Acceleration z (m/s^2)"] - df["Gravity"] #high pass filter

clean_data = np.array(df["user_acc"]) # Convert cleaned acceleration data to NumPy array for faster processing
window_size = 50 # Window size = number of samples per motion segment
stride = 10 # Stride = how many samples to move forward before taking the next window
            # Smaller stride = more overlap between windows

x = []  # List to store all motion windows

# Cut the long signal into overlapping windows of 50 samples
# window 1 : samples 0-49, window 2 : samples 10-59 for stride = 10
for i in range(0, len(clean_data)-window_size, stride):
    window = clean_data[i:i+window_size]  # extract one time window
    x.append(window)

x = np.array(x) # Convert list of windows into NumPy array
print("Clean data shape is:",clean_data.shape)
print("Shape of input is:",x.shape)