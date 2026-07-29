class Member:
    def __init__(self, id, name, join_date, total_paid):
        self.id = id
        self.name = name
        self.join_date = join_date
        self.total_paid = total_paid

    # Members are equal if their IDs are the same
    def __eq__(self, other):
        return self.id == other.id

    # Compare members based on total_paid
    def __lt__(self, other):
        return self.total_paid < other.total_paid

    # Clean string representation
    def __repr__(self):
        return (
            f"Member(id={self.id}, "
            f"name='{self.name}', "
            f"join_date='{self.join_date}', "
            f"total_paid={self.total_paid})"
        )



# Example Usage:-
# Create 5 members
members = [
    Member(101, "Rahul", "2023-06-15", 4500.0),
    Member(102, "Amit", "2022-12-10", 7200.0),
    Member(103, "Neha", "2024-01-20", 3800.0),
    Member(104, "Priya", "2023-03-05", 9100.0),
    Member(105, "Karan", "2022-08-18", 6000.0),
]

# Sort by total_paid
sorted_members = sorted(members)

print("Sorted by Total Paid:")
for member in sorted_members:
    print(member)

# Highest-paying member
print("\nHighest Paying Member:")
print(max(members))

# Earliest joining member
earliest_member = sorted(members, key=lambda m: m.join_date)[0]

print("\nEarliest Joining Member:")
print(earliest_member)
