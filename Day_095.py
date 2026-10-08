# ========================= Question =========================
# You are given an integer, size. Your task is to print an
# alphabet rangoli of size size.
#
# Rangoli is a form of Indian folk art based on creation of patterns.
#
# Example:
#
# Input:
# 5
#
# Output:
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
#
# The center of the rangoli has the first alphabet letter 'a',
# and the boundary has the alphabet letter according to the size.
#
# Function Description:
#
# Complete the rangoli function.
#
# rangoli has the following parameter:
# int size: the size of the rangoli
#
# Returns:
# string: a single string made up of each line of the rangoli
# separated by a newline character (\n)
#
# Input Format:
# Only one line of input containing the size of the rangoli.
#
# ============================================================


# ========================= Solution =========================
import string

def rangoli(size: int) -> str:

    # Get lowercase alphabets
    alphabets = string.ascii_lowercase

    # Store all lines of the rangoli
    lines = []

    # Total width of each line
    width = 4 * size - 3

    # Create the upper half including the center
    for i in range(size):
        start = size - 1

        left = alphabets[start:start - i - 1:-1]
      
        right = left[-2::-1]
      
        pattern = '-'.join(left + right)

        pattern = pattern.center(width, '-')
      
        lines.append(pattern)

    lines += lines[-2::-1]

    return '\n'.join(lines)


# ========================= Example Usage =========================

size = int(input())


# Generate the rangoli
result = rangoli(size)
print(result)
