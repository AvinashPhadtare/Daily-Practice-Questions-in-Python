# ========================== Question =========================
#
# Write a decorator exclaim that adds "!" at the end of the
# string returned by a function.
#
# Apply it on a function greet(name) that returns
# "Hello, <name>". You are given N names. Your task is to print
# the greeting for each name.
#
# Example:
#
# Input:
# 3
# Raymond
# Steven
# Adrian
#
# Output:
# Hello, Raymond!
# Hello, Steven!
# Hello, Adrian!
#
# Important Point:
#
# A decorator takes a function, defines an inner wrapper that
# calls it and changes the result, and then returns the wrapper.
#
# ============================================================

# ======================= Solution ==========================
def exclaim(func):
    def wrapper(name):
        return func(name) + "!"
    return wrapper


@exclaim
def greet(name):
    return f"Hello, {name}"


n = int(input())

for _ in range(n):
    print(greet(input().strip()))
