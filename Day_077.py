# ========================= Question =========================
# Given a string containing lowercase English letters,
# find the three most common characters.
#
# Rules:
# 1. Sort characters by occurrence count in descending order.
# 2. If two characters have the same count,
#    sort them alphabetically.
#
# Print the top three characters and their counts.
# =============================================================


# Solution:-

s = input()

count = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

sorted_chars = sorted(count.items(),key=lambda x: (-x[1], x[0])) 

for char, frequency in sorted_chars[:3]:
    print(char,frequency)
