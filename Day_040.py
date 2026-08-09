# ============================================================
# QUESTION
# ============================================================
#
# You have a list of daily revenue numbers for your gym:
#
# revenues = [200, 450, 300, 750, 500, 150, 600, 250, 400, 350]
#
# Write the following functions:
#
# 1. two_days_target(revenues, target) -> tuple
#    Return the indices of two days whose revenues sum to target.
#    Return (-1, -1) if no such pair is found.
#    The solution should run in O(n) time.
#
# 2. find_days_above_average(revenues) -> list
#    Return the indices of days that earned above the average revenue.
#    Calculate the average first, then find the days above average
#    using a single pass.
#
# 3. running_total(revenues) -> list
#    Return a new list where each element is the sum of all revenues
#    up to and including that day.
#
# ============================================================
# SOLUTION
# ============================================================

revenues = [200, 450, 300, 750, 500, 150, 600, 250, 400, 350]


# Function 1: Find two days whose revenues add up to target
def two_days_target(revenues, target):

    # Dictionary to store:
    # revenue -> index
    seen = {}

    # Go through the list with both index and revenue
    for i, revenue in enumerate(revenues):

        # Find the revenue needed to reach the target
        needed = target - revenue

        # Check whether the needed revenue was already seen
        if needed in seen:

            # Return previous index and current index
            return (seen[needed], i)

        # Store the current revenue and its index
        seen[revenue] = i

    # Return this if no pair is found
    return (-1, -1)


# Function 2: Find days whose revenue is above average
def find_days_above_average(revenues):

    # Calculate the average revenue
    average = sum(revenues) / len(revenues)

    # List to store indices of days above average
    result = []

    # Check every revenue
    for i, revenue in enumerate(revenues):

        # If revenue is greater than average
        if revenue > average:

            # Store the index
            result.append(i)

    # Return the list of indices
    return result


# Function 3: Create running total of revenues
def running_total(revenues):

    # List to store running totals
    result = []

    # Starting total
    total = 0

    # Go through every revenue
    for revenue in revenues:

        # Add current revenue to total
        total += revenue

        # Store the updated total
        result.append(total)

    # Return the running totals
    return result


# ============================================================
# TESTING THE FUNCTIONS
# ============================================================

print(two_days_target(revenues, 950))

print(find_days_above_average(revenues))

print(running_total(revenues))
