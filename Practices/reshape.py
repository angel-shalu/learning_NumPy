import numpy as np

# 2 reffer as rows and 4 reffer as column
numpy_array= np.array([0.577,1.618, 2.718, 3.14, 6, 28, 37, 1729]).reshape(2,4)
print(numpy_array)       
print(numpy_array.dtype)
print()

# 4 reffer as rows and 2 reffer as column
numpy_array= np.array([0.577,1.618, 2.718, 3.14, 6, 28, 37, 1729]).reshape(4,2)
print(numpy_array)
print(numpy_array.dtype)