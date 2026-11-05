# ========================= Question =========================
#
# You are given a list of N integers.
#
# Remove duplicate elements while preserving the original
# order of the first occurrence of every element.
#
# Example:
#
# Input:
# 8
# 1 2 1 3 2 4 4 5
#
# Output:
# 1 2 3 4 5
#
# Important Points:
#
# 1. Read N and the list of integers.
# 2. Create an empty list for unique elements.
# 3. Create an empty set to track seen elements.
# 4. Visit each number in the original list.
# 5. If the number is not in the set, add it to both.
# 6. Skip numbers that have already appeared.
# 7. Print the unique list in its original order.
#
# ============================================================



# ======================= Solution ===========================
def remove_duplicates(arr):
    unique_numbers = []
    seen = set()

    for number in arr:
        if number not in seen:
            unique_numbers.append(number)
            seen.add(number)

    print(*unique_numbers)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    remove_duplicates(arr)
