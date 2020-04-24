import numpy as np
# Creating a numpy array from 0 to 4 with 8 divisons.
series = np.linspace(0, 4, 9)
print(series)
print('--------------------------')
# Resize changes the shape of the original array but reshape create a new array!
series.resize((3, 3))
print(series)
print('--------------------------')
mywork = series.reshape((9,))
print(mywork)
print('--------------------------')
print(series)
