"""Relational operations
Relational operations are used to compare arrays element by element.
These operations return Boolean values (True or False) based on the comparison.
 
array_name, operator,value 
numpy_array<100
"""

import numpy as np
numpy_array=np.arange(10,20,5)
print(numpy_array)
print(numpy_array<30)
print(numpy_array>30)
print(numpy_array<=30)
print(numpy_array>=30)
print(numpy_array==30)
print(numpy_array!=30)
print()



import numpy as np
numpy_array=np.arange(10,20)
print(numpy_array)
print(numpy_array<25)
print()



import numpy as np
# Create two arrays
a = np.array([10, 20, 30, 40])
b = np.array([15, 20, 25, 40])
print("Array a:", a)
print("Array b:", b)

# Greater than
gt_result = a > b
print("\na > b:", gt_result)

# Less than
lt_result = a < b
print("a < b:", lt_result)

# Equal to
eq_result = a == b
print("a == b:", eq_result)

# Not equal to
neq_result = a != b
print("a != b:", neq_result)

# Greater than or equal to
gte_result = a >= b
print("a >= b:", gte_result)

# Less than or equal to
lte_result = a <= b
print("a <= b:", lte_result)
print()



"""Explanation (Element-wise Comparison):
Element Position 	a Value	   b Value	 a > b 	  a == b	a <= b
   (0, 0)	          10	     15	     False	  False	    True
   (0, 1)	          20	     20    	 False	  True	    True
   (0, 2)	          30	     25	     True	  False	    False
   (1, 0)             40	     40	     False	  True	    True
   (1, 1)	          50	     55	     False	  False	    True
   (1, 2)	          60	     65	     False	  False	    True"""

# Create two 2D arrays
a = np.array([[10, 20, 30],[40, 50, 60]])
b = np.array([[15, 20, 25],[40, 55, 65]])
print("Array a:\n", a)
print("\nArray b:\n", b)

# Greater than (>)
print("\na > b:\n", a > b)

# Equal to (==)
print("\na == b:\n", a == b)

# Less than or equal to (<=)
print("\na <= b:\n", a <= b)
