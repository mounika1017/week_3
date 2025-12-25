import numpy as np
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("2D Array:")
print(arr)
print("matrix size:", arr.shape)
print("Element at position (2,2):", arr[2][2])
print("Row-wise sum:", np.sum(arr,axis=1))
print("Transpose of array:")
print(arr.T)
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))
print("Average of all elements:", np.mean(arr))
