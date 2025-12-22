import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\Raw Data.csv")

# Apply a rolling (sliding window) average on Z-axis acceleration
# window=50 → average of current point + previous 49 points
# min_periods=1 → at the start, use whatever data is available like same data for first point, then sum of first two for second position and so on
# This reduces noise and smooths the signal
df["Z_Smooth"] = df["Acceleration z (m/s^2)"].rolling(window=50, min_periods=1).mean()
window1 = df[0:100]
print(window1.shape)
print(window1.head())

#On average, standard deviation shows how far the values away from the mean
noise_std = df["Acceleration z (m/s^2)"].std()
print(f"Sensor Noise Floor (Std Dev): {noise_std:.4f} m/s^2")

plt.figure(figsize=(15,5))
plt.plot(df["Time (s)"],df["Acceleration z (m/s^2)"],label="Raw Noise",color='green',alpha=0.6,linewidth=1)
plt.plot(df["Time (s)"],df["Z_Smooth"],color='red',linewidth=2,label="Smooth signal",linestyle='--')

#plt.xlim(0,5) #to look data upto first 5 seconds
plt.ylim(9.5,10.1) # Limit Y-axis to closely observe small variations around gravity (~9.8 m/s²)
plt.legend()
plt.grid(True)
plt.show()
