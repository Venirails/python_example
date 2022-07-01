import numpy as np


array_list = [1,2,3,4,5,6]
array_tuple= (1,2,3,4,5,6)
array = np.array(array_list)
array = np.array(array_tuple)
print(array[0] + array[1])

matrix_1 = np.array([[1,0,0], [0,1,0], [0,0,1]])
print(type(matrix_1))
print(matrix_1[0,1])
matrix_2 = np.array([[1,0,0], [0,1,0], [0,0,1]])

print(np.dot(matrix_1, matrix_2))
print(np.linalg.inv(matrix_1))