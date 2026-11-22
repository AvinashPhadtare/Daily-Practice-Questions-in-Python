# ========================= Question =========================
#
# You are given two NumPy arrays A and B, both having
# dimensions N x N.
#
# Your task is to compute the matrix product of A and B.
#
# Example:
#
# Input:
# 2
# 1 2
# 3 4
# 1 2
# 3 4
#
# Output:
# [[ 7 10]
#  [15 22]]
#
# Important Points:
#
# 1. Import the NumPy module using import numpy.
#
# 2. Read the integer N, which represents the number of
#    rows and columns of both arrays.
#
# 3. Read the next N lines and store the integers of
#    array A in a list.
#
# 4. Read the following N lines and store the integers
#    of array B in another list.
#
# 5. Convert both lists into NumPy arrays.
#
# 6. Use numpy.dot(A, B) or numpy.matmul(A, B) to
#    calculate the matrix product.
#
# 7. Print the resulting matrix.
#
# ============================================================

# ======================= Solution ===========================
import numpy as np 

N = int(input())

list1 = []
list2 = []

for _ in range(N):
    temp = list(map(int,input().split()))
    list1.append(temp)

for _ in range(N):
    temp = list(map(int,input().split()))
    list2.append(temp)


arr1 = np.array(list1, dtype = int)
arr2 = np.array(list2, dtype = int)

print(np.dot(arr1, arr2))
