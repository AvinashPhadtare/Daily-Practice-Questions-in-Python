# ========================= Question ========================
# Given the participants' score sheet for a University Sports Day,
# you are given n scores.
#
# Store the scores in a list and find the runner-up score.
#
# The runner-up score is the second highest unique score.
#
# Input Format:
# - The first line contains an integer n.
# - The second line contains n integers separated by spaces.
#
# Constraints:
# - 2 <= n <= 10
# - -100 <= score <= 100
#
# Output Format:
# - Print the runner-up score.
#
# Example:
# Input:
# 5
# 2 3 6 6 5
#
# Output:
# 5
#
# Explanation:
# The highest score is 6.
# The next highest unique score is 5.
# Therefore, the runner-up score is 5.
# ============================================================

# Solution
if __name__ == '__main__':
    n = int(input())

    arr = map(int, input().split())

    # Remove duplicate scores
    arr = list(set(arr))

    # Sort scores in ascending order
    arr.sort()

    # Print the second highest score
    print(arr[-2])


# ========================= Example Usage ====================
#
# Input:
# 5
# 2 3 6 6 5
#
# Step 1: Original scores
# [2, 3, 6, 6, 5]
#
# Step 2: Remove duplicates
# [2, 3, 5, 6]
#
# Step 3: Sort the list
# [2, 3, 5, 6]
#
# Step 4: Get second highest using arr[-2]
# 5
#
# Output:
# 5
# ============================================================
