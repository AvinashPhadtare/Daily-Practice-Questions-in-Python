def group_by_member(payments: list) -> dict:
    """Group payment records by member_id and summarize totals and months paid."""
    result = {}

    for payment in payments:
        member_id = payment["member_id"]
        amount = payment["amount"]
        month = payment["month"]

        member_summary = result.setdefault(
            member_id,
            {"total_paid": 0, "months_paid": []},
        )

        member_summary["total_paid"] += amount
        member_summary["months_paid"].append(month)

    return result


if __name__ == "__main__":
    payments = [
        {"member_id": 1, "amount": 500, "month": "Jan"},
        {"member_id": 2, "amount": 1200, "month": "Jan"},
        {"member_id": 1, "amount": 500, "month": "Feb"},
        {"member_id": 3, "amount": 800, "month": "Jan"},
        {"member_id": 2, "amount": 1200, "month": "Feb"},
        {"member_id": 1, "amount": 500, "month": "Mar"},
    ]

    print(group_by_member(payments))
