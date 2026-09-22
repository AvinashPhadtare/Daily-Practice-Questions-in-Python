# ========================= Question ========================
# Write a generator function member_ids(start: int) that produces
# an infinite sequence of member IDs starting from start.
#
# Then write a generator function members_by_plan(...) that wraps
# the ID generator and yields only IDs whose plan, looked up in
# a dictionary, matches the given plan.
#
# Use itertools.islice or a manual counter to safely take only
# the first 10 values from an infinite generator.
#
# =============================================================

from itertools import islice


# Produce infinite member IDs
def member_ids(start: int):
    while True:
        yield start
        start += 1


# Filter IDs according to member plan
def members_by_plan(id_generator, members, plan: str):
    for member_id in id_generator:
        if member_id not in members:
            continue
          
        if members[member_id]["plan"] == plan:
            yield member_id


# Example member data
members = {
    100: {"name": "Avinash", "plan": "gold"},
    101: {"name": "Rahul", "plan": "basic"},
    102: {"name": "Sneha", "plan": "gold"},
    103: {"name": "Amit", "plan": "premium"},
    104: {"name": "Priya", "plan": "gold"},
    105: {"name": "Rohan", "plan": "basic"},
    106: {"name": "Neha", "plan": "gold"},
    107: {"name": "Vikas", "plan": "premium"},
    108: {"name": "Pooja", "plan": "gold"},
    109: {"name": "Karan", "plan": "basic"},
    110: {"name": "Anjali", "plan": "gold"},
}


# infinite ID generator
id_gen = member_ids(100)

# filtered generator for gold members
gold_members = members_by_plan(id_gen, members, "gold")

# only the first 10 matching IDs
first_10 = list(islice(gold_members, 10))

print(first_10)
