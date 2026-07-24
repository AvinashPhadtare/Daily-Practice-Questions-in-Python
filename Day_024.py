class PaymentRecord:
    def __init__(self, member_id, amount, date, status, payment_method):
        self.member_id = member_id
        self.amount = amount
        self.date = date
        self.status = status
        self.payment_method = payment_method

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["member_id"],
            data["amount"],
            data["date"],
            data["status"],
            data["method"]
        )

    @classmethod
    def from_csv_row(cls, row):
        values = row.split(",")

        return cls(
            int(values[0]),
            float(values[1]),
            values[2],
            values[3],
            values[4]
        )

    def __repr__(self):
        return (f"PaymentRecord(member_id={self.member_id}, "
                f"amount={self.amount}, "
                f"date='{self.date}', "
                f"status='{self.status}', "
                f"payment_method='{self.payment_method}')")


# Create object from dictionary
data = {
    "member_id": 1,
    "amount": 500.0,
    "date": "2025-01-15",
    "status": "paid",
    "method": "upi"
}

payment1 = PaymentRecord.from_dict(data)

# Create object from CSV
payment2 = PaymentRecord.from_csv_row(
    "2,750.0,2025-02-10,pending,cash"
)

print(payment1)
print(payment2)