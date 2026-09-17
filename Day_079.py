# ========================= Question =========================
# You are given a string consisting only of digits (0-9),
# commas (,) and dots (.).
#
# Complete the regex_pattern below.
#
# The regex pattern will be used with re.split() to split
# the string at every comma (,) and dot (.).
#
# It is guaranteed that every comma and dot is preceded
# and followed by a digit.
#
# Sample Input:
# 100,000,000.000
#
# Sample Output:
# 100
# 000
# 000
# 000
#
# Complete only the regex_pattern.
# =============================================================


# Solution:-
import re
regex_pattern = r",|\."
s = input()

result = re.split(regex_pattern,s)

for val in result:
    print(value)
