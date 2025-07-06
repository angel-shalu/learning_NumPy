# @ OPERATOR 
""" new_matrix = matrix_1 * matrix_2 
Returns the product of the two matrices.

In NumPy, the @ operator is used for:
Matrix Multiplication (also called dot product for 1D or 2D arrays)."""

import numpy as np

# First Array (shape 2x3)
numpy_arange = np.arange(20, 50, 5).reshape(2, 3)

# Second Array (shape 3x2 for matrix multiplication compatibility)
numpy_array = np.arange(25, 55, 5).reshape(3, 2)  # Needs shape (3,2) for matrix multiplication

print("Array 1:\n", numpy_arange)
print()
print("\nArray 2:\n", numpy_array)
print()

print("\nProduct of @ Operator (Matrix Multiplication):")
array = numpy_arange @ numpy_array  # Using @ operator (matrix multiplication)
print(array)
print()



import numpy as np
numpy_arange=np.arange(20,50,5).reshape(2,3)
numpy_array=np.array([20,50,22,7,2,72]).reshape(2,3)
print("Array :\n",numpy_arange)
print()
print("Array2 :\n",numpy_array)
print()
print("Product of @ Operator")
array=numpy_arange//numpy_array  # @ Operator
print(array)


# DOT() FUNCTION
import numpy as np
numpy_arange=np.arange(20,50,5).reshape(2,3)
numpy_array=np.array([20,50,22,7,2,72]).reshape(2,3)
print("Array :\n",numpy_arange)
print()
print("Array2 :\n",numpy_array)
print()
print("Product of the fuction dot()")
array=numpy_arange//numpy_array  # Dot() function
print(array)
