# =============================================================================
# Problem: Maximum Check-ins in Every Sliding Window
#
# A gym records the number of member check-ins every hour.
#
# Example:
# counts = [5, 3, 8, 7, 2, 9, 1, 4, 6, 3, 7, 8, 2, 5, 9, 1, 3, 6, 4, 7, 2, 8, 5, 3]
#
# You are given:
#   1. A list 'counts' containing hourly check-in counts.
#   2. An integer 'k' representing the size of the sliding window.
#
# Write a function:
#
#     max_checkins_window(counts: list, k: int) -> list
#
# that returns the maximum check-in count for every contiguous window of
# size k.
#
# Example:
#
# counts = [5, 3, 8, 7, 2]
# k = 3
#
# Windows:
# [5, 3, 8] -> 8
# [3, 8, 7] -> 8
# [8, 7, 2] -> 8
#
# Output:
# [8, 8, 8]
#
# Requirements:
# 1. First solve using the naive O(n*k) approach.
# 2. Then solve efficiently using collections.deque in O(n).
# 3. Compare the time complexities of both approaches.
# =============================================================================


# =============================================================================
# Solution 1 : Naive Approach (O(n*k))
# =============================================================================

def max_checkins_window_naive(counts, k):
    result = []

    # Iterate through every possible window
    for i in range(len(counts) - k + 1):

        # Find maximum of current window
        window_max = max(counts[i:i+k])

        result.append(window_max)

    return result


# Example
counts = [5, 3, 8, 7, 2]
print(max_checkins_window_naive(counts, 3))
# Output: [8, 8, 8]


# =============================================================================
# Solution 2 : Optimized Approach using Deque (O(n))
# =============================================================================

from collections import deque

def max_checkins_window(counts, k):

    dq = deque()      # Stores indexes
    result = []

    for i in range(len(counts)):

        # -----------------------------------------------------------
        # Remove indexes that are outside the current window
        # -----------------------------------------------------------
        while dq and dq[0] <= i - k:
            dq.popleft()

        # -----------------------------------------------------------
        # Remove smaller elements from the back because they can never
        # become the maximum while the current larger element exists.
        # -----------------------------------------------------------
        while dq and counts[dq[-1]] < counts[i]:
            dq.pop()

        # Add current index
        dq.append(i)

        # -----------------------------------------------------------
        # Once the first complete window is formed,
        # the front of deque always stores the maximum element.
        # -----------------------------------------------------------
        if i >= k - 1:
            result.append(counts[dq[0]])

    return result


# Example
counts = [5, 3, 8, 7, 2]
print(max_checkins_window(counts, 3))
# Output: [8, 8, 8]


# =============================================================================
# Time Complexity Comparison
#
# Naive Approach:
# Time  : O(n*k)
# Space : O(1)
#
# Deque Approach:
# Time  : O(n)
# Space : O(k)
#
# The deque solution is faster because every element is inserted and
# removed at most once.
# =============================================================================
