# ADDITION
import numpy as np
numpy_arange= np.arange(20,50, 5)   #np.arange(start=20 stop=50 step=5)	Creates evenly spaced numbers in a range
print("Array : ",numpy_arange)
print()
numpy_arange=np.reshape(numpy_arange,(2,3))
print("Reshape Array:\n",numpy_arange)
print()
numpy_array= np.array([20,50,22,7,2,72]).reshape(2,3)
print("Reshape:\n",numpy_array)
print()
print('Added array =')
addition=numpy_arange+numpy_array #Addition
print(addition)

# Another code 
numpy_arange= np.arange(20,50, 7.5).reshape(2,2)
numpy_array= np.array([0.577,1.618, 2.718, 3.14]).reshape(2,2)
print(numpy_arange)
print()
print(numpy_array)
print()
print('Added array:')
addition=numpy_arange+numpy_array #Addition
print(addition)



# SUBSTRACTION
import numpy as np
numpy_arange= np.arange(20,50, 5)   #np.arange(start=20 stop=50 step=5)	Creates evenly spaced numbers in a range
print("Array : ",numpy_arange)
print()
numpy_arange=np.reshape(numpy_arange,(2,3))
print("Reshape Array:\n",numpy_arange)
print()
numpy_array= np.array([20,50,22,7,2,72]).reshape(2,3)
print("Reshape:\n",numpy_array)
print()
print('Subtracted array =')
substraction=numpy_arange-numpy_array #Substraction
print(substraction)


# MULTIPLICATION
numpy_arange=np.arange(20,50,5).reshape(2,3)
numpy_array=np.array([20,50,22,7,2,72]).reshape(2,3)
print("Array :\n",numpy_arange)
print()
print("Array2 :",numpy_array)
print()
print("Multiplication Array")
multiply=numpy_arange*numpy_array  #Multiplication
print(multiply)


# DIVISION
numpy_arange=np.arange(20,50,5).reshape(2,3)
numpy_array=np.array([20,50,22,7,2,72]).reshape(2,3)
print("Array :\n",numpy_arange)
print()
print("Array2 :\n",numpy_array)
print()
print("Divided Array")
division=numpy_arange/numpy_array  #Division
print(division)


# FLOOR DIVISION
"""Floor division means dividing numbers and rounding down the result to the nearest whole number (integer).
It discards the decimal part and keeps only the integer part of the division result."""

numpy_arange=np.arange(20,50,5).reshape(2,3)
numpy_array=np.array([20,50,22,7,2,72]).reshape(2,3)
print("Array :\n",numpy_arange)
print()
print("Array2 :\n",numpy_array)
print()
print("Divided Array")
division=numpy_arange//numpy_array  #Division
print(division)


# MODULUS
numpy_arange=np.arange(20,50,5).reshape(2,3)
numpy_array=np.array([20,50,22,7,2,72]).reshape(2,3)
print("Array :\n",numpy_arange)
print()
print("Array2 :\n",numpy_array)
print()
print("Modulus Array")
modulus=numpy_arange%numpy_array  #Modulus
print(modulus)


# EXPONENTIATION
numpy_arange=np.arange(20,50,5).reshape(2,3)
numpy_array=np.array([20,50,22,7,2,72]).reshape(2,3)
print("Array :\n",numpy_arange)
print()
print("Array2 :\n",numpy_array)
print()
print("Exponentiated Array")
exponent=numpy_arange//numpy_array  #Exponentiation
print(exponent)
