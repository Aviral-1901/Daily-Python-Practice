import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def dtw(s1, s2):
    n = len(s1)
    m = len(s2)
    dtw_matrix = np.full((n, m),np.inf) 

    dtw_matrix[0][0] = np.linalg.norm(s1[0] - s2[0])

    for j in range(1, m):
        dtw_matrix[0][j] = np.linalg.norm(s1[0] - s2[j]) + dtw_matrix[0][j-1]

    for i in range(1, n):
        dtw_matrix[i][0] = np.linalg.norm(s1[i] - s2[0]) + dtw_matrix[i-1][0]

    for i in range(1, n):
        for j in range(1, m):
            cost = np.linalg.norm(s1[i] - s2[j])
            min_prev = min(dtw_matrix[i-1][j], dtw_matrix[i][j-1], dtw_matrix[i-1][j-1])
            dtw_matrix[i][j] = cost + min_prev

    return dtw_matrix[n-1][m-1]

def load_gesture(filename):
    df = pd.read_csv(filename)
    df = df.rolling(window=5, min_periods=1).mean()
    acceleration_data = df[["Acceleration x (m/s^2)","Acceleration y (m/s^2)","Acceleration z (m/s^2)"]]
    acceleration_data = acceleration_data - acceleration_data.mean(axis=0)
    acceleration_data = acceleration_data / np.abs(acceleration_data).max()
    numpy_matrix = acceleration_data.to_numpy()
    return numpy_matrix

circle = load_gesture(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day39_MultiDimensionalDTW\Circle.csv")
shape_z = load_gesture(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day39_MultiDimensionalDTW\Shape_Z.csv")
test_circle = load_gesture(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day39_MultiDimensionalDTW\Circle_Test.csv")

print("The score of circle and test_circle is",dtw(circle,test_circle))
print("The score of circle and Z is",dtw(circle,shape_z))


