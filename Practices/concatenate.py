#  concatenate()
#  np.concatenate((array_one, array_two,....), axis=0 or 1)

import numpy as np

# Create first NumPy array with values from 1 to 9 (3x3 matrix)
numpy_array_one = np.arange(1, 10).reshape(3, 3)
print("Array One:\n", numpy_array_one)

# Create second NumPy array with values from 11 to 19 (3x3 matrix)
numpy_array_two = np.arange(11, 20).reshape(3, 3)
print("\nArray Two:\n", numpy_array_two)

# Concatenate arrays horizontally (axis=1 → columns)
new_array_one = np.concatenate((numpy_array_one, numpy_array_two), axis=1)
print("\nThis is the array obtained by concatenating along axis=1 (columns):\n", new_array_one)

# Concatenate arrays vertically (axis=0 → rows)
new_array_two = np.concatenate((numpy_array_one, numpy_array_two), axis=0)
print("\nThis is the array obtained by concatenating along axis=0 (rows):\n", new_array_two)



x=np.array([[0.577,1.618], [2.718, 3.14]])
y=np.array([[6,28], [37, 1729]])
z = np.concatenate((x,y), axis = 1)
print('\nThis is the new array yielded by addinginto the row\n', z)
z = np.concatenate((x,y), axis = 0)
print('\nThis is the new array yielded by adding intothe column\n', z)