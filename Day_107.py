# ========================= Question =========================
#
# You are given a set A and a number of other sets.
#
# Your task is to perform specific mutation operations on
# set A using the elements of the other sets.
#
# The operations are:
#
# 1. intersection_update(B):
#    Updates set A with only the elements common to A and B.
#
# 2. update(B):
#    Adds all elements of set B to set A.
#
# 3. symmetric_difference_update(B):
#    Updates set A with elements that exist in either A or B,
#    but not in both.
#
# 4. difference_update(B):
#    Removes all elements of B from set A.
#
# Example:
#
# Input:
# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11
# update 2
# 55 66
# symmetric_difference_update 5
# 22 7 35 62 58
# difference_update 7
# 11 22 35 55 58 62 66
#
# Output:
# 38
#
# Important Points:
#
# 1. Read an integer N representing the number of elements
#    in set A.
#
# 2. Read N space-separated integers and store them in set A.
#
# 3. Read an integer M representing the number of mutation
#    operations to perform.
#
# 4. For each operation, read the operation name and the
#    number of elements in the other set.
#
# 5. Read the elements of the other set.
#
# 6. Perform the specified mutation operation on set A.
#
# 7. Repeat the process for all M operations.
#
# 8. Calculate the sum of the remaining elements in set A
#    using sum(A).
#
# 9. Print the sum on a single line.
#
# ============================================================


# ======================= Solution ===========================
n = int(input())
A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    operation, length = input().split()
    other_set = set(map(int, input().split()))

    if operation == "intersection_update":
        A.intersection_update(other_set)

    elif operation == "update":
        A.update(other_set)

    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

    elif operation == "difference_update":
        A.difference_update(other_set)

print(sum(A))
