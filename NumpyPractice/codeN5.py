import numpy as np
# Creating an array of 3 X 3 with all 1s.
p = np.ones((3, 3))
print(p)
print('------------------')
# Creating an array of 3 X 3 with all 0s.
q = np.zeros((3, 3))
print(q)
print('------------------')
# Creating an identity matrix.
r = np.eye(3)
print(r)
print('------------------')
# Creating a diagonal matrix with diagonals as -> 1 2 3
y = [1, 2, 3]
s = np.diag(y)
print(s)
print('------------------')
