import numpy as np

myArr = [1, 2, 3, 4, 5, 6, 7, 8]
myArr2 = np.array(myArr * 3)  # 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 ....
print(myArr2)
print('-------------------------')
myArr3 = np.repeat(myArr, 3)  # 1 1 1 2 2 2 3 3 3 4 4 4 5 5 5 .....
print(myArr3)
