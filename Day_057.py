# ========================= Question ========================
#
# Consider the following:
#
# - A string, s, of length n where s = c_0 c_1 ... c_{n-1}.
# - An integer, k, where k is a factor of n.
#
# We can split s into n/k substrings where each substring, t_i, consists of
# a contiguous block of k characters in s. Then, use each t_i to create
# string u_i such that:
#
# - The characters in u_i are a subsequence of the characters in t_i.
# - Any repeat occurrence of a character is removed from the string
#   such that each character in u_i occurs exactly once. In other
#   words, if the character at some index j in t_i occurs at a previous
#   index < j in t_i, then do not include the character in string u_i.
#
# Given s and k, print n/k lines where each line i denotes string u_i.
#
# Example:
# s = 'AAABCADDE'
# k = 3
#
# There are three substrings of length 3 to consider: 'AAA', 'BCA' and
# 'DDE'. The first substring is all 'A' characters, so u_1 = 'A'. The
# second substring has all distinct characters, so u_2 = 'BCA'. The
# third substring has 2 different characters, so u_3 = 'DE'.
#
# Function Description:
# Complete the merge_the_tools function below.
#
# merge_the_tools has the following parameters:
# - string s: the string to analyze
# - int k: the size of substrings to analyze
#
# Prints:
# Print each subsequence on a new line. There will be n/k of them.
# No return value is expected.
#
# ============================================================


# ------------------------------------------------------------
# Function: Split string into chunks of k and deduplicate
# ------------------------------------------------------------
def merge_the_tools(string: str, k: int) -> None:
    # Calculate the total length of the string
    n = len(string)

    # Loop through the string with a step size of k
    # to slice s into n / k substrings of length k
    for i in range(0, n, k):

        # Extract the contiguous substring t_i of length k
        t_i = string[i : i + k]

        # Use a set to track already seen characters for O(1) lookups
        seen = set()

        # List to maintain the order of first occurrence for characters
        u_i = []

        # Iterate over each character in substring t_i
        for char in t_i:

            # If the character has not been processed yet
            if char not in seen:
                # Add it to the set to prevent duplicate inclusion
                seen.add(char)
                # Append to the output list to keep the relative order
                u_i.append(char)

        # Print the processed string u_i for the current block
        print("".join(u_i))


# ------------------------------------------------------------
# Example usage
# ------------------------------------------------------------
if __name__ == "__main__":

    # Sample input values
    sample_string = "AABCAAADA"
    sample_k = 3

    # Call the function
    merge_the_tools(sample_string, sample_k)
