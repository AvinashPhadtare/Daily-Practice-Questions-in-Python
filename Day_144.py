# ========================= Question =========================
#
# You are given the shape of an array in the form of
# space-separated integers.
#
# Each integer represents the size of a different dimension
# of the array.
#
# Your task is to print two arrays of the given shape:
# one using numpy.zeros() and another using numpy.ones().
#
# Both arrays must have an integer data type.
#
# Example:
#
# Input:
# 3 3 3
#
# Output:
# [[[0 0 0]
#   [0 0 0]
#   [0 0 0]]
#
#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]
#
#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]]
#
# [[[1 1 1]
#   [1 1 1]
#   [1 1 1]]
#
#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]
#
#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]]
#
# Important Points:
#
# 1. Import NumPy using import numpy as np.
#
# 2. Read the space-separated integers from the input.
#
# 3. Convert the input values into a tuple of integers.
#
# 4. Use numpy.zeros() to create an array filled with zeros.
#
# 5. Use numpy.ones() to create an array filled with ones.
#
# 6. Both arrays must have an integer data type.
#
# 7. Print the zeros array first and then the ones array.
#
# Finally, display both arrays with the given shape.
#
# ============================================================


# ======================= Solution ===========================
import numpy as np

shape = tuple(map(int, input().split()))

print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))
