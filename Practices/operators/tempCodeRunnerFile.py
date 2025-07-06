# 4. Reciprocal (1/x) → You should avoid division by zero!
reciprocal_arr = np.reciprocal(np.where(arr != 0, arr, 1))  # Avoid division by zero
print("Reciprocal (avoiding zero):", reciprocal_arr)