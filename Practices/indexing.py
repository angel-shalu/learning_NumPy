#  indexing
#  Indexing in Python starts with 0.

 #Using1Darray
import numpy as np
special_nums=np.array([0.577,1.618,2.718,3.14,6,37,1729])
print(special_nums[0])
print(special_nums[-1]) #Thisshowsnegativeindexingandnegativeindexingstartswith-1.
print(special_nums[-3])
print(special_nums[2])
print(special_nums[5])

 #Using2Darray
special_nums=np.array([0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]).reshape(3,4)
# special_nums=np.reshape(special_nums,(3,4))
print(special_nums)
print("Length:", len(special_nums))
print(special_nums[1,1])   # It means first line, first column, namely the output is 5.
print(special_nums[2,3])   # It means second line,third column,namely the output is 89
 