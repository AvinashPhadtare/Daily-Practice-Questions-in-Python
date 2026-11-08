# ========================= Question =========================

# You are given an array of integers representing the heights
# of plants in a greenhouse.
#
# Your task is to calculate the average height of all plants
# with DISTINCT heights.
#
# Duplicate heights must be counted only once.
#
# Formula:
#
# Average = Sum of distinct heights / Number of distinct heights
#
# Example:
#
# Input:
# 10
# 161 182 161 154 176 170 167 171 170 174
#
# Output:
# 169.375
#
# Important Points:
#
# 1. Read an integer N representing the number of plants.
#
# 2. Read N space-separated integers representing plant heights.
#
# 3. Convert the heights into a set to remove duplicate values.
#
# 4. Calculate the sum of all distinct heights using sum().
#
# 5. Calculate the number of distinct heights using len().
#
# 6. Divide the sum of distinct heights by the number of
#    distinct heights to calculate the average.
#
# 7. Return the average rounded to 3 decimal places.
#
# 8. Complete the average(arr) function as required.
#
# ============================================================


# ======================= Solution ===========================
def average(arr):
    distinct_heights = set(arr)
    result = sum(distinct_heights) / len(distinct_heights)
    return round(result, 3)


n = int(input())
arr = list(map(int, input().split()))

result = average(arr)
print(result)
