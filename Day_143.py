# ========================= Question =========================
#
# You are given a 2-D NumPy array with dimensions N x M.
#
# Your task is to find the sum of the array elements along
# axis 0 and then find the product of the resulting array.
#
# Example:
#
# Input:
# 2 2
# 1 2
# 3 4
#
# Output:
# 24
#
# Explanation:
#
# The given array is:
# [[1, 2],
#  [3, 4]]
#
# Step 1: Calculate the sum along axis 0.
#         [1+3, 2+4] = [4, 6]
#
# Step 2: Calculate the product of the sum array.
#         4 * 6 = 24
#
# Important Points:
#
# 1. Import NumPy using import numpy as np.
#
# 2. Read N and M from the first input line.
#
# 3. Read the next N lines and store the integers in a list.
#
# 4. Convert the list into a 2-D NumPy array.
#
# 5. Use np.sum(arr, axis=0) to calculate the sum of each
#    column.
#
# 6. Use np.prod() to calculate the product of the sums.
#
# 7. Print the final result.
#
# ============================================================

# ======================= Solution ===========================
import numpy as np

N,M = map(int, input().split())

ele = []
for _ in range(N):
    temp = list(map(int,input().split()))
    ele.append(temp)

arr = np.array(ele,dtype = int)

add = np.sum(arr, axis = 0)

print(np.prod(add))
