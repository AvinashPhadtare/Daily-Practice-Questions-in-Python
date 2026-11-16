# ========================= Question =========================
#
# You are given four integers: x, y, z, and n.
#
# Generate all possible coordinates [i, j, k] where:
#
# 1. i ranges from 0 to x.
# 2. j ranges from 0 to y.
# 3. k ranges from 0 to z.
# 4. The sum i + j + k must NOT be equal to n.
#
# Use list comprehension to generate the result.
#
# Example:
#
# Input:
# x = 2
# y = 1
# z = 1
# n = 2
#
# Output:
# [[0, 0, 0], [0, 0, 1], [0, 1, 0],
#  [1, 0, 0], [1, 1, 1], [2, 0, 1],
#  [2, 1, 0], [2, 1, 1]]
#
# ============================================================

# ======================= Solution ===========================
x = 2
y = 1
z = 1
n = 2

result = [
    [i,j,k]
    for i in range(x+1)
    for j in range(j+1)
    for k in range(k+1)
    if i+j+k != n
]

print(result)
