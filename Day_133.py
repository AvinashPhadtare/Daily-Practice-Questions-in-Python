# ========================= Question =========================
#
# You are given N credit card numbers.
#
# Your task is to check whether each credit card number is
# valid or invalid.
#
# A valid credit card number must follow these rules:
#
# 1. It must start with 4, 5, or 6.
#
# 2. It must contain exactly 16 digits.
#
# 3. It must contain only digits from 0 to 9, except for
#    permitted hyphens.
#
# 4. It may be written as 16 continuous digits, or as four
#    groups of 4 digits separated by single hyphens (-).
#
# 5. It must NOT contain any other separators, such as
#    spaces or underscores.
#
# 6. It must NOT contain four or more consecutive
#    occurrences of the same digit.
#
# Example:
#
# Input:
# 6
# 4123456789123456
# 5123-4567-8912-3456
# 61234-567-8912-3456
# 4123356789123456
# 5133-3367-8912-3456
# 5123 - 3567 - 8912 - 3456
#
# Output:
# Valid
# Valid
# Invalid
# Valid
# Invalid
# Invalid
#
# Important Points:
#
# 1. Read the integer N.
#
# 2. Read N credit card numbers.
#
# 3. Check whether each number starts with 4, 5, or 6.
#
# 4. Check that the number contains exactly 16 digits.
#
# 5. Allow either continuous digits or correctly grouped
#    digits separated by hyphens.
#
# 6. Reject numbers containing four or more consecutive
#    repeated digits.
#
# 7. Print "Valid" if all conditions are satisfied.
#
# 8. Otherwise, print "Invalid".
#
# ============================================================

# ======================= Solution ===========================
import re

N = int(input())

for _ in range(N):
    card = input().strip()

    valid_format = re.fullmatch(
        r'(?:[456][0-9]{15}|[456][0-9]{3}(?:-[0-9]{4}){3})',
        card
    )

    digits_only = card.replace("-","")


    has_repeated_digits = re.search(
        r'([0-9])\1{3,}',
        digits_only
    )


    if valid_format and not has_repeated_digits:
        print("Valid")
    else:
        print("Invalid")
