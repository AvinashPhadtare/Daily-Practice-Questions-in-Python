class Gym_Membership:
    def __init__(self, name, age, plan):
        self.name = name
        self.age = age
        self.plan = plan
        self.is_active = False

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def upgrade_plan(self, new_plan):
        active_plan = ["basic", "premium", "vip"]
        if new_plan not in active_plan:
            raise ValueError(f"{new_plan} is not a valid plan")
        self.plan = new_plan
    
    def __str__(self):
        status = "Active" if self.is_active else "Inactive"
        return f"{self.name} | Age: {self.age} | Plan: {self.plan} | Status: {status}"

# Create two members
m1 = Gym_Membership("Avinash", 22, "basic")
m2 = Gym_Membership("Riya", 25, "premium")

# Demonstrate functionality
m1.activate()
m2.deactivate()
m1.upgrade_plan("vip")

# Print results
print(m1)
print(m2)
