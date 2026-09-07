# ========================= Question =========================
#
# You are given the first name and last name of a person
# on two different lines.
#
# Complete the print_full_name() function.
#
# The function accepts:
# 1. first - the first name as a string
# 2. last  - the last name as a string
#
# Print the following message:
#
# Hello firstname lastname! You just delved into python.
#
# Example:
#
# Input:
# Ross
# Taylor
#
# Output:
# Hello Ross Taylor! You just delved into python.
#
# =============================================================


# Solution:-
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.") 

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
