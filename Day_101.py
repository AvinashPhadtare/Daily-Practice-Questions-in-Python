# ========================= Question =========================
#
# You are given an expression in a single line.
#
# Read that line as a string variable, such as var, and
# print the result using eval(var).
#
# Note:
# Python 2 users should import:
# from __future__ import print_function
#
# Constraint:
# The input string contains fewer than 100 characters.
#
# Example:
#
# Input:
# print(2 + 3)
#
# Output:
# 5
#
# Explanation:
#
# 1. Read the expression as a string.
#
# 2. Use eval(var) to execute the expression.
#
# 3. The expression print(2 + 3) calculates 2 + 3.
#
# 4. The result printed is 5.
#
# Important Points:
#
# 1. Read the input using input().
#
# 2. Store the expression in a variable named var.
#
# 3. Use eval(var) to evaluate the expression.
#
# 4. Print the result by executing eval(var).
#
# ============================================================

# ======================= Solution ===========================

var = input()
eval(var)
