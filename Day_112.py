# ========================== Question =========================
#
# You are given N mobile numbers.
#
# Your task is to print "YES" if the number is valid, otherwise
# print "NO".
#
# A valid mobile number has exactly 10 digits and starts with
# 6, 7, 8 or 9.
#
# Example:
#
# Input:
# 4
# 9876543210
# 5876543210
# 98765
# 7000000001
#
# Output:
# YES
# NO
# NO
# YES
#
# Important Point:
#
# Use ^ and $ in the pattern so that the whole string must
# match, not just a part of it.
#
# ============================================================

# ======================= Solution ==========================
import re

n = int(input())

for _ in range(n):
    number = input().strip()
    if re.match(r"^[6-9]\d{9}$", number):
        print("YES")
    else:
        print("NO")
