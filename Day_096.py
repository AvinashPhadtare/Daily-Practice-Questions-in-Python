# ========================= Question =========================
#
# You are given a string containing only:
#   - lowercase letters
#   - uppercase letters
#   - digits
#
# Sort the characters according to the following order:
#
# 1. All lowercase letters first, in sorted order.
# 2. All uppercase letters next, in sorted order.
# 3. All odd digits next, in sorted order.
# 4. All even digits last, in sorted order.
#
# Example:
#
# Input:
# Sorting1234
#
# Separate the characters:
#
# Lowercase letters:
# o r t i n g
# Sorted:
# g i n o r t
#
# Uppercase letters:
# S
#
# Odd digits:
# 1 3
#
# Even digits:
# 2 4
#
# Combine everything:
#
# ginortS1324
#
# Output:
# ginortS1324
#
# The task is to print the string after applying this
# specific sorting order.
#
# ============================================================


# ======================= Solution ==========================
# Taking the Input
string = input()

lower = sorted(c for c in string if c.islower())
upper = sorted(c for c in string if c.isupper())
odd = sorted(c for c in string if c.isdigit() and int(c) % 2 != 0)
even = sorted(c for c in string if c.isdigit() and int(c) % 2 == 0)

# Printing the Output
print(''.join(lower + upper + odd + even))
