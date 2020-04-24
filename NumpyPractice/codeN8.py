import numpy as np
x = [1, 2, 3]
arX = np.array(x)
arY = np.array(x)
z = arX.dot(arY)
print("The dot product of [1 2 3] with itself is : ", z)

myArray = np.arange(0, 20, 2)
print(myArray)
print('---------------------------------')
matOri = myArray.reshape(2, 5)
print(matOri)
print('---------------------------------')
# Finding Transpose of a Matrix
matTrans = matOri.T
print(matTrans)
# Checking type of Numpy Array
print(matTrans.dtype)
# Changing data type to float
z = matTrans.astype('f')
print(z)
print(z.dtype)
