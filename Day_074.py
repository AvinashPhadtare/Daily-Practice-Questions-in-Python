# ========================== Question ==========================
# Write a Python program to check whether a given string contains:
#
# - At least one alphanumeric character
# - At least one alphabetical character
# - At least one digit
# - At least one lowercase character
# - At least one uppercase character
#
# The program should check each character of the string.
# If at least one character satisfies the condition, print True.
# Otherwise, print False.
#
# Example:
# Input:
# qA2
#
# Output:
# True
# True
# True
# True
# True
# ==============================================================


# Solution:-
def check_string(string):
    has_alnum = any(char.isalnum() for char in string)
    has_alpha = any(char.isalpha() for char in string)
    has_digit = any(char.isdigit() for char in string)
    has_lower = any(char.islower() for char in string)
    has_upper = any(char.isupper() for char in string)
    return has_alnum, has_alpha, has_digit, has_lower, has_upper


if __name__ == '__main__':
    string = input().strip()
    result = check_string(string)

    for value in result:
        print(value)
