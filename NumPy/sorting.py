import numpy as np

a = np.array([3, 1, 4, 2])

# Sort the array (returns a new sorted array)
sorted_arr = np.sort(a)
print("Sorted array:", sorted_arr)   # [1 2 3 4]

# Argsort (returns indices that would sort the array)
indices = np.argsort(a)
print("Indices to sort a:", indices)  # [1 3 0 2]

# Where condition is True (returns index positions where a > 2)
where_result = np.where(a > 2)
print("Where a > 2:", where_result)   # (array([0, 2]),)
