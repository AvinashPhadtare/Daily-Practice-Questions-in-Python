# ========================== Question =========================
#
# You are given a date in the format DD-MM-YYYY.
#
# Your task is to print the name of the weekday on that date,
# followed by the number of days left in that year after this
# date (up to 31 December).
#
# Example:
#
# Input:
# 22-10-2026
#
# 22 October 2026 is a Thursday
# Days left = 9 (Oct) + 30 (Nov) + 31 (Dec) = 70
#
# Output:
# Thursday 70
#
# Important Point:
#
# Use datetime.strptime to read the date and strftime("%A") to
# get the weekday name. Subtracting two dates gives a timedelta,
# and its .days is the number of days.
#
# ============================================================

# ======================= Solution ==========================
from datetime import datetime, date

d = datetime.strptime(input().strip(), "%d-%m-%Y").date()
year_end = date(d.year, 12, 31)

print(d.strftime("%A"), (year_end - d).days)
