""" empty()
np.empty((shape of the array))
It creates an empty array in the certain dimension with random values which change for every call"""
 
import numpy as np
numpy_empty=np.empty((4,4))
print(numpy_empty)

numpy_empty=np.empty((4,4),dtype=int)
print(numpy_empty)
print(numpy_empty.dtype)
print(len(numpy_empty))
print(type(numpy_empty))

numpy_empty=np.empty((4,4),dtype=complex)
print(numpy_empty)

numpy_empty=np.empty((4,4),dtype=str)
print(numpy_empty)

numpy_empty=np.empty((4,4),dtype=bool)
print(numpy_empty)