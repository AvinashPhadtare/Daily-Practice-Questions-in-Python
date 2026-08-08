# Question:
# Design a data structure to represent your entire gym's data.
#
# Write these functions:
# 1. total_members(gym) -> int
# 2. members_by_city(gym, city) -> list
# 3. all_vip_members(gym) -> list
# 4. add_member(gym, branch_id, member_dict) -> mutate the structure


# Nested gym data structure
gym = {
    "name": "FitZone",
    "branches": [
        {
            "branch_id": 1,
            "city": "Pune",
            "members": [
                {"id": 101, "name": "Avinash", "plan": "premium"},
                {"id": 102, "name": "Rahul", "plan": "basic"},
            ]
        },
        {
            "branch_id": 2,
            "city": "Mumbai",
            "members": [
                {"id": 201, "name": "Priya", "plan": "vip"},
            ]
        }
    ]
}


# 1. Count total members across all branches
def total_members(gym):
    total = 0

    for branch in gym["branches"]:
        total += len(branch["members"])

    return total


# 2. Get members belonging to a particular city
def members_by_city(gym, city):
    for branch in gym["branches"]:
        if branch["city"] == city:
            return branch["members"]

    return []


# 3. Get all VIP members across all branches
def all_vip_members(gym):
    vip_members = []

    for branch in gym["branches"]:
        for member in branch["members"]:
            if member["plan"] == "vip":
                vip_members.append(member)

    return vip_members


# 4. Add a new member to a specific branch
def add_member(gym, branch_id, member_dict):
    for branch in gym["branches"]:
        if branch["branch_id"] == branch_id:
            branch["members"].append(member_dict)
            return True

    return False


# -------------------------
# Testing the functions
# -------------------------

# Total members
print("Total members:", total_members(gym))


# Members in Pune
print("Pune members:", members_by_city(gym, "Pune"))


# All VIP members
print("VIP members:", all_vip_members(gym))


# Add a new member to Pune branch
new_member = {
    "id": 103,
    "name": "Sneha",
    "plan": "premium"
}

print("Member added:", add_member(gym, 1, new_member))


# Check total members after adding
print("Total members after adding:", total_members(gym))


# Check Pune members after adding
print("Pune members after adding:", members_by_city(gym, "Pune"))
