# ========================= Question =========================
#
# You are given two sets of integers, A and B.
#
# Your task is to find the symmetric difference between
# these two sets.
#
# Symmetric difference means the elements that exist in
# either set A or set B, but NOT in both sets.
#
# Example:
#
# Input:
# 4
# 2 4 5 9
# 4
# 2 4 11 12
#
# Output:
# 5
# 9
# 11
# 12
#
# Important Points:
#
# 1. Read an integer M representing the size of set A.
#
# 2. Read M space-separated integers and store them in A.
#
# 3. Read an integer N representing the size of set B.
#
# 4. Read N space-separated integers and store them in B.
#
# 5. Find the symmetric difference between A and B.
#
# 6. Include elements that exist in only one of the sets.
#
# 7. Exclude elements that exist in both sets.
#
# 8. Sort the resulting integers in ascending order.
#
# 9. Print each integer on a separate line.
#
# ============================================================

# ======================= Solution ===========================
m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

result = a.symmetric_difference(b)

for num in sorted(result):
    print(num)
