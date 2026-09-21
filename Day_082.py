# ========================= Question =========================
# You are given two strings.
#
# The first string is the main string.
# The second string is the substring to search for.
#
# Find the start and end indices of EVERY occurrence
# of the substring inside the main string.
#
# Overlapping occurrences must also be considered.
#
# Print each occurrence as:
#
# (start_index, end_index)
#
# If no match is found, print:
#
# (-1, -1)
#
# Example:
#
# Input:
# aaadaa
# aa
#
# Output:
# (0, 1)
# (1, 2)
# (4, 5)
# ============================================================

# Solution:-
import re

string = input()
substring = input()

# Escape the substring so that special regex characters
# are treated as normal characters.
#
# Example:
# If substring is "a.b",
# re.escape() converts it to "a\.b"
#
# This is useful because the user gives us a normal string,
# not a regex pattern.
pattern = r'(?=(' + re.escape(substring) + r'))'

# finditer() gives us MatchObjects.
#
# The positive lookahead (?=...)
# allows overlapping matches to be found.
matches = re.finditer(pattern, string)


found = False

for match in matches:
    start_index = match.start(1)

    end_index = match.end(1) - 1
    print((start_index, end_index))
    found = True

if not found:
    print((-1, -1))
