# ============================= QUESTION ===================================
# Consider an empty list called my_list = [].
# You will be given N commands. Each command performs an operation
# on the list.

# The following 7 commands are supported:
#
# 1. insert i e
#    - Insert integer e at index/position i.
#
# 2. print
#    - Print the current list.
#
# 3. remove e
#    - Remove the first occurrence of integer e from the list.
#
# 4. append e
#    - Add integer e to the end of the list.
#
# 5. sort
#    - Sort the list in ascending order.
#
# 6. pop
#    - Remove the last element from the list.
#
# 7. reverse
#    - Reverse the order of elements in the list.
#
# Read the value of N followed by N commands.
# Execute every command in the given order.
#
# For every "print" command, print the current list.
#
# Example:
#
# Input:
# 4
# append 1
# append 2
# insert 1 3
# print
#
# Output:
# [1, 3, 2]
# ================================================================

# Solution:-

n = int(input())

my_list = []

for _ in range(n):
    c = input().split()

    if c[0] == "insert":
        my_list.insert(int(c[1]), int(c[2]))

    elif c[0] == "append":
        my_list.append(int(c[1]))

    elif c[0] == "remove":
        my_list.remove(int(c[1]))

    elif c[0] == "sort":
        my_list.sort()

    elif c[0] == "pop":
        my_list.pop()

    elif c[0] == "print":
        print(my_list)

    elif c[0] == "reverse":
        my_list.reverse()


# Optimized code solution:- 
n = int(input())

my_list = []

def insert(c):
    my_list.insert(int(c[1]), int(c[2]))

def append(c):
    my_list.append(int(c[1]))

def remove(c):
    my_list.remove(int(c[1]))

def sort(c):
    my_list.sort()

def pop(c):
    my_list.pop()

def print_list(c):
    print(my_list)

def reverse(c):
    my_list.reverse()


operations = {
    "insert": insert,
    "append": append,
    "remove": remove,
    "sort": sort,
    "pop": pop,
    "print": print_list,
    "reverse": reverse
}

for _ in range(n):
    c = input().split()
    operations[c[0]](c)
