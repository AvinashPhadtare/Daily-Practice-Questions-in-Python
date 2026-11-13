# ========================= Question =========================
#
# You are given an array of integers and two disjoint sets, A and B.
#
# Your task is to calculate your total happiness based on the
# elements present in the array.
#
# Initially, your happiness is 0.
#
# Rules:
# - If an element is present in set A, increase happiness by 1.
# - If an element is present in set B, decrease happiness by 1.
# - If an element is present in neither set, happiness remains unchanged.
#
# Example:
#
# Input:
# 3 2
# 1 5 3
# 3 1
# 5 7
#
# Output:
# 1
#
# Important Points:
#
# 1. Read two integers N and M representing the size of the
#    array and the size of each set, respectively.
#
# 2. Read N space-separated integers and store them in an array.
#
# 3. Read M space-separated integers and store them in set A.
#
# 4. Read M space-separated integers and store them in set B.
#
# 5. Initialize happiness to 0.
#
# 6. Traverse each element of the array.
#
# 7. If an element exists in set A, increase happiness by 1.
#
# 8. If an element exists in set B, decrease happiness by 1.
#
# 9. If an element exists in neither set, do not change happiness.
#
# 10. The array may contain duplicate elements, so process every
#     element separately.
#
# 11. Print the final happiness as a single integer.
#
# ============================================================


# ======================= Solution ===========================
N, M = map(int,input().split())

arr = list(map(int, input().split()))

set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

happiness = 0

for num in arr:
    if num in set_A:
        happiness += 1
    elif num in set_B:
        happiness -= 1

print(happiness)
