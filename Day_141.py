# ========================= Question =========================
#
# You are given a 2-D NumPy array of size N x M.
#
# Your task is to find:
#
# 1. The mean along axis 1.
# 2. The variance along axis 0.
# 3. The standard deviation of the entire array.
#
# Example:
#
# Input:
# 2 2
# 1 2
# 3 4
#
# Output:
# [ 1.5  3.5]
# [ 1.  1.]
# 1.11803398875
#
# Important Points:
#
# 1. Import NumPy using import numpy as np.
#
# 2. Read the number of rows N and columns M.
#
# 3. Read the next N lines containing M space-separated
#    integers and store them in a list.
#
# 4. Convert the list into a 2-D NumPy array.
#
# 5. Use np.mean(arr, axis=1) to calculate the mean
#    of each row.
#
# 6. Use np.var(arr, axis=0) to calculate the variance
#    of each column.
#
# 7. Use np.std(arr) to calculate the standard deviation
#    of all elements in the array.
#
# 8. Print the mean, variance, and standard deviation
#    in the given order.
#
# ============================================================

# ======================= Solution ===========================

import numpy as np

N, M = map(int, input().split())

ele = []

for _ in range(N):
    temp = list(map(int, input().split()))
    ele.append(temp)

arr = np.array(ele, dtype=int)

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.std(arr))
