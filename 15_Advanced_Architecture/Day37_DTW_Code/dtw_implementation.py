import numpy as np

s1 = np.array([1,3])
s2 = np.array([1, 2, 3])

def dtw(s1, s2):
    n = len(s1)
    m = len(s2)
    dtw_matrix = np.full((n, m),np.inf) 

    dtw_matrix[0][0] = np.abs(s1[0] - s2[0])

    for j in range(1, m):
        dtw_matrix[0][j] = np.abs(s1[0] - s2[j]) + dtw_matrix[0][j-1]

    for i in range(1, n):
        dtw_matrix[i][0] = np.abs(s1[i] - s2[0]) + dtw_matrix[i-1][0]

    for i in range(1, n):
        for j in range(1, m):
            cost = np.abs(s1[i] - s2[j])
            min_prev = min(dtw_matrix[i-1][j], dtw_matrix[i][j-1], dtw_matrix[i-1][j-1])
            dtw_matrix[i][j] = cost + min_prev
    
    return dtw_matrix[n-1][m-1]

dtw_distance = dtw(s1,s2)
print(dtw_distance)