# ========================= Question =========================
#
# You are given a set A and N other sets.
#
# Your task is to check whether set A is a STRICT SUPERSET
# of every one of the N other sets.
#
# A strict superset means:
# - Every element of the other set exists in set A.
# - Set A contains at least one additional element that is
#   not present in the other set.
#
# If A is a strict superset of every other set, print True.
# Otherwise, print False.
#
# Example:
#
# Input:
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
#
# Output:
# False
#
# Important Points:
#
# 1. Read the space-separated elements of set A.
#
# 2. Read an integer N representing the number of other sets.
#
# 3. For each of the N sets:
#
#    a. Read its space-separated elements.
#
#    b. Check whether set A is a strict superset of that set
#       using the .issuperset() method and a length comparison,
#       or use the > operator directly.
#
# 4. A > B returns True if A is a strict superset of B.
#
# 5. If A is a strict superset of every other set, print True.
#
# 6. If even one set is not a strict subset of A, print False.
#
# ============================================================

# ======================= Solution ===========================
A = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    B = set(map(int, input().split()))

    if not A > B:
        result = False
        break

print(result)
