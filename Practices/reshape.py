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



# Reshape method()
# Step 1: Create an array of numbers from 1 to 36 (37 excluded)
# Step 2: Reshape it into a 2D array with 6 rows and 6 columns (6×6 = 36 elements)
# Step 3: Print the reshaped array

numpy_arange = np.arange(1, 37)   # Numbers from 1 to 36
numpy_arange = np.reshape(numpy_arange, (6, 6))
print(numpy_arange)

# Same code with anothe way
numpy_arange= np.arange(1, 37).reshape(6,6)
print(numpy_arange)
print(numpy_arange.size)  # Print the size of the element

