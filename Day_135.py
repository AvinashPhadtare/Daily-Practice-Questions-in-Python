# ========================= Question =========================
#
# You are given four integers: x, y, z, and n.
#
# These represent the dimensions of a cuboid and a target
# integer n.
#
# Your task is to print a list of all possible coordinates
# [i, j, k] on a 3D grid.
#
# The coordinates must satisfy the following conditions:
#
# 1. i ranges from 0 to x, inclusive.
#
# 2. j ranges from 0 to y, inclusive.
#
# 3. k ranges from 0 to z, inclusive.
#
# 4. The sum of the coordinates i + j + k must NOT be
#    equal to n.
#
# 5. Print all valid coordinates as a list of lists.
#
# 6. Use a list comprehension instead of multiple loops.
#
# Example:
#
# Input:
# 1
# 1
# 1
# 2
#
# Output:
# [[0, 0, 0], [0, 0, 1], [0, 1, 0],
#  [1, 0, 0], [1, 1, 1]]
#
# Important Points:
#
# 1. Read four integers: x, y, z, and n.
#
# 2. Generate all possible combinations of i, j, and k.
#
# 3. Each coordinate must start from 0 and go up to its
#    corresponding dimension, including the endpoint.
#
# 4. Calculate the sum i + j + k for every combination.
#
# 5. Exclude the combinations whose sum is equal to n.
#
# 6. Store every remaining coordinate as a list containing
#    three elements: [i, j, k].
#
# 7. Use a list comprehension to generate the result.
#
# 8. Print the final list in lexicographic increasing order.
#
# ============================================================


# ======================= Solution ===========================
x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [
    [i,j,k]
    for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1)
    if i + j + k != n
]

print(result)
