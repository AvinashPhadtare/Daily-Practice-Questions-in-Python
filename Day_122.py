# ========================= Question =========================
#
# You are given a sentence containing words separated by spaces.
#
# Count how many times each word appears.
#
# Treat uppercase and lowercase versions as the same word.
# Print the words in the order in which they first appear.
#
# Example:
#
# Input:
# red blue red green blue red
#
# Output:
# red 3
# blue 2
# green 1
#
# Important Points:
#
# 1. Read the sentence.
# 2. Convert the sentence to lowercase.
# 3. Use split() to separate it into words.
# 4. Create an empty dictionary.
# 5. Visit each word.
# 6. If the word exists, increase its count by one.
# 7. Otherwise, add the word with a count of one.
# 8. Print each word and its frequency.
#
# ============================================================


# ======================= Solution ===========================
def count_words(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    for word, count in frequency.items():
        print(word, count)


if __name__ == '__main__':
    sentence = input()
    count_words(sentence)
