# ones()
# np.ones((shape of the array))

import numpy as np
numpy_ones=np.ones(7)    #crate 1D arrayof shape 7
print(numpy_ones)

# Create a 2D array (matrix) of shape (3, 4) filled with zeros (default dtype=float)
numpy_ones= np.ones((3, 4))
print(numpy_ones)       # Print the array
print(type(numpy_ones))   # Print the type of the array
print(numpy_ones.dtype)    # Print the data type of elements inside the array


# Create a 2D numpy array of shape (3, 4) filled with zeros.
# dtype=int → means all numbers will be integers (0)
numpy_ones= np.ones((3, 4),dtype=int)
print(numpy_ones)
numpy_ones= np.ones((3, 4),dtype=complex)
print(numpy_ones)
numpy_ones= np.ones((3, 4),dtype=bool)
print(numpy_ones)
numpy_ones= np.ones((3, 4),dtype=str)
print(numpy_ones)
