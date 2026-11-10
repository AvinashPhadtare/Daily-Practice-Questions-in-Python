# ========================= Question =========================
#
# You are given two sets of student roll numbers.
#
# One set contains the roll numbers of students who have
# subscribed to the English newspaper, and the other set
# contains the roll numbers of students who have subscribed
# to the French newspaper.
#
# Your task is to find the total number of students who have
# subscribed to at least one of the two newspapers.
#
# Example:
#
# Input:
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
#
# Output:
# 13
#
# Important Points:
#
# 1. Read an integer N representing the number of students
#    subscribed to the English newspaper.
#
# 2. Read N space-separated roll numbers and store them
#    in a set named english.
#
# 3. Read an integer M representing the number of students
#    subscribed to the French newspaper.
#
# 4. Read M space-separated roll numbers and store them
#    in a set named french.
#
# 5. Use the .union() operation to combine both sets.
#
# 6. The union contains all elements that exist in either
#    set or in both sets.
#
# 7. Duplicate roll numbers present in both sets are counted
#    only once because sets store unique elements.
#
# 8. Use len() to calculate the total number of students
#    who have subscribed to at least one newspaper.
#
# 9. Print the total number of students on a single line.
#
# ============================================================

# ======================= Solution ===========================
n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

result = english.union(french)

print(len(result))
