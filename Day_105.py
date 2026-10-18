# ========================= Question =========================
#
# You are given two sets, A and B.
#
# Your task is to check whether set A is a subset of set B.
#
# A set A is a subset of set B if every element of A is
# also present in set B.
#
# If A is a subset of B, print True.
# Otherwise, print False.
#
# Example:
#
# Input:
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2
#
# Output:
# True
# False
# False
#
# Important Points:
#
# 1. Read an integer T representing the number of test cases.
#
# 2. For each test case:
#
#    a. Read an integer N representing the number of elements
#       in set A.
#
#    b. Read the elements of set A.
#
#    c. Read an integer M representing the number of elements
#       in set B.
#
#    d. Read the elements of set B.
#
# 3. Use the .issubset() method to check whether every element
#    of A is present in B.
#
# 4. If A is a subset of B, print True.
#
# 5. Otherwise, print False.
#
# 6. Print the result for each test case on a separate line.
#
# ============================================================


# ======================= Solution ===========================
T = int(input())

for _ in range(T):
    n = int(input())
    A = set(map(int, input().split()))

    m = int(input())
    B = set(map(int, input().split()))

    print(A.issubset(B))
