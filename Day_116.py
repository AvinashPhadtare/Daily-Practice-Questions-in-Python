# ========================== Question =========================
#
# You are given N lines, each containing a student NAME and the
# CLASS in which the student studies.
#
# Your task is to group the students by class using defaultdict.
# Print the classes in ascending order, and for each class print
# the student names in alphabetical order separated by ", ".
#
# Example:
#
# Input:
# 5
# Raymond 7
# Steven 4
# Adrian 7
# Stewart 4
# Peter 6
#
# Output:
# 4: Steven, Stewart
# 6: Peter
# 7: Adrian, Raymond
#
# Important Point:
#
# defaultdict(list) removes the need to check whether a key
# already exists before appending. Convert CLASS to int so that
# class 10 comes after class 9.
#
# ============================================================

# ======================= Solution ==========================
from collections import defaultdict

n = int(input())
groups = defaultdict(list)

for _ in range(n):
    name, cls = input().split()
    groups[int(cls)].append(name)

for cls in sorted(groups):
    print(f"{cls}: {', '.join(sorted(groups[cls]))}")
