# ======================== Question =========================
# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules:
# - Both players are given the same string S.
# - Both players have to make substrings using the letters of S.
# - Stuart has to make words starting with consonants.
# - Kevin has to make words starting with vowels.
# - The game ends when both players have made all possible substrings.

# Scoring:
# - A player gets +1 point for each occurrence of the substring in S.

# Example:
# String S = BANANA
# Kevin's vowel beginning word = ANA
# ANA occurs twice in BANANA, so Kevin gets 2 points.

# Print:
# - "Kevin <score>" if Kevin wins.
# - "Stuart <score>" if Stuart wins.
# - "Draw" if both scores are equal.

# Note:
# - Vowels are only A, E, I, O, U.
# - Y is not considered a vowel.
# ==========================================================================


# Solution:
def minion_game(s):

    kevin = 0
    stuart = 0

    for i in range(len(s)):

        # Number of substrings that can start from index i
        point = len(s) - i

        # If character is a vowel, Kevin gets the points
        if s[i] in "AEIOU":
            kevin += point

        # Otherwise, the character is a consonant
        # and Stuart gets the points
        else:
            stuart += point

    # Check who has the higher score
    if kevin > stuart:
        print(f"Kevin {kevin}")

    elif kevin == stuart:
        print("Draw")

    else:
        print(f"Stuart {stuart}")



s = input("Enter a String: ")
minion_game(s)


# ====================== Example Usage ======================
#Example:
# Input:
# BANANA

# Output:
# Stuart 12

# Another Example:

# Input:
# BAANANAS
#
# Output:
# Kevin 19
# ============================================================
