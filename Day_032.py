class GymConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self,
                 max_capacity=500,
                 gym_name="Power Gym",
                 open_time="06:00",
                 close_time="22:00",
                 active_plans=None):

        # Prevent reinitialization on subsequent calls
        if self._initialized:
            return

        self.max_capacity = max_capacity
        self.gym_name = gym_name
        self.open_time = open_time
        self.close_time = close_time
        self.active_plans = active_plans if active_plans is not None else ["Basic", "Premium"]

        self._initialized = True

    def update(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            raise AttributeError(f"'{key}' is not a valid configuration field.")

    def __str__(self):
        return (
            f"Gym Name      : {self.gym_name}\n"
            f"Max Capacity  : {self.max_capacity}\n"
            f"Open Time     : {self.open_time}\n"
            f"Close Time    : {self.close_time}\n"
            f"Active Plans  : {self.active_plans}"
        )


# Proof that it is a Singleton
config1 = GymConfig()
config2 = GymConfig()

print("Same object?", config1 is config2)

config1.update("max_capacity", 700)
config1.update("gym_name", "Elite Fitness")

print("\nConfiguration from config1:")
print(config1)

print("\nConfiguration from config2:")
print(config2)
