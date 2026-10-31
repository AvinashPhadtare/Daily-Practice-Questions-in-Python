# ========================== Question =========================
#
# N students are enrolled in Maths and M students are enrolled
# in Physics. You are given their roll numbers.
#
# Your task is to print, in ascending order (one per line), the
# roll numbers of students who are enrolled in exactly one of
# the two subjects.
#
# Example:
#
# Input:
# 5
# 1 2 3 4 5
# 4
# 4 5 6 7
#
# Maths   = {1, 2, 3, 4, 5}
# Physics = {4, 5, 6, 7}
# Exactly one subject = {1, 2, 3, 6, 7}
#
# Output:
# 1
# 2
# 3
# 6
# 7
#
# Important Point:
#
# "Exactly one" means the symmetric difference of the two sets,
# which is done with the ^ operator.
#
# ============================================================

# ======================= Solution ==========================
n = int(input())
maths = set(map(int, input().split()))
m = int(input())
physics = set(map(int, input().split()))

for roll in sorted(maths ^ physics):
    print(roll)
