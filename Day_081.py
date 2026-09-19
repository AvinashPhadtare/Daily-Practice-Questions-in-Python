# ========================= Question =========================
# You are given a string svg.
#
# It contains alphanumeric characters, spaces and the symbols
# '+' and '-'.
#
# Find all substrings that:
#
# 1. Contain only vowels.
# 2. Contain at least 2 vowels.
# 3. Are surrounded by consonants.
#
# Vowels:
# AEIOU and aeiou
#
# Consonants:
# QWRTYPSDFGHJKLZXCVBNM
# qwrtypsdfghjklzxcvbnm
#
# Print all matching substrings in their order of occurrence.
#
# If there are no matches, print -1.
#
# Example:
#
# Input:
# rabcdeefgyYhFjkIoomnpOeorteeeeet
#
# Output:
# ee
# Ioo
# Oeo
# eeeee
# ============================================================
# Pattern explanation:
#
# (?<=[consonants])
#     The character immediately before the match
#     must be a consonant.
#
# [aeiouAEIOU]{2,}
#     Match only vowels.
#     {2,} means at least 2 vowels.
#
# (?=[consonants])
#     The character immediately after the match
#     must be a consonant.
#
# Lookbehind and lookahead make sure that the
# surrounding consonants are NOT included in the match.

# Solution:-
import re

string = input()
pattern = (
    r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
    r'[aeiouAEIOU]{2,}'
    r'(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
)
matches = re.findall(pattern, string)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)
