
# ========================= Question =========================
#
# You are given two integer NumPy arrays A and B of the same
# dimensions.
#
# The first line contains two space-separated integers N and M,
# representing the number of rows and columns of the arrays.
#
# The next N lines contain M space-separated integers for
# array A.
#
# The following N lines contain M space-separated integers
# for array B.
#
# Your task is to perform the following operations on arrays
# A and B and print each result in the given order:
#
# 1. Addition:       A + B
# 2. Subtraction:    A - B
# 3. Multiplication: A * B
# 4. Integer Division: A // B
# 5. Modulus:        A % B
# 6. Power:          A ** B
#
# Example:
#
# Input:
# 1 4
# 1 2 3 4
# 5 6 7 8
#
# Output:
# [[ 6  8 10 12]]
# [[-4 -4 -4 -4]]
# [[ 5 12 21 32]]
# [[0 0 0 0]]
# [[1 2 3 4]]
# [[    1    64  2187 65536]]
#
# Important Points:
#
# 1. Import NumPy using import numpy as np.
#
# 2. Read the number of rows and columns.
#
# 3. Read the elements of arrays A and B and convert them
#    into integer NumPy arrays.
#
# 4. Use the + operator to add corresponding elements.
#
# 5. Use the - operator to subtract corresponding elements.
#
# 6. Use the * operator to multiply corresponding elements.
#
# 7. Use the // operator for floor division.
#
# 8. Use the % operator to calculate the remainder.
#
# 9. Use the ** operator to calculate powers.
#
# 10. Print the results of all six operations in the given
#     order.
#
# Finally, display the results of all six operations.
#
# ============================================================


# ======================= Solution ===========================

import numpy as np

N, M = map(int, input().split())

A = np.array([input().split() for _ in range(N)], dtype=int)
B = np.array([input().split() for _ in range(N)], dtype=int)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
