import numpy as np
import pandas as pd

def load_gesture(filename):
    df = pd.read_csv(filename)
    df = df.rolling(window=5, min_periods=1).mean()
    acceleration_data = df[["Acceleration x (m/s^2)","Acceleration y (m/s^2)","Acceleration z (m/s^2)"]]
    acceleration_data = acceleration_data - acceleration_data.mean(axis=0)
    acceleration_data = acceleration_data / np.abs(acceleration_data).max()
    numpy_matrix = acceleration_data.to_numpy()
    return numpy_matrix

def dtw_smart(s1, s2):
    n = len(s1) #n le row haru batauxa
    m = len(s2) #m le column haru batauxa
    prev_row = np.full(m, np.inf)
    curr_row = np.full(m, np.inf)

    #first row, first element (the corner)
    prev_row[0] = np.linalg.norm(s1[0] - s2[0])

    #the top row
    for j in range(1, m):
        cost = np.linalg.norm(s1[0] - s2[j])
        prev_row[j] = cost + prev_row[j-1]

    for i in range(1, n):
        cost = np.linalg.norm(s1[i] - s2[0])
        curr_row[0] = cost + prev_row[0]  #left-most column 

        for j in range(1,m):
            cost = np.linalg.norm(s1[i] - s2[j])
            curr_row[j] = cost + min(curr_row[j-1], prev_row[j], prev_row[j-1])
            #curr[j] = local_cost + min( curr[j-1]->left, prev[j]->up, prev[j-1]-> diagonal )
        prev_row = curr_row.copy() 
    
    return curr_row[m-1]

circle = load_gesture(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day40_DTW_Optimized\Circle.csv")
shape_z = load_gesture(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day40_DTW_Optimized\Shape_Z.csv")
test_circle = load_gesture(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day40_DTW_Optimized\Circle_Test.csv")

print("The score of circle and test_circle is:",dtw_smart(circle, test_circle))
print("The score of circle and z is :",dtw_smart(circle, shape_z))