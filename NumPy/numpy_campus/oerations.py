"""Scalar Array Operations in NumPy
Scalar operations mean performing arithmetic between a NumPy array and a single number (called a scalar). 
NumPy automatically broadcasts the scalar to each element in the array."""

import numpy as np
a = np.array([10, 20, 30])

print("Original:", a)
print("a + 5:", a + 5)
print("a * 2:", a * 2)
print("a / 10:", a / 10)
print("a ** 2:", a ** 2)
print("a // 5:", a // 5)
print("a % 5:", a % 5)


"""Vector Operations in NumPy
Vector operations in NumPy are element-wise operations between two arrays (vectors) of the same shape."""

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a + b =", a + b)
print("a * b =", a * b)
print("Dot product:", np.dot(a, b))


# Universal functions
print("Square root:", np.sqrt(a))
print("Exponential:", np.exp(a))
print("Sine:", np.sin(a))
print("Logarithm:", np.log(a))