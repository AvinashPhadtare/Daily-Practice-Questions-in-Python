# ========================= Question =========================
#
# You are given two values, a and b.
#
# Your task is to perform integer division of a by b
# and print the result.
#
# Input Format:
#
# The first line contains an integer T, representing
# the number of test cases.
#
# The next T lines each contain two space-separated
# values, a and b.
#
# Task:
#
# For each test case:
#
# 1. Convert a and b into integers.
#
# 2. Perform integer division using //.
#
# 3. Print the result of the division.
#
# 4. If ZeroDivisionError or ValueError occurs,
#    print the error message in the required format.
#
# Example:
#
# Input:
# 3
# 1 0
# 2 $
# 3 1
#
# Output:
# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'
# 3
#
# Important Points:
#
# - Use int() to convert the input values into integers.
#
# - Use // for integer division in Python 3.
#
# - Use try to execute code that might produce an error.
#
# - Use except to handle the errors.
#
# - ZeroDivisionError occurs when the divisor is zero.
#
# - ValueError occurs when a value cannot be converted
#   into an integer.
#
# Finally, print the division result or the error message.
#
# ============================================================


# ======================= Solution ============================
T = int(input())

for _ in range(T):
    a, b = input().split()

    try:
        print(int(a) // int(b))

    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")

    except ValueError as e:
        print("Error Code:", e)
