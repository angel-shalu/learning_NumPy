# ZEROS METHOD
# zeros()
# np.zeros((shape of the array))

import numpy as np
numpy_array = np.zeros(3)   #crate 1D arrayof shape 3
print(numpy_array)

# Create a 2D array (matrix) of shape (3, 4) filled with zeros (default dtype=float)
numpy_zeros= np.zeros((3, 4))
print(numpy_zeros)       # Print the array
print(type(numpy_zeros))   # Print the type of the array
print(numpy_zeros.dtype)    # Print the data type of elements inside the array


# Create a 2D numpy array of shape (3, 4) filled with zeros.
# dtype=int → means all numbers will be integers (0)
numpy_zeros= np.zeros((3, 4),dtype=int)
print(numpy_zeros)
numpy_zeros= np.zeros((3, 4),dtype=complex)
print(numpy_zeros)
numpy_zeros= np.zeros((3, 4),dtype=bool)
print(numpy_zeros)
numpy_zeros= np.zeros((3, 4),dtype=str)
print(numpy_zeros)
