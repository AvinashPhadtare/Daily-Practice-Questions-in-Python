# ========================= Question =========================
#
# You are given two NumPy arrays A and B.
#
# Your task is to compute their inner product and outer
# product.
#
# Example:
#
# Input:
# 0 1
# 2 3
#
# Output:
# 3
# [[0 0]
#  [2 3]]
#
# Important Points:
#
# 1. Import the NumPy module using import numpy as np.
#
# 2. Read the space-separated elements of array A.
#
# 3. Read the space-separated elements of array B.
#
# 4. Convert both lists into NumPy arrays of integers.
#
# 5. Use np.inner(A, B) to calculate the inner product.
#
# 6. Use np.outer(A, B) to calculate the outer product.
#
# 7. Print the inner product first and the outer product
#    second.
#
# ============================================================


# ======================= Solution ===========================
import numpy as np

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

arr1 = np.array(list1, dtype=int)
arr2 = np.array(list2, dtype=int)

print(np.inner(arr1, arr2))
print(np.outer(arr1, arr2))
