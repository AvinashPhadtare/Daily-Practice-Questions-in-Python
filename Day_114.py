# ========================== Question =========================
#
# You are given N lines, each containing two values A and B.
#
# Your task is to print A divided by B rounded to 2 decimal
# places.
#   - If B is zero, print "Division by zero"
#   - If A or B is not a valid integer, print "Invalid input"
#
# Example:
#
# Input:
# 4
# 10 2
# 7 0
# a 5
# 9 4
#
# Output:
# 5.00
# Division by zero
# Invalid input
# 2.25
#
# Important Point:
#
# Keep the int() conversion inside the try block, because that
# is where ValueError is raised. Catch specific exceptions, not
# a bare except.
#
# ============================================================

# ======================= Solution ==========================
n = int(input())

for _ in range(n):
    try:
        a, b = input().split()
        print(f"{int(a) / int(b):.2f}")
    except ZeroDivisionError:
        print("Division by zero")
    except ValueError:
        print("Invalid input")
