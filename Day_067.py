# ======================== Question ========================
# You are given a string and your task is to swap its cases.
#
# In other words:
# - Convert all lowercase letters to uppercase.
# - Convert all uppercase letters to lowercase.
# - Numbers, spaces, and special characters should remain unchanged.
#
# Example:
#
# Input:
# HackerRank.com presents "Pythonist 2":
#
# Output:
# hACKERrANK.COM PRESENTS "pYTHONIST 2":
#
# ------------------------------------------------------------

# Solution:-

def swap_case(s: str):
    result = ""

    for char in s:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()

    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
