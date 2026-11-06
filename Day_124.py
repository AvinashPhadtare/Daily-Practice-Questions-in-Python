# ========================= Question =========================
# You are given an integer N.
#
# For every integer i from 1 to N, print:
#
# 1. The number i.
# 2. The sum of its digits.
# 3. The product of its digits.
#
# Example:
#
# Input:
# 12
#
# Output:
# 1 1 1
# 2 2 2
# 3 3 3
# 4 4 4
# 5 5 5
# 6 6 6
# 7 7 7
# 8 8 8
# 9 9 9
# 10 1 0
# 11 2 1
# 12 3 2
#
# Important Points:
#
# 1. Read an integer N.
#
# 2. Use a for loop from 1 to N.
#
# 3. Store the current number in a temporary variable.
#
# 4. Initialize the sum of digits to 0.
#
# 5. Initialize the product of digits to 1.
#
# 6. Use a while loop to process each digit.
#
# 7. Use % 10 to get the last digit.
#
# 8. Use // 10 to remove the last digit.
#
# 9. Add each digit to the sum.
#
# 10. Multiply each digit to calculate the product.
#
# 11. Print the number, sum and product on one line.
#
# 12. Complete the calculate_digits(number) function.
#
# ============================================================


# ======================= Solution ===========================
def calculate_digits(number):
    for i in range(1, number + 1):
        temp = i

        digit_sum = 0
        digit_product = 1

        while temp > 0:
            digit = temp % 10

            digit_sum += digit
            digit_product *= digit

            temp = temp // 10

        print(i, digit_sum, digit_product)


if __name__ == '__main__':
    n = int(input())
    calculate_digits(n)
