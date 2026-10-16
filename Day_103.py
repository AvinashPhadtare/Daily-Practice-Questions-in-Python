# ========================= Question =========================
#
# You are given a list of lowercase words.
#
# The vowels are:
# a, e, i, o, u, y
#
# Your task is to debug the function score_words(words) so that
# it calculates the correct total score for all the words.
#
# Scoring Rules:
#
# 1. Count the number of vowels in each word.
#
# 2. If the number of vowels is EVEN, the word gets 2 points.
#
# 3. If the number of vowels is ODD, the word gets 1 point.
#
# 4. Add the scores of all words and return the total score.
#
# Sample Input 0:
# 2
# hacker book
#
# Sample Output 0:
# 4
#
# Explanation:
#
# 1. hacker contains 2 vowels (a, e).
#    Since 2 is even, it gets 2 points.
#
# 2. book contains 2 vowels (o, o).
#    Since 2 is even, it gets 2 points.
#
# Total score = 2 + 2 = 4
#
# Sample Input 1:
# 3
# programming is awesome
#
# Sample Output 1:
# 4
#
# Important Points:
#
# 1. Use is_vowel(letter) to check whether a letter is a vowel.
#
# 2. Count the vowels in each word using a loop.
#
# 3. Use num_vowels % 2 == 0 to check whether the count is even.
#
# 4. Add 2 points for an even number of vowels.
#
# 5. Add 1 point for an odd number of vowels.
#
# 6. Return the total score.
#
# ============================================================


# ======================= Solution ===========================
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    score = 0

    for word in words:
        num_vowels = 0

        for letter in word:
            if is_vowel(letter):
                num_vowels += 1

        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1

    return score


n = int(input())
words = input().split()

print(score_words(words))
