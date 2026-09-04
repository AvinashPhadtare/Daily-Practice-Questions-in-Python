# ========================= Question =========================
# Given an integer n and n space-separated integers,
# create a tuple t containing those integers.
# Then print the result of hash(t).
#
# Example:
# Input:
# 2
# 1 2
#
# Output:
# 3713081631934410656
# ============================================================


# Solution :- 
n = int(input())

t = tuple(map(int, input().split()))

print(hash(t))

# Optimized solution :-
# HackerRank's Expected code:- 
# Read number of elements
n = int(input())

# Read the tuple
t = tuple(map(int, input().split()))

# HackerRank's old tuple hash algorithm
x = 0x345678
mult = 1000003
z = len(t)

for y in t:
    x = ((x ^ y) * mult) & ((1 << 64) - 1)
    z -= 1
    mult += 82520 + z + z

x = (x + 97531) & ((1 << 64) - 1)

# Convert unsigned 64-bit number to signed 64-bit number
if x >= (1 << 63):
    x -= (1 << 64)

if x == -1:
    x = -2

print(x)
