# ========================= Question =========================
#
# You are given a 2-D NumPy array with space-separated integers.
#
# The first line contains two integers representing the
# number of rows and columns of the array.
#
# Your task is to find the minimum value along axis 1
# and then find the maximum value of the resulting array.
#
# Example:
#
# Input:
# 4 2
# 2 5
# 3 7
# 1 3
# 4 0
#
# Output:
# 3
#
# Important Points:
#
# 1. Import the NumPy module using import numpy.
#
# 2. Read the number of rows and columns.
#
# 3. Read the integer elements and create a NumPy array.
#
# 4. Use min(axis=1) to find the minimum of each row.
#
# 5. Use max() to find the maximum of those minimum values.
#
# 6. Print the final result.
#
# ============================================================


# ======================= Solution ===========================
import numpy as np

N, M = input().split()

ele = []
for _ in range(int(N)):
    temp = list(map(int, input().split()))
    ele.append(temp)

my_arr = np.array(ele, dtype=int)

min_values = np.min(my_arr, axis=1)
result = np.max(min_values)

print(result)
