import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\Raw Data.csv")

# ---- LOW-PASS FILTER (Gravity Estimation) ----
# rolling(window=50).mean() simply AVERAGES the last 50 samples
# This averaging is called a LOW-PASS FILTER because:
# - Slow-changing signals (gravity) survive averaging like 9.8,9.81,9.79 survives as avg is around 9.8
# - Fast-changing signals (motion spikes) cancel out like +2  -2  +2  -2  +2 cancels out to 0
# Result: a smooth signal that closely represents gravity
df["Gravity"] = df["Acceleration z (m/s^2)"].rolling(window=50,min_periods=1).mean() #low pass filter


# ---- HIGH-PASS FILTER (User Motion Extraction) ----
# Raw acceleration = gravity (slow) + motion (fast)
# By subtracting gravity, we REMOVE the slow component
# What remains is the fast-changing user motion
# This subtraction acts as a HIGH-PASS FILTER
df["user_acc"] = df["Acceleration z (m/s^2)"] - df["Gravity"]

plt.plot(df["Time (s)"], df["Acceleration z (m/s^2)"],label="Raw",color='green')
plt.plot(df["Time (s)"], df["user_acc"],label="User Movement",color='red')
plt.axhline(y=0)
plt.grid(True)
plt.legend()
plt.show()
