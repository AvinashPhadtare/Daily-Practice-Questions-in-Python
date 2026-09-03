# ============================================================
# Question:
# Given a dictionary containing student names as keys and
# their marks as values, find the average marks of the
# student whose name is provided as the query.
#
# Print the average correct to 2 decimal places.
#
# Example:
# Input:
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
#
# Output:
# 56.00
# ============================================================


# Read the number of students
n = int(input())

# Create an empty dictionary
# Key   -> student name
# Value -> list of marks
student_marks = {}

# Read information for each student
for _ in range(n):

    # Read the complete line and split it into values
    # Example:
    # "Malika 52 56 60"
    #
    # name = "Malika"
    # line = ["52", "56", "60"]
    name, *line = input().split()

    # Convert all marks from strings to floating-point numbers
    # Example:
    # ["52", "56", "60"]
    # becomes
    # [52.0, 56.0, 60.0]
    scores = list(map(float, line))

    # Store the student's name and marks in the dictionary
    student_marks[name] = scores


# Read the name of the student whose average we need
query_name = input()

# Get the marks of the requested student
marks = student_marks[query_name]

# Calculate the average
# Average = total marks / number of marks
average = sum(marks) / len(marks)

# Print the average with exactly 2 digits after the decimal
print(f"{average:.2f}")
