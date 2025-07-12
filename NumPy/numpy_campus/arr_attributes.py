"""NumPy arrays have several useful attributes 
that provide information about the array's structure and content."""

"""ndim – Number of Dimensions
Returns the number of axes (dimensions) of the array."""

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ndim)  # Output: 2

import numpy as np
a = np.array([[[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]]]])
print(a.ndim)  # Output: 4

# 1D Array
a1 = np.arange(10)
print(a1)
print(a1.ndim)

# 2D Array
a2 = np.arange(12, dtype=float).reshape(3,4)
print(a2)    # print the output
print(a2.ndim)   # print the number of dimension

# 3D Array
a3 = np.arange(8).reshape(2,2,2)
print(a3.ndim)


"""2. shape – Dimensions of the Array
Returns a tuple representing the dimensions (rows, columns, etc.)."""

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.shape)  # Output: (2, 3) → 2 rows, 3 columns

# 1D Array
a1 = np.arange(10)
print("Original Array",a1)
print("Shape of the array",a1.shape)

# 2D Array
a2 = np.arange(12, dtype=float).reshape(3,4)
print("Original array",a2)    # print the output
print("Shape of the array",a2.shape)   # print dimension of the array
print("Dimension of the array\n",a2)

# 3D Array
a3 = np.arange(8).reshape(2,2,2)
print(a3.shape)
print(a3)



"""3. size – Total Number of Elements
Returns the total number of elements in the array."""

import numpy as np
a = np.array([[[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]]]])
print(a.size)  # Output: 12

# 1D Array
a1 = np.arange(10)
print(a1.size)

# 2D Array
a2 = np.arange(12, dtype=float).reshape(3,4)
print("Array\n",a2)
print("Size of the array:",a2.size)   # print the size of the array

# 3D Array
a3 = np.arange(8).reshape(2,2,2)
print(a3)
print(a3.size)


""" 4. itemsize – Size of One Element (in bytes)
Tells how many bytes each element takes."""

import numpy as np
a = np.array([[[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]]]])
print(a.itemsize) 

# 1D Array
a1 = np.arange(10)
print(a1)
print(a1.itemsize)

# 2D Array
a2 = np.arange(12, dtype=float).reshape(3,4)
print(a2)   
print(a2.itemsize)  

# 3D Array
a3 = np.arange(8).reshape(2,2,2)
print(a3.itemsize)



""" 5. dtype – Data Type of Elements
Shows the data type (int, float, etc.) of the array elements. """

import numpy as np
a = np.array([[[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]]]])
print(a.dtype) 

a1 = np.arange(10)
a2 = np.arange(12, dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)




# All the attributes in one frame

a1 = np.arange(10)
a2 = np.arange(12, dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

"""ndim – Number of Dimensions
Returns the number of axes (dimensions) of the array."""
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

""" shape – Dimensions of the Array
Returns a tuple representing the dimensions (rows, columns, etc.)."""
print(a1.shape)
print(a2.shape)
print(a3.shape)

"""size – Total Number of Elements
Returns the total number of elements in the array."""
print(a1.size)
print(a2.size)
print(a3.size)

"""itemsize – Size of One Element (in bytes)
Tells how many bytes each element takes."""
print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

"""dtype – Data Type of Elements
Shows the data type (int, float, etc.) of the array elements."""
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

""". nbytes – Total Bytes Consumed
Total memory consumed by the entire array (size * itemsize)."""
print(a1.nbytes)
print(a2.nbytes)
print(a3.nbytes)

"""T – Transpose of the Array
Gives the transpose of the array (rows become columns and vice versa)."""
print(a1.T)
print(a2.T)
print(a3.T)

"""data – Memory Buffer (Rarely Used)
Returns the memory location of the array data (for advanced use)."""
print(a1.data)
print(a2.data)
print(a3.data)



