import numpy as np

p = np.ones((2, 3), int)
print("The first numpy array of 1s is : ")
print(p)
print('----------------------------------')
q = 2*p
print("The second numpy array of 2 * 1s is : ")
print(q)
print('----------------------------------')
# q under p gets printed in nested format
arrayV = np.vstack((p, q))
print("The vertically stacked array is : ")
print(arrayV)
print('----------------------------------')
# q at right p gets printed in nested format
arrayH = np.hstack((p, q))
print("The horizontally stacked array is : ")
print(arrayH)
