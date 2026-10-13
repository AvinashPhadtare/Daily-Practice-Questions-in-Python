# ========================= Question =========================
#
# You are given a 1-D NumPy array containing space-separated
# floating-point numbers.
#
# Your task is to print the floor, ceiling, and round-to-nearest
# integer (rint) values of all elements in the array.
#
# Example:
#
# Input:
# 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
#
# Output:
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# [  1.   2.   3.   4.   6.   7.   8.   9.  10.]
#
# Important Points:
#
# 1. Import NumPy using import numpy.
#
# 2. Add numpy.set_printoptions(legacy='1.13') below the
#    NumPy import to get the required output format.
#
# 3. Read the space-separated floating-point numbers using
#    input().split().
#
# 4. Convert the input into a NumPy array of float values.
#
# 5. Use numpy.floor(A) to find the floor of each element.
#
# 6. Use numpy.ceil(A) to find the ceiling of each element.
#
# 7. Use numpy.rint(A) to round each element to the nearest
#    integer.
#
# 8. Print the results in the order: floor, ceil, and rint.
#
# ============================================================

# ======================= Solution ===========================
import numpy as np

np.set_printoptions(legacy="1.13")
# This helps produce the array formatting expected by HackerRank, including the spacing and decimal representation.

A = np.array(input().split(), dtype=float)

print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))
