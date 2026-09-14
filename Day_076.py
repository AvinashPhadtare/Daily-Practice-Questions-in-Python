# ========================= Question =========================
# Perform append, pop, popleft and appendleft operations
# on an empty deque.
#
# The first line contains the number of operations.
# Each following line contains an operation and, if required,
# a value.
#
# Finally, print all elements remaining in the deque.
# =============================================================

# Solution:-

from collections import deque

d = deque()

n = int(input())
for i in range(n):
    command = input().split()
    operation = command[0]
    if operation == "append":
        d.append(command[1])
    elif operation == "appendleft":
        d.appendleft(command[1])
    elif operation == "pop":
        d.pop()
    elif operation == "popleft":
        d.popleft()

print(*d)
