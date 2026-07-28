class GymPlan:
    def __init__(self, name, price, duration_months, discount_percent=0):
        self.name = name
        self.price = price
        self.duration_months = duration_months
        self.discount_percent = discount_percent

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value not in ("basic", "premium", "vip"):
            raise ValueError("Name must be 'basic', 'premium', or 'vip'.")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be a positive number.")
        self._price = float(value)

    @property
    def duration_months(self):
        return self._duration_months

    @duration_months.setter
    def duration_months(self, value):
        if value not in (1, 3, 6, 12):
            raise ValueError("Duration must be 1, 3, 6, or 12 months.")
        self._duration_months = value

    @property
    def discount_percent(self):
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Discount must be between 0 and 100.")
        self._discount_percent = value

    @property
    def final_price(self):
        return self.price * (1 - self.discount_percent / 100)

    @property
    def is_premium_or_above(self):
        return self.name in ("premium", "vip")



# Example Usage:-
# Create a GymPlan object
plan = GymPlan("premium", 3000.0, 6, 10)

# Access attributes
print("Plan Name:", plan.name)
print("Price:", plan.price)
print("Duration:", plan.duration_months, "months")
print("Discount:", plan.discount_percent, "%")

# Read-only computed property
print("Final Price:", plan.final_price)

# Check if plan is Premium or VIP
print("Premium or Above:", plan.is_premium_or_above)

# Update some values
plan.price = 3500.0
plan.discount_percent = 20

print("\nAfter Updating:")
print("Updated Price:", plan.price)
print("Updated Discount:", plan.discount_percent, "%")
print("Updated Final Price:", plan.final_price)

# Uncomment these one by one to see ValueError

# plan.name = "gold"          # Invalid plan name
# plan.price = -100           # Price must be positive
# plan.duration_months = 5    # Invalid duration
# plan.discount_percent = 120 # Discount must be between 0 and 100
