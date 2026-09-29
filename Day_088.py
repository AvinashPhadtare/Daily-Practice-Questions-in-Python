# ========================= Question ========================
#
# Write a @timer decorator that measures how long any function
# takes to execute and prints:
#
# "function_name took X.XXXXs"
#
# The decorator should work with any function, so the wrapper
# should be able to accept positional arguments (*args) and
# keyword arguments (**kwargs).
#
# ------------------------------------------------------------
#
# Write a @logger decorator that:
#
# 1. Prints this message BEFORE calling the original function:
#
#    "Calling function_name with args=(...) and kwargs={...}"
#
# 2. Calls the original function.
#
# 3. Prints this message AFTER the function finishes:
#
#    "function_name returned: <result>"
#
# ------------------------------------------------------------
#
# Apply BOTH decorators to the following function.
# 
# Function to decorate:
#
# calculate_member_fee(
#     base: float,
#     months: int,
#     discount: float = 0
# ) -> float
#
# The function calculates:
#
#     base * months * (1 - discount)
#
# ============================================================


# Solution: 
import time
from functools import wraps

# Timer decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.6f}s.")
        return result
    return wrapper


# Logger decorator
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args = {args} and kwargs = {kwargs}" )
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")

        return result
    return wrapper


# Main function to decorate and decorators in right order
@timer
@logger
def calculate_member_fee(base:float, months: int, discount:float=0) -> float:
    return base * months * (1 - discount)


# Usage example:
result = calculate_member_fee(500, 6, 0.10)
