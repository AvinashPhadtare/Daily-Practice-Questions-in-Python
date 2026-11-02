# ========================= Question =========================
#
# You are given a list of N integers.
#
# Find the second largest DISTINCT number in the list.
#
# If there are fewer than two distinct numbers,
# print "Not Possible".
#
# Example:
#
# Input:
# 6
# 4 1 7 7 5 8
#
# Output:
# 7
#
# Important Points:
#
# 1. Read N and the list of integers.
# 2. Convert the list into a set to remove duplicates.
# 3. Convert the set back into a list.
# 4. Sort the list in ascending order.
# 5. Check if at least two distinct numbers exist.
# 6. If yes, print the second largest using [-2].
# 7. Otherwise, print "Not Possible".
#
# ============================================================


# ======================= Solution ===========================
def find_second_largest(arr):
    unique_numbers = list(set(arr))
    unique_numbers.sort()

    if len(unique_numbers) < 2:
        print("Not Possible")
    else:
        print(unique_numbers[-2])


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    find_second_largest(arr)
