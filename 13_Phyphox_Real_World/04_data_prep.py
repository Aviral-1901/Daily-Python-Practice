import numpy as np
import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__)) #get the directory where this Python file is located

def process_file(filename):
    df = pd.read_csv(filename)
    time_diff = df["Time (s)"].diff().mean()  #calculates average time difference between samples
    #this helps detect the sampling frequency automatically
    frequency = 1 / time_diff #sampling frequency
    print(f"Detected Frequency for {filename}: {frequency:.2f} Hz")

    # 3. Calculate how many rows equal 10 seconds (The Safety Buffer)
    seconds_to_cut = 13 #number of seconds to remove from start and end (noise / setup time)
    rows_to_cut = int(seconds_to_cut * frequency)
    #Trim
    # We check if the file is big enough first!
    if len(df) > (rows_to_cut * 2):
        df = df.iloc[rows_to_cut : -rows_to_cut] #trims the noisy beginning and ending of the signal
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
    x /= 20.0 #normalizes values so neural network trains faster and more stably
    # Accelerometer values are roughly within ±20 m/s²
    return x

x_sit = process_file( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\sit.csv")
x_walk = process_file( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\walk.csv")

print("x_sit shape is",x_sit.shape)
print("x_walk shape is",x_walk.shape)

#Create labels
# 0 -> sitting
# 1 -> walking
y_sit = np.zeros((x_sit.shape[0],1))
y_walk = np.ones((x_walk.shape[0],1))

#combine sit and walk data into one dataset
X_final = np.concatenate((x_sit,x_walk), axis=0)
Y_final = np.concatenate((y_sit,y_walk), axis=0)

#data order random banauna ko lagi indices shuffle gareko
indices = np.arange(X_final.shape[0]) # Create list [0, 1, 2... 1572]
np.random.shuffle(indices) # Shuffle list [5, 100, 2...]

X_shuffled = X_final[indices]
Y_shuffled = Y_final[indices]

print("X final shape is",X_final.shape)
print("Y final shape is",Y_final.shape)

# Save the X (Inputs) matrix to a file named 'X_train.npy'
np.save(os.path.join(script_dir, "X_train.npy"), X_shuffled)

# Save the Y (Labels) matrix to a file named 'Y_train.npy'
np.save(os.path.join(script_dir, "Y_train.npy"), Y_shuffled)

