# Day 24
# ========================= Question =========================
#
# You are given a polynomial P of a single variable x.
#
# You are also given the values of x and k.
#
# Your task is to verify whether P(x) = k.
#
# Constraints:
#
# 1. All coefficients of polynomial P are integers.
# 2. x and k are also integers.
#
# Example:
#
# Input:
# 1 4
# x**3 + x**2 + x + 1
#
# Output:
# True
#
# Explanation:
#
# Given:
# x = 1
# k = 4
# P(x) = x**3 + x**2 + x + 1
#
# Substituting x = 1:
# P(1) = 1**3 + 1**2 + 1 + 1
# P(1) = 1 + 1 + 1 + 1
# P(1) = 4
#
# Since P(x) = k, the output is True.
#
# Important Points:
#
# 1. Read the integer values x and k.
#
# 2. Read the polynomial expression P.
#
# 3. Use eval(P) to evaluate the polynomial expression.
#
# 4. Check whether the evaluated result is equal to k.
#
# 5. Print True if the condition is satisfied; otherwise,
#    print False.
#
# ============================================================

# ======================= Solution ===========================

x, k = map(int, input().split())

P = input()

print(eval(P) == k)
