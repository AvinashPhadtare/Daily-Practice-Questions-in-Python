# ========================= Question ========================
# Given the names and grades for each student in a class of N
# students, store them in a nested list and print the name(s)
# of any student(s) having the second lowest grade.
#
# If there are multiple students with the second lowest grade,
# order their names alphabetically and print each name on a
# new line.
#
# Input Format:
# - The first line contains an integer N, the number of students.
# - The next 2N lines contain the name and grade of each student.
# - The first line contains the student's name.
# - The second line contains the student's grade.
#
# Output Format:
# - Print the name(s) of student(s) having the second lowest
#   grade in alphabetical order.
#
# Example Input:
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
#
# Example Output:
# Berry
# Harry
#
# Explanation:
# The grades are:
# 37.21, 37.21, 37.2, 41, 39
#
# After removing duplicates and sorting:
# 37.2, 37.21, 39, 41
#
# Lowest grade = 37.2
# Second lowest grade = 37.21
#
# Harry and Berry have the second lowest grade.
# Alphabetically:
# Berry
# Harry
# ============================================================


# Solution: 
# Create an empty nested list
students = []

# Take the number of students
n = int(input())

# Take name and grade of each student
for i in range(n):
    name = input()
    grade = float(input())

    # Store name and grade as a nested list
    students.append([name, grade])

# Get all grades from the nested list
grades = [student[1] for student in students]

# Remove duplicate grades
grades = list(set(grades))

# Sort grades in ascending order
grades.sort()

# Get the second lowest grade
second_lowest = grades[1]

# Find names of students having second lowest grade
names = [student[0] for student in students
         if student[1] == second_lowest]

# Sort names alphabetically
names.sort()

# Print each name on a new line
for name in names:
    print(name)


# ========================= Example Usage ====================
#
# Input:
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
#
# Nested list created:
# [
#     ['Harry', 37.21],
#     ['Berry', 37.21],
#     ['Tina', 37.2],
#     ['Akriti', 41.0],
#     ['Harsh', 39.0]
# ]
#
# Unique sorted grades:
# [37.2, 37.21, 39.0, 41.0]
#
# Second lowest grade:
# 37.21
#
# Students having 37.21:
# Harry
# Berry
#
# Alphabetically sorted:
# Berry
# Harry
#
# Output:
# Berry
# Harry
# ============================================================
