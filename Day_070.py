# ========================= Question =========================
#
# You are given a string containing space-separated words.
#
# Your task is to:
#
# 1. Split the string using a space " " as the delimiter.
# 2. Join the resulting words using a "-" hyphen.
#
# Example:
#
# Input:
# this is a string
#
# After split():
# ["this", "is", "a", "string"]
#
# After join("-"):
# this-is-a-string
#
# The function should return:
# this-is-a-string
#
# =============================================================

# Solution:-
def split_and_join(line):
    words = line.split(" ")
    result = "-".join(words)
    return result


# Read the input string
line = input()
print(split_and_join(line))
