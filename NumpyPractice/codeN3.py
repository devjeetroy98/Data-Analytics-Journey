import numpy as np
# Nested List
myMatrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
# Nested Numpy Array
matrixN = np.array(myMatrix)
print("The numpy nested array is : ", matrixN)
print("--------------------------------------")
print("The dimension of the nested array is : ", matrixN.shape)

# Chaning the dimension of the nested numpy array.
matrix2 = matrixN.reshape(4, 2)
print("The new numpy nested array is : ", matrix2)
print("--------------------------------------")
print("The dimension of the new nested array is : ", matrix2.shape)
