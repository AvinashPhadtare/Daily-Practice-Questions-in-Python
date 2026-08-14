# ========================= Question ========================
# Write a Python program using the csv module to manage gym members.
#
# Each member has:
# - id
# - name
# - plan
# - active
#
# Build the following functions:
#
# 1. write_members_to_csv(members, filepath)
#    - Write the list of member dictionaries to a CSV file.
#    - The CSV file must contain a header row.
#    - Each member should be written as one row.
#
# 2. read_members_from_csv(filepath) -> list
#    - Read the member data from the CSV file.
#    - Return the data as a list of dictionaries.
#    - Convert id back to an integer.
#    - Convert active back to a Boolean value.
#
# 3. If the specified CSV file does not exist,
#    return an empty list instead of raising an error.
#
# Constraints:
# - Use only Python's built-in csv module.
# - Do NOT use pandas.
# ============================================================


# Solution:-
import csv


def write_members_to_csv(members, filepath):
    with open(filepath, "w", newline="") as file:
        fieldnames = members[0].keys()

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(members)


def read_members_from_csv(filepath):
    try:
        with open(filepath, "r", newline="") as file:
            reader = csv.DictReader(file)

            members = []

            for row in reader:
                row["id"] = int(row["id"])
                row["active"] = row["active"] == "True"

                members.append(row)

            return members

    except FileNotFoundError:
        return []


# Example Usage
members = [
    {"id": 1, "name": "Avinash", "plan": "premium", "active": True},
    {"id": 2, "name": "Rahul", "plan": "basic", "active": False},
]

write_members_to_csv(members, "members.csv")

print("Members read from CSV:")
print(read_members_from_csv("members.csv"))

print("\nReading missing file:")
print(read_members_from_csv("missing.csv"))
