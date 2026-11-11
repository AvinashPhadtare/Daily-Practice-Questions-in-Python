# ========================= Question =========================
#
# You are given a non-empty set of integers, S.
#
# Your task is to perform a series of commands on the set.
#
# The commands can be:
# - pop: Removes an arbitrary element from the set.
# - remove x: Removes element x from the set. Raises an error
#   if x is not present in the set.
# - discard x: Removes element x from the set if it exists.
#   Does nothing if x is not present in the set.
#
# Example:
#
# Input:
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5
#
# Output:
# 4
#
# Important Points:
#
# 1. Read an integer N representing the number of elements
#    in the set S.
#
# 2. Read N space-separated integers and store them in a set.
#    Convert the elements to integers while creating the set.
#
# 3. Read an integer M representing the number of commands.
#
# 4. Execute each command one by one.
#
# 5. If the command is "pop", remove an arbitrary element
#    from the set using S.pop().
#
# 6. If the command is "remove x", remove element x using
#    S.remove(x). It raises a KeyError if x is absent.
#
# 7. If the command is "discard x", remove element x using
#    S.discard(x). It does nothing if x is absent.
#
# 8. After executing all the commands, calculate the sum
#    of the remaining elements using sum(S).
#
# 9. Print the sum of the elements of the set on a single line.
#
# ============================================================

# ======================= Solution ===========================
n = int(input())
s = set(map(int,input().split()))

N = int(input())

for _ in range(N):
    command = input().split()   

    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))
