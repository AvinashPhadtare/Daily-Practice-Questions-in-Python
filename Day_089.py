# ========================= Question ========================
# Write a Python program to create a decorator factory named
# @validate_types(**expected_types) that validates the types of
# function arguments at runtime.
#
# The decorator should work in the following form:
#
# @validate_types(member_id=int, amount=float, plan=str)
# def register_payment(member_id, amount, plan):
#     ...
#
# The decorator factory should:
#
# 1. Accept the expected argument types as keyword arguments.
#
# 2. Return a decorator that can be applied to a function.
#
# 3. The decorator should return a wrapper function.
#
# 4. When the decorated function is called, the wrapper should
#    check the actual types of the provided arguments.
#
# 5. The expected types are:
#       - member_id -> int
#       - amount    -> float
#       - plan      -> str
#
# 6. If all argument types are correct, the original function
#    should execute normally.
#
# 7. If any argument has an incorrect type, raise a TypeError
#    explaining which argument has the wrong type and what type
#    was expected.
#
# Example:
#
# register_payment(1, 500.0, "premium")
# -> Works because all argument types are correct.
#
# register_payment("1", 500.0, "premium")
# -> Raises TypeError because member_id must be an int.
#
# Important concept:
# The decorator factory has three levels:
#
#     factory(expected_types)
#             ↓
#        decorator(function)
#             ↓
#        wrapper(*args, **kwargs)
#
# The factory runs when the decorator is configured,
# the decorator receives the function, and the wrapper
# performs validation when the function is actually called.
#
# ============================================================


# ========================= Solution ======================== 
def validate_types(**expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Get the function's argument names
            arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
            
            # Create a dictionary of argument names and their corresponding values
            arg_dict = dict(zip(arg_names, args))
            arg_dict.update(kwargs)
            
            # Validate the types of the provided arguments
            for arg_name, expected_type in expected_types.items():
                if arg_name in arg_dict:
                    actual_value = arg_dict[arg_name]
                    if not isinstance(actual_value, expected_type):
                        raise TypeError(f"Argument '{arg_name}' must be of type {expected_type.__name__}, "
                                        f"but got {type(actual_value).__name__}.")
            
            # Call the original function if all types are valid
            return func(*args, **kwargs)
        return wrapper
    return decorator


# ========================= Example Usage ========================
@validate_types(member_id=int, amount=float, plan=str)
def register_payment(member_id, amount, plan):
    return {
        "member_id": member_id,
        "amount": amount,
        "plan": plan
    }

result = register_payment(1, 500.0, "premium")

print(result)
