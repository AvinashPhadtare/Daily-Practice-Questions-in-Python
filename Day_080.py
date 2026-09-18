# ========================= Question =========================
# You are given a string.
#
# Find the first occurrence of an alphanumeric character
# that has consecutive repetitions.
#
# The search should be performed from left to right.
#
# If a repeating alphanumeric character is found,
# print that character.
#
# If no such character exists, print -1.
#
# Example:
#
# Input:
# ..12345678910111213141516171820212223
#
# Output:
# 1
#
# Explanation:
# '..' is the first repeating sequence, but '.' is not
# an alphanumeric character.
#
# Later, '111' occurs.
# Therefore, the first repeating alphanumeric character is '1'.
# ============================================================

# Solution:- 

import re

svg = input()
match = re.search(r'([A-Za-z0-9])\1', svg)
 
if match:
    print(match.group(0))
else:
    print(-1)
