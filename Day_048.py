# ================================================================
#                         QUESTION
# ================================================================
#
# You have a large CSV file containing payment records.
# The file may contain 1 million or more records, so you must NOT
# load the entire file into memory at once.
#
# Create a generator function:
#
#     stream_payments(filepath: str)
#
# It should read the CSV file one row at a time and yield one
# payment dictionary at a time.
#
# Using this generator, implement:
#
# 1. total_revenue(filepath)
#    - Return the total of all payment amounts.
#    - Do not load the entire file into memory.
#
# 2. revenue_by_plan(filepath)
#    - Group total revenue by plan type.
#    - Stream through the file only once.
#
# 3. large_payments(filepath, threshold)
#    - Return a list containing only payments whose amount is
#      greater than the given threshold.
#
# The solution should work efficiently even for very large CSV files.
# ================================================================

import csv


# ================================================================
# Generator Function
# ================================================================

def stream_payments(filepath: str):
    """
    Read the CSV file one row at a time.

    Instead of loading the complete file into memory,
    yield one payment dictionary at a time.
    """

    with open(filepath, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            # Convert amount from string to float
            row["amount"] = float(row["amount"])

            # Send one payment to the caller
            yield row


# ================================================================
# 1. Calculate Total Revenue
# ================================================================

def total_revenue(filepath: str) -> float:
    """
    Calculate total revenue without loading
    the complete CSV file into memory.
    """

    total = 0.0

    # Generator gives us one payment at a time
    for payment in stream_payments(filepath):

        total += payment["amount"]

    return total


# ================================================================
# 2. Calculate Revenue By Plan
# ================================================================

def revenue_by_plan(filepath: str) -> dict:
    """
    Calculate total revenue for each plan.

    Example:
        {
            "Basic": 3000.0,
            "Premium": 7500.0
        }
    """

    revenue = {}

    # Stream through the file only once
    for payment in stream_payments(filepath):

        plan = payment["plan"]
        amount = payment["amount"]

        # If plan does not exist, start from 0
        if plan not in revenue:
            revenue[plan] = 0.0

        revenue[plan] += amount

    return revenue


# ================================================================
# 3. Find Large Payments
# ================================================================

def large_payments(filepath: str, threshold: float) -> list:
    """
    Return only payments whose amount is greater
    than the given threshold.
    """

    result = []

    for payment in stream_payments(filepath):

        if payment["amount"] > threshold:
            result.append(payment)

    return result


# ================================================================
# Example Usage
# ================================================================

file_path = "payments.csv"

print("Total Revenue:")
print(total_revenue(file_path))

print("\nRevenue By Plan:")
print(revenue_by_plan(file_path))

print("\nLarge Payments:")
print(large_payments(file_path, 10000))
