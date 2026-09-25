# ========================= Question ========================
# Mental Model:
# An iterator class gives you full control over iteration.
# Implement __iter__() (returns self) and __next__()
# (returns next value or raises StopIteration).
#
# Use a class-based iterator when you need stateful iteration —
# when knowing where you are depends on complex state that a
# simple generator can't express.
#
# Problem:
# Build a DateRangeIterator class that iterates over dates
# from a start date to an end date (inclusive), one day at a time.
#
# Example:
# DateRangeIterator("2025-01-01", "2025-01-07")
#
# Output:
# 2025-01-01
# 2025-01-02
# 2025-01-03
# 2025-01-04
# 2025-01-05
# 2025-01-06
# 2025-01-07
#
# Requirements:
# - Use datetime.date
# - Use timedelta
# - Implement proper __iter__() and __next__()
# - The end date must be included.
# - Raise StopIteration when the range is finished.
#
# Then use the iterator to generate a weekly attendance
# report template.
#
# For each date, produce:
#
# {
#     "date": "2025-01-01",
#     "expected_members": 0,
#     "actual": 0
# }
#
# ============================================================

# Solution: 

from datetime import timedelta, date


class DateRangeIterator:
    def __init__(self,start_date,end_date):
        self.start_date = date.fromisoformat(start_date)
        self.end_date = date.fromisoformat(end_date)
        self.current_date = self.start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_date > self.end_date:
            raise StopIteration
        result = self.current_date

        self.current_date += timedelta(days=1)

        return result


date_iterator = DateRangeIterator("2025-01-01", "2025-01-07")

for current_date in date_iterator:
    print(current_date)


date_iterator = DateRangeIterator("2025-01-01", "2025-01-07")

attendance_report = []

for current_date in date_iterator:
    record = {
        "date": current_date.isoformat(),
        "expected_members": 0,
        "actual": 0
    }

    attendance_report.append(record)


print("\nAttendance Report:")

for record in attendance_report:
    print(record)
