# ========================= Question =========================
#
# You are given a collection of country stamps.
#
# Your task is to find the total number of distinct countries
# represented by the stamps.
#
# A country may appear multiple times in the collection,
# but it should be counted only once.
#
# Example:
#
# Input:
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France
#
# Output:
# 5
#
# Important Points:
#
# 1. Read an integer N representing the total number of
#    country stamps.
#
# 2. Create an empty set to store distinct country names.
#
# 3. Read the country name for each stamp, one by one.
#
# 4. Use the .add() operation to insert each country name
#    into the set.
#
# 5. Sets automatically remove duplicate elements.
#
# 6. If a country appears multiple times, it will be stored
#    only once in the set.
#
# 7. After reading all the country names, find the total
#    number of distinct countries using len().
#
# 8. Print the total number of distinct country stamps.
#
# ============================================================

# ======================= Solution ===========================
N = int(input())

set_A = set()
for _ in range(N):
    country = input()
    set_A.add(country)
print(len(set_A))
