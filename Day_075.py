# ========================= Question =========================
# You are given n words. Some words may repeat.
# For each distinct word, output its number of occurrences.
#
# The output order must be the order in which each word
# first appeared in the input.
#
# Output:
# 1. Number of distinct words
# 2. Frequency of each distinct word
# =============================================================

# Solution:-
n = int(input())
counts = {}

for _ in range(n):
    word = input()
    if word in counts:
        counts[word] += 1
    else:
        counts = 1

print(len(counts))
print(*counts.values())
