# ========================= Question =========================
#
# You are given a square matrix A with dimensions N x N.
#
# Your task is to find the determinant of matrix A.
#
# Note:
# Round the answer to 2 places after the decimal.
#
# Example:
#
# Input:
# 2
# 1.1 1.1
# 1.1 1.1
#
# Output:
# 0.0
#
# Explanation:
#
# The given matrix is:
# A = [[1.1, 1.1],
#      [1.1, 1.1]]
#
# For a 2 x 2 matrix:
# det(A) = (a*d) - (b*c)
#
# det(A) = (1.1 * 1.1) - (1.1 * 1.1)
# det(A) = 0.0
#
# Important Points:
#
# 1. Import the NumPy module using import numpy as np.
#
# 2. Read the integer N representing the matrix dimensions.
#
# 3. Read the next N lines containing N space-separated
#    floating-point numbers.
#
# 4. Convert the input into a NumPy array.
#
# 5. Use np.linalg.det(A) to calculate the determinant.
#
# 6. Round the determinant to 2 decimal places using round().
#
# 7. Print the final result.
#
# ============================================================

# ======================= Solution ===========================
import numpy as np

N = int(input())

ele = []

for _ in range(N):
    temp = list(map(float, input().split()))
    ele.append(temp)

A = np.array(ele, dtype=float)

det = np.linalg.det(A)

print(round(det, 2))
