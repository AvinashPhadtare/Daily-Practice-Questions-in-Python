# ========================= Question =========================
#
# You are given information about N people. Each person has
# a first name, last name, age, and sex.
#
# Your task is to print their names in a specific format,
# sorted by age in ascending order.
#
# The youngest person's name should be printed first.
#
# If two people have the same age, print them in the order
# in which they appeared in the input.
#
# Example:
#
# Input:
# 3
# Mike Thomson 20 M
# Robert Bustle 32 M
# Andria Bustle 30 F
#
# Output:
# Mr. Mike Thomson
# Ms. Andria Bustle
# Mr. Robert Bustle
#
# Important Points:
#
# 1. Read the integer N, representing the number of people.
#
# 2. Read the first name, last name, age, and sex of each
#    person.
#
# 3. Use a decorator to modify the name-printing function.
#
# 4. If the sex is 'M', add 'Mr.' before the person's name.
#
# 5. If the sex is 'F', add 'Ms.' before the person's name.
#
# 6. Sort the people by age in ascending order.
#
# 7. Preserve the input order for people with the same age.
#
# 8. Print each formatted name on a separate line.
#
# ============================================================


# ======================= Solution ===========================
def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        return [f(person) for person in people]
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for _ in range(int(input()))]
    print(*name_format(people), sep='\n')
