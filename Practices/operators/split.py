#  Splitting of 1D arrays
#  np.array_split(array_name, number_of_splits)

import numpy as np

array_special_nums= np.array([77,18,2,8,14,6,28,37,9])
print('\nBefore splitting the array \n', array_special_nums)
new_array = np.array_split(array_special_nums, 3)
print('\nAfter splitting the array \n',new_array)

array_special_nums= np.array([77,18,2,8,14,6,28,37,9])
print('\nBefore splitting the array \n', array_special_nums)
new_array = np.array_split(array_special_nums, 6)
print('\nAfter splitting the array \n',new_array)




#  Splitting of 2D arrays
#  np.array_split(array_name, number_of_splits, axis=0 or 1)

import numpy as np
array_special_nums=np.array([[2,1], [2, 2], [3, 6], [13, 28], [37, 17]])
print('\nBefore splitting the array \n', array_special_nums)
new_array = np.array_split(array_special_nums, 2)
print('\nAfter splitting the array \n',new_array)



import numpy as np
# Create a NumPy array with special numbers
array_special_nums = np.array([[2, 1],[2, 2],[3, 6],[13, 28],[37, 17]])
print("\nBefore splitting the array:\n", array_special_nums)

# Split the array into 2 parts using np.array_split()
new_array = np.array_split(array_special_nums, 2)
print("\nAfter splitting the array:")
for idx, arr in enumerate(new_array, start=1):
    print(f"\nSplit {idx}:\n", arr)


import numpy as np
array_special_nums=np.array([[2,1], [2, 2], [3, 6], [13, 28], [37, 17]])
print('\nBefore splitting the array \n', array_special_nums)
# Split the array into 2 parts along columns (axis=0 → split by rows)
new_array = np.array_split(array_special_nums, 2, axis=0)
print('\nAfter splitting the array \n',new_array)


import numpy as np
array_special_nums=np.array([[2,1], [2, 2], [3, 6], [13, 28], [37, 17]])
print('\nBefore splitting the array \n', array_special_nums)
# Split the array into 2 parts along columns (axis=1 → split by columns)
new_array = np.array_split(array_special_nums, 2, axis=1)
print('\nAfter splitting the array \n',new_array)