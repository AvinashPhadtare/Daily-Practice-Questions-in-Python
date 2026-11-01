# ========================== Question =========================
#
# You are given a string S and a substring T.
#
# Your task is to count how many times T occurs in S.
# The occurrences are allowed to overlap.
#
# Example:
#
# Input:
# ABCDCDC
# CDC
#
# "CDC" starts at index 2 and again at index 4
#
# Output:
# 2
#
# Important Point:
#
# str.count() does not count overlapping matches, so check
# every starting position yourself using startswith(sub, i).
#
# ============================================================

# ======================= Solution ==========================
s = input().strip()
sub = input().strip()

count = 0
for i in range(len(s) - len(sub) + 1):
    if s.startswith(sub, i):
        count += 1

print(count)
