# ========================= Question ========================
# Mental Model:
# `itertools` provides powerful iterator-based tools for working
# with collections without manually implementing common iteration
# patterns.
#
# The key idea is that `itertools` functions are lazy — they
# produce values on demand.
#
# Problem:
# Use ONLY `itertools` functions (no manual loops where an
# `itertools` function can do the job) to manage gym members.
#
# Given:
#
# Each member has:
# - id
# - name
# - plan
# - city
#
# Requirements:
#
# 1. Group members by city using `itertools.groupby()`.
#    - What must you do before using `groupby()`?
#    - Sort the members by `city` first because `groupby()`
#      groups consecutive equal values.
#
# 2. Generate all pairs of members who could share a training
#    slot using `itertools.combinations()`.
#    - Each pair must contain two different members.
#    - Do not generate duplicate/reversed pairs.
#
# 3. Create a weekly training schedule using `itertools.product()`.
#    - Generate every member × every day-of-week combination.
#
# 4. Chain members from two different branches into one stream
#    using `itertools.chain()`.
#    - Separate the Pune members and Mumbai members.
#    - Combine both groups into one iterator.
#
# ============================================================


# Solution:-
from itertools import groupby, combinations, product, chain


# Group members by city
def grouped_city(members: list):
    # groupby() works correctly when members are sorted by the grouping key
    sorted_members = sorted(members, key=lambda member: member["city"])

    return groupby(sorted_members, key=lambda member: member["city"])


# Generate all possible pairs of members
def combination_of_members(members: list):
    return combinations(members, 2)


# Create a schedule for every member and every day
def schedule(members: list):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    return product(members, days)


# Chain members from Pune and Mumbai into one stream
def chain_of_members(members: list):
    pune_members = []
    mumbai_members = []

    # Separate members based on their city
    for member in members:
        if member["city"] == "Pune":
            pune_members.append(member)

        if member["city"] == "Mumbai":
            mumbai_members.append(member)

    return chain(pune_members, mumbai_members)



# ========================= Usage =========================
members = [
    {"id": 1, "name": "Avinash", "plan": "premium", "city": "Pune"},
    {"id": 2, "name": "Rahul", "plan": "basic", "city": "Mumbai"},
    {"id": 3, "name": "Priya", "plan": "premium", "city": "Pune"},
    {"id": 4, "name": "Sneha", "plan": "vip", "city": "Pune"},
    {"id": 5, "name": "Raj", "plan": "basic", "city": "Mumbai"},
]


# 1. Group members by city
groups = grouped_city(members)

for city, members_group in groups:
    print(city, list(members_group))


# 2. Generate pairs of members
pairs = combination_of_members(members)

for member1, member2 in pairs:
    print(member1["name"], "and", member2["name"])


# 3. Create member × day schedule
schedule_of_members = schedule(members)

for member, day in schedule_of_members:
    print(member["name"], "and", day)


# 4. Chain Pune and Mumbai members
combined_members = chain_of_members(members)

for member in combined_members:
    print(member)
