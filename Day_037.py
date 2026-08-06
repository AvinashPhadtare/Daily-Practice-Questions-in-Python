# ========================= Question ========================
# You are given a list of member transactions. Each transaction is represented
# as a dictionary containing:
#   - member_id : Unique ID of the member
#   - type      : "payment" or "refund"
#   - amount    : Transaction amount
#
# transactions = [
#     {"member_id": 1, "type": "payment", "amount": 500},
#     {"member_id": 2, "type": "payment", "amount": 1200},
#     {"member_id": 1, "type": "refund", "amount": 200},
#     {"member_id": 3, "type": "payment", "amount": 800},
#     {"member_id": 2, "type": "refund", "amount": 300},
#     {"member_id": 1, "type": "payment", "amount": 500},
# ]
#
# Write the following functions:
#
# 1. group_by_member(txns)
#    - Returns a dictionary where each key is a member_id and
#      the value is a list of all transactions for that member.
#
# 2. net_balance(txns, member_id)
#    - Returns the net balance of the given member.
#    - Net Balance = Total Payments - Total Refunds
#
# 3. top_payer(txns)
#    - Returns the member_id with the highest net balance.
#
# Finally, display:
# - The grouped transactions.
# - The net balance of member 1.
# - The member ID of the top payer.==============================================================



# Solution:- 
transactions = [
    {"member_id": 1, "type": "payment", "amount": 500},
    {"member_id": 2, "type": "payment", "amount": 1200},
    {"member_id": 1, "type": "refund", "amount": 200},
    {"member_id": 3, "type": "payment", "amount": 800},
    {"member_id": 2, "type": "refund", "amount": 300},
    {"member_id": 1, "type": "payment", "amount": 500},
]


def group_by_member(txns):
    groups = {}

    for txn in txns:
        member = txn["member_id"]

        if member not in groups:
            groups[member] = []

        groups[member].append(txn)

    return groups


def net_balance(txns, member_id):
    balance = 0

    for txn in txns:
        if txn["member_id"] == member_id:
            if txn["type"] == "payment":
                balance += txn["amount"]
            else:
                balance -= txn["amount"]

    return balance


def top_payer(txns):
    grouped = group_by_member(txns)

    highest_member = None
    highest_balance = float("-inf")

    for member, member_txns in grouped.items():
        balance = net_balance(member_txns, member)

        if balance > highest_balance:
            highest_balance = balance
            highest_member = member

    return highest_member

# Example Usage:- 
print("Grouped Transactions:")
print(group_by_member(transactions))

print("\nNet Balance of Member 1:")
print(net_balance(transactions, 1))

print("\nTop Payer:")
print(top_payer(transactions))
