import numpy as np
a1 = np.arange(10)
a2 = np.arange(12, dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

"""1. Using astype() Method (Recommended)
This creates a new array with the desired data type."""
print(a3.dtype)
print(a3.astype(np.float32))
