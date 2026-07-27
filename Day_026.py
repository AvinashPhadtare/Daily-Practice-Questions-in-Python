class PlanUtils:
    PLANS = {
        "basic": 500,
        "premium": 1200,
        "vip": 2500
    }

    @staticmethod
    def is_valid_plan(plan: str) -> bool:
        return plan in PlanUtils.PLANS

    @staticmethod
    def plan_price(plan: str) -> float:
        if not PlanUtils.is_valid_plan(plan):
            raise ValueError("Invalid plan name")
        return float(PlanUtils.PLANS[plan])

    @staticmethod
    def upgrade_path(current: str) -> str:
        if not PlanUtils.is_valid_plan(current):
            raise ValueError("Invalid plan name")

        if current == "basic":
            return "premium"
        elif current == "premium":
            return "vip"
        else:
            return "already_max"

    @staticmethod
    def discount_price(plan: str, percent: float) -> float:
        price = PlanUtils.plan_price(plan)
        return price - (price * percent / 100)

# Example usage

print(PlanUtils.is_valid_plan("basic"))
print(PlanUtils.is_valid_plan("gold"))

print(PlanUtils.plan_price("basic"))
print(PlanUtils.plan_price("vip"))

print(PlanUtils.upgrade_path("basic"))
print(PlanUtils.upgrade_path("vip"))

print(PlanUtils.discount_price("vip", 10))
print(PlanUtils.discount_price("premium", 25))