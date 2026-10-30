# ========================== Question =========================
#
# You are given N integers and a target value.
#
# Your task is to count the number of pairs of numbers whose
# sum is equal to the target.
#
# Use itertools.combinations so that every pair is checked
# exactly once.
#
# Example:
#
# Input:
# 5
# 1 2 3 4 5
# 6
#
# Pairs with sum 6 = (1, 5) and (2, 4)
#
# Output:
# 2
#
# Important Point:
#
# combinations(nums, 2) never pairs a number with itself and
# never gives both (a, b) and (b, a).
#
# ============================================================

# ======================= Solution ==========================
from itertools import combinations

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

count = 0
for a, b in combinations(nums, 2):
    if a + b == target:
        count += 1

print(count)
