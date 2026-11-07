# ========================= Question =========================
# You are given an integer N.
#
# Print the following values for every integer i from 1 to N:
#
# 1. Decimal representation
# 2. Octal representation
# 3. Hexadecimal representation (in capital letters)
# 4. Binary representation
#
# All four values must be printed on a single line.
#
# Each value must be right-aligned using spaces so that
# all values have the same width as the binary representation
# of N.
#
# The values must be separated by a single space.
#
# Example:
#
# Input:
# 5
#
# Output:
#  1  1  1  1
#  2  2  2 10
#  3  3  3 11
#  4  4  4 100
#  5  5  5 101
#
# Important Points:
#
# 1. Read an integer N.
#
# 2. Run a loop from 1 to N.
#
# 3. Convert each number into octal using oct().
#    Remove the first two characters, '0o'.
#
# 4. Convert each number into hexadecimal using hex().
#    Remove the first two characters, '0x'.
#
# 5. Convert hexadecimal letters to capital letters
#    using upper().
#
# 6. Convert each number into binary using bin().
#    Remove the first two characters, '0b'.
#
# 7. Use the binary representation of N to determine
#    the width required for formatting.
#
# 8. Right-align all four values to that width.
#
# 9. Print the values separated by a single space.
# ============================================================


# ======================= Solution ===========================
def print_formatted(number):
    # Find the width of the binary representation
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        # Convert number into different number systems
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(
            decimal.rjust(width),
            octal.rjust(width),
            hexadecimal.rjust(width),
            binary.rjust(width)
        )


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
