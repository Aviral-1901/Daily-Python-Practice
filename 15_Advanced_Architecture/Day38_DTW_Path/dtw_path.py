import numpy as np
import matplotlib.pyplot as plt

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
    path = dtw_path(dtw_matrix)
    print(path)
    return dtw_matrix[n-1][m-1], dtw_matrix

def dtw_path(matrix):
    i = matrix.shape[0] - 1
    j = matrix.shape[1] - 1
    path = []
    path.append((i,j))
    while(i > 0) or (j > 0):
        if(i==0):
            j = j -1
        elif j==0:
            i = i - 1
        else:
            cost_up = matrix[i-1][j]
            cost_left = matrix[i][j-1]
            cost_diagonal = matrix[i-1][j-1]

            if cost_diagonal <= cost_left and cost_diagonal <= cost_up:
                i = i - 1
                j = j - 1
            elif cost_left <= cost_up:
                j = j - 1
            else:
                i = i - 1
        path.append((i,j))
    return path


dtw_distance, matrix = dtw(s1,s2)
print(dtw_distance)
plt.figure()
plt.plot(s1, label="Signal1", color="blue")
plt.plot(s2, label="Signal2", color="orange")
plt.legend()
plt.show()


final_path = dtw_path(matrix)
plt.figure()
plt.imshow(matrix, origin='lower', cmap='viridis')
plt.colorbar()

row = []
cols = []

for p in final_path:
    row.append(p[0])
    cols.append(p[1])

plt.plot(cols, row, color='white', linewidth=2, label='optimal_path')
plt.legend()
plt.title(f"DTW matrix (cost : {dtw_distance})")
plt.show()
