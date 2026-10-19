# ========================= Question =========================
#
# You are given an unordered list of room numbers from an
# infinite hotel.
#
# The hotel has:
# - One Captain who stays in a separate room.
# - A number of families, each consisting of K members.
#
# Each family is assigned one room, while the Captain gets
# a separate room.
#
# The room number of each family appears exactly K times
# in the list, while the Captain's room number appears only
# once.
#
# Your task is to find the Captain's room number.
#
# The total number of tourists and the number of families
# are unknown. You only know K and the list of room numbers.
#
# Example:
#
# Input:
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
#
# Output:
# 8
#
# Important Points:
#
# 1. Read an integer K representing the number of members
#    in each family.
#
# 2. Read the space-separated room numbers and store them
#    in a list.
#
# 3. Each family room number appears exactly K times.
#
# 4. The Captain's room number appears only once.
#
# 5. Use a set or another suitable approach to identify
#    the room number that does not repeat K times.
#
# 6. Print the Captain's room number on a single line.
#
# ============================================================

# ======================= Solution ===========================
k = int(input())
room_numbers = list(map(int, input().split()))

rooms = set(room_numbers)

captain_room = (sum(rooms) * k - sum(room_numbers)) // (k - 1)

print(captain_room)
