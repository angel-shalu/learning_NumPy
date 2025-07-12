"""1.Using array()  
# Creates an array from a Python list or tuple."""

import numpy as np
a = np.array([1, 2, 3])
print(a)  # [1 2 3]


""" 2. Zeros and Ones
zeros(shape) – Creates an array filled with 0s.
ones(shape) – Creates an array filled with 1s."""
import numpy as np
b = np.zeros(3)         # [0. 0. 0.]
print(b)

c = np.ones((2, 2))     # [[1. 1.]
print(c)                #  [1. 1.]]


""" 3. full(shape, value)
Creates an array filled with a specific value."""
# 2 rows and 3 column of same elements

d = np.full((2, 3), 5)      # [[5 5 5]
print(d)                    #  [5 5 5]]


""" 4. eye(n) or identity(n)
Creates an identity matrix."""

e = np.eye(3)        # 3x3 identity matrix
print(e)

import numpy as np
e = np.eye(3)               # default dtype: float
print(e)
e_int = np.eye(3, dtype=int)  # identity matrix with integer type
print(e_int)



"""5. arange(start, stop, step)
Creates an array with regularly spaced values (like Python range)."""

# start stop step
numpy_array = np.arange(0, 10, 2)  # [0 2 4 6 8]
print(numpy_array)

# start and stop
numpy_array = np.arange(0, 10)  # [0 1 2 3 4 5 6 7 8 9]
print(numpy_array)


""" 6. linspace(start, stop, num)
Creates an array of evenly spaced values between start and stop."""

arr = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.  ]
print(arr)


"""7. logspace(start, stop, num)
Creates an array with logarithmically spaced values."""

arr = np.logspace(1, 3, 3)  # [  10.  100. 1000.]
print(arr)


"""8. random module (for random arrays)
rand(shape) – Uniform distribution [0, 1)
randn(shape) – Standard normal distribution
randint(low, high, shape) – Random integers"""

arr =np.random.rand(2, 3)      # Random floats [0,1)
print(arr)
a = np.random.randn(2, 2)     # Random normal
print(a)
b = np.random.randint(0, 10, (2, 2))  # [[1 7]
print(b)                                #  [4 9]]


""" 9. empty(shape)
Creates an uninitialized array (with random values present in memory)."""
a = np.empty((2, 2))  # May contain garbage values
print(a)


""" 10. copy()
Creates a new array that is a copy of an existing array."""

a = np.array([1, 2, 3])
print(a)
b = a.copy()   # copy the variable a 
print(b)
