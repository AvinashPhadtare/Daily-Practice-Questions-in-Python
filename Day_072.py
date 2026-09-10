# ========================== Question ==========================
# Write a Python program to count how many times a substring
# occurs in a given string.
#
# - Traverse the string from left to right.
# - The comparison is case-sensitive.
# - Overlapping occurrences must also be counted.
#
# Example:
# Input:
# ABCDCDC
# CDC
#
# Output:
# 2
# ==============================================================

# Solution:-
def count_substring(string, sub_string):

    count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
