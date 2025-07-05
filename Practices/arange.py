#  arange()
#  np.arange(start, end, step)


import numpy as np

# print the numbers from 0 to 49
numpy_array = np.arange(0, 50)
print(numpy_array)

# print the numbers from 0 to 49 with step 5
numpy_array = np.arange(0, 50, 5)
print(numpy_array)           # Print the array

print(numpy_array.dtype)     # Print data type of the array
print(len(numpy_array))      # Print length of the array


# Another way same output
numpy_array= np.arange(0,100, 5, int)
print(numpy_array)
print(len(numpy_array))


# Type of arange
numpy_array=np.arange(2,37, 3)
print(numpy_array)
print(type(numpy_array))


# Arrange the array from 5 to n-1 i.e 9
numpy_array=np.arange(5,10)
print(numpy_array)


# If 1st arg is grater than 2nd argument  then Numpy simply returns an empty array:
numpy_array=np.arange(50,10)
print(numpy_array)


# If we want in decending order
numpy_array = np.arange(22, 6, -1)  # Decreasing numbers
print(numpy_array)

