import sys

# Normal class (without __slots__)
class AttendanceRecord:
    def __init__(self, member_id, date, status, checked_in_time):
        self.member_id = member_id
        self.date = date
        self.status = status
        self.checked_in_time = checked_in_time


# Class with __slots__
class AttendanceRecordSlotted:
    __slots__ = ("member_id", "date", "status", "checked_in_time")

    def __init__(self, member_id, date, status, checked_in_time):
        self.member_id = member_id
        self.date = date
        self.status = status
        self.checked_in_time = checked_in_time


NUM_OBJECTS = 10000

# Create objects
normal_records = [
    AttendanceRecord(i, "2026-07-31", "Present", "09:00")
    for i in range(NUM_OBJECTS)
]

slotted_records = [
    AttendanceRecordSlotted(i, "2026-07-31", "Present", "09:00")
    for i in range(NUM_OBJECTS)
]

# Measure memory
# Note: For normal objects, include the __dict__ size because
# the attributes are stored there.
normal_memory = sum(
    sys.getsizeof(obj) + sys.getsizeof(obj.__dict__)
    for obj in normal_records
)

# Slotted objects don't have a __dict__
slotted_memory = sum(sys.getsizeof(obj) for obj in slotted_records)

difference = normal_memory - slotted_memory
percentage_saved = (difference / normal_memory) * 100

print(f"Normal objects memory : {normal_memory} bytes")
print(f"Slotted objects memory: {slotted_memory} bytes")
print(f"Memory saved          : {difference} bytes")
print(f"Percentage saved      : {percentage_saved:.2f}%")
