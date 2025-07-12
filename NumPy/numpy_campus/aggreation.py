# Aggregation Functions 
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Total sum
print("Sum:", np.sum(arr))                 # 21

# Maximum value
print("Max:", np.max(arr))                 # 6

# Minimum value
print("Min:", np.min(arr))                 # 1

# Mean (average)
print("Mean:", np.mean(arr))               # 3.5

# Median
print("Median:", np.median(arr))           # 3.5

# Standard deviation
print("Standard deviation:", np.std(arr))  # 1.707...

# Variance
print("Variance:", np.var(arr))            # 2.916...
