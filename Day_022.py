class PaymentRecord:
    def __init__(self, member_id, amount, date, status, payment_method):
        self.member_id = member_id
        self.amount = amount
        self.date = date
        self.status = status
        self.payment_method = payment_method

    def mark_paid(self):
        self.status = "paid"

    def mark_failed(self):
        self.status = "failed"

    def is_overdue(self, today):
        if self.status == "pending" and self.date < today:
            return True
        return False

    def __repr__(self):
        return (f"PaymentRecord(member_id={self.member_id}, "
                f"amount={self.amount}, "
                f"date='{self.date}', "
                f"status='{self.status}', "
                f"payment_method='{self.payment_method}')")


# Create 3 payment records
payment1 = PaymentRecord(101, 1500.0, "2026-07-20", "pending", "upi")
payment2 = PaymentRecord(102, 2000.0, "2026-07-18", "pending", "cash")
payment3 = PaymentRecord(103, 1800.0, "2026-07-15", "pending", "card")

# Mark one as paid
payment1.mark_paid()

# Mark one as failed
payment2.mark_failed()

# Check if the third payment is overdue
today = "2026-07-22"

print(payment1)
print(payment2)
print(payment3)

print("Is Payment 3 overdue?", payment3.is_overdue(today))