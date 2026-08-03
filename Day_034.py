# ========================= Question ========================
#
# You have a list of plan types for all active members:
#
# plans = [
#     "basic", "premium", "basic", "vip",
#     "premium", "basic", "vip", "premium", "basic"
# ]
#
# Write the following functions:
#
# 1. plan_distribution(plans: list) -> dict
#    - Return the count of each plan type.
#
# 2. most_popular_plan(plans: list) -> str
#    - Return the plan with the highest count.
#
# 3. plans_above_threshold(plans: list, threshold: int) -> list
#    - Return the plan names that appear MORE than
#      'threshold' times.
#
# Constraints:
# - Do NOT use collections.Counter.
# - Count the frequencies manually using a dictionary.
# ==============================================================



# Solution:- 

def plan_distribution(plans: list):
    counts = {}

    for plan in plans:
        counts[plan] = counts.get(plan, 0) + 1

    return counts

def most_popular_plan(plans: list):
    counts = plan_distribution(plans)

    max_plan = None
    max_count = 0

    for plan, count in counts.items():
        if count > max_count:
            max_count = count
            max_plan = plan

    return max_plan

def plans_above_threshold(plans: list, threshold: int):

    result = []
    counts = plan_distribution(plans)

    for plan, count in counts.items():
        if count > threshold:
            result.append(plan)

    return result




# Example usage:-
plans = [
    "basic",
    "premium",
    "basic",
    "vip",
    "premium",
    "basic",
    "vip",
    "premium",
    "basic"
]


print(plan_distribution(plans))
# Output:-
# {'basic': 4, 'premium': 3, 'vip': 2}


print(most_popular_plan(plans))
# Output:-
# 'basic'


print(plans_above_threshold(plans, 2))
# Output:-
# ['basic', 'premium']
