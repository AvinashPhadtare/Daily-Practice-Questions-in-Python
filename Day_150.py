# ========================= Question =========================
#
# You are given two integer NumPy arrays.
#
# The first line contains three space-separated integers N,
# M, and P.
#
# The first array has N rows and P columns.
# The second array has M rows and P columns.
#
# Your task is to concatenate the two arrays along axis 0.
#
# Example:
#
# Input:
# 4 3 2
# 1 2
# 1 2
# 1 2
# 1 2
# 3 4
# 3 4
# 3 4
#
# Output:
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]]
#
# Important Points:
#
# 1. Import the NumPy module using import numpy as np.
#
# 2. Read the values of N, M, and P.
#
# 3. Read the elements of the first array containing N rows
#    and P columns.
#
# 4. Read the elements of the second array containing M rows
#    and P columns.
#
# 5. Convert both lists into NumPy arrays with integer data
#    types.
#
# 6. Use np.concatenate() to join the two arrays.
#
# 7. Use axis=0 to concatenate the arrays vertically.
#
# 8. Print the resulting concatenated array.
#
# Finally, display the combined NumPy array.
#
# ============================================================


# ======================= Solution ===========================
import numpy as np

N, M, P = map(int, input().split())

ele1 = []
ele2 = []

for _ in range(N):
    temp = input().split()
    ele1.append(temp)

for _ in range(M):
    temp = input().split()
    ele2.append(temp)

arr_1 = np.array(ele1, dtype=int)
arr_2 = np.array(ele2, dtype=int)

result = np.concatenate((arr_1, arr_2), axis=0)
print(result)
