import numpy as np
import matplotlib.pyplot as plt



#task 1 and 2 vector rotation and identity matrix
vecA = np.array([2,0])
MatrixM = np.array([[0,-1],[1,0]])

#identity matrix used for debugging purpose
I = np.eye(2)

v_rotated = MatrixM @ vecA
v_output = I @ vecA
print("the value of rotated vector is :",v_rotated)

print("the value is : ",v_output)
plt.quiver(0,0,2,0,angles='xy',scale_units='xy',scale=1,color='red')
#plt.quiver(0,0,v_rotated[0],v_rotated[1],angles='xy',scale_units='xy',scale=1,color='blue')
plt.quiver(0,0,v_output[0],v_output[1],angles='xy',scale_units='xy',scale=1,color='blue')


plt.xlim(-5,9)
plt.ylim(-5,9)
plt.grid()
plt.show()



#task 3 inverse matrix
original_vector = np.array([3,2])
scramble_matrix = np.array([[2,1],[1,3]])
encrypted_matrix = scramble_matrix @ original_vector

print("the scrambled matrix multiplication is : ",encrypted_matrix)

inv_matrix = np.linalg.inv(scramble_matrix)
decrypted_vector = inv_matrix @ encrypted_matrix
print('the decrypted vector is : ',decrypted_vector)



#task 4 eigen vectors
matrixM = np.array([[1,1],[0,1]])
vectorV = np.array([1,0])
v_new = matrixM @ vectorV
print("the v_new vector is ",v_new)
plt.quiver(0, 0, 1, 0, angles='xy', scale_units='xy',scale=1,color='red')
plt.quiver(0, 0, v_new[0], v_new[1], angles='xy', scale_units='xy',scale=1, color='blue')

v2 = np.array([0,1])
v_new2 = matrixM @ v2
print('the next vector v2 is : ',v_new2)
plt.quiver(0,0,v_new2[0],v_new2[1],angles='xy', scale_units='xy',scale=1, color='green')

plt.xlim(0,10)
plt.ylim(0,10)
plt.grid()
plt.show()