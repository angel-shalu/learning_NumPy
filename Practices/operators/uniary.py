"""Unary operations are operations that operate on a single operand (i.e., one array).
They perform element-wise operations such as:

Negation
Square root
Absolute value
Reciprocal
Rounding, Ceiling, Floor, etc."""


import numpy as np

# Create a NumPy array
arr = np.array([-9, -4, 0, 4, 9])
print("Original Array:", arr)

# 1. Negation (changes sign)
negated = np.negative(arr)
print("\nNegated Array:", negated)


# 2. Absolute Value (makes all elements positive)
abs_val = np.abs(arr)
print("Absolute Value Array:", abs_val)
print()


# 3. Square Root (works only with non-negative numbers)
# 	Calculates the square root of each element
arr = np.array([9,4,0,4,9])
print("Original Array:",arr)
sqrt_val = np.sqrt(arr)
print("Square Root of Array:", sqrt_val)
# If you want integer square roots (by rounding down)
sqrt_int = np.sqrt(arr).astype(int)
print("Square Root (as int by truncation):", sqrt_int)



# 4. Reciprocal (1/x) → You should avoid division by zero!
import numpy as np
reciprocal_arr = np.reciprocal(np.where(arr != 0, arr, 1))  # Avoid division by zero
print("Reciprocal (avoiding zero):", reciprocal_arr)


# 5. Floor (round down) -----	Rounds down (toward minus infinity)
import numpy as np
floor_arr = np.floor(sqrt_val)
print("Floor of Square Root Array:", floor_arr)


# 6. Ceil (round up)-----	Rounds up (toward positive infinity)
import numpy as np
ceil_arr = np.ceil(sqrt_val)
print("Ceil of Square Root Array:", ceil_arr)


# 7. Round (round to nearest integer)------	Rounds each element to the nearest integer
import numpy as np
round_arr = np.round(sqrt_val)
print("Rounded Square Root Array:", round_arr)








import numpy as np
numpy_array =np.arange(1,25).reshape(4, 6)
print(numpy_array)
print(f'The minimum element of the certain array is {numpy_array.min()}.')
print(f'The maximum element of the certain array is {numpy_array.max()}.')
print(f'The sum of the elements of the array is {numpy_array.sum()}.')
print(f'The mean of the elements of the array is{numpy_array.mean()}.')
print(f'The standard deviation of the elements of the array is {numpy_array.std()}.')
print(f'The variance of the elements of the array is {numpy_array.var()}.')
print(f'The length of the elements of the array is {len(numpy_array)}.')
print(f'The shape of the array is {numpy_array.shape}.')
print(f'The dtype of the array is {numpy_array.dtype}.')
print(f'The type of the array is {type(numpy_array)}.')
print(f'The minimum numbers of every row are {numpy_array.min(axis = 1)}.') # axis = 1 denotesthe row.
print(f'The maximum numbers of every row are {numpy_array.max(axis = 1)}.')
print(f'The minimum numbers of every column are {numpy_array.min(axis=0)}.') # axis = 0denotesthecolumn
print(f'The maximum numbers of every column are{numpy_array.max(axis=0)}.')
print(f'The sum of the numbers in each column are{numpy_array.sum(axis=0)}.')
print(f'The sumof the numbers in each row are {numpy_array.sum(axis=1)}.')
print(f'The meanof the numbers in each column is{numpy_array.mean(axis=0)}.')
print(f'The mean of the numbers in each row is {numpy_array.mean(axis=1)}.')
print(f'Thecumulativesumofthenumbersineachcolumnis\n{numpy_array.cumsum(axis=0)}.')
print(f'Thecumulativesumofthenumbersineachrowis\n{numpy_array.cumsum(axis=1)}.')
print(f'Thecumulativesumofthenumbersinthearrayis\n{numpy_array.cumsum()}.')
print('etc...')