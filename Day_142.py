# ========================= Question =========================
#
# You are given two integers N and M.
#
# Your task is to print an identity array of size N x M,
# with 1's on the main diagonal and 0's everywhere else.
#
# Example:
#
# Input:
# 3 3
#
# Output:
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
#
# Important Points:
#
# 1. Import the NumPy module using import numpy.
#
# 2. Add numpy.set_printoptions(legacy='1.13') below
#    the NumPy import to get the required output format.
#
# 3. Read the two space-separated integers N and M.
#
# 4. Use numpy.eye(N, M) to create an identity array
#    of size N x M.
#
# 5. The main diagonal elements will be 1's, and all
#    other elements will be 0's.
#
# 6. Print the resulting array.
#
# ============================================================


# ======================= Solution ===========================
import numpy as np 


N, M  = map(int, input().split())

np.set_printoptions(legacy='1.13')

print(np.eye(N,M, k = 0))
