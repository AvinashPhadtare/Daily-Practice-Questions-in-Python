# ========================== Question ==========================
# Write a Python program to modify a character in a string.
#
# Complete the mutate_string() function:
# - string: original string
# - position: index of character to change
# - character: new character
#
# Since strings are immutable, convert the string into a list,
# modify the character, and convert it back to a string.
#
# Example:
# Input:
# abracadabra
# 5 k
#
# Output:
# abrackdabra
# ==============================================================

# Solution:-
def mutate_string(string, position, character):
    new_list = list(string)
    new_list[position] = character
    string = ''.join(new_list)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
