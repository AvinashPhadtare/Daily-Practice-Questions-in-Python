# ========================= Question =========================
#
# Build a Timer context manager that measures the time spent
# inside a `with` block.
#
# Example:
#
#     with Timer() as t:
#         time.sleep(1.5)
#
#     print(f"Block took {t.elapsed:.3f} seconds")
#
# The Timer should:
# - Start timing in __enter__().
# - Store elapsed time in __exit__().
# - Work even if an exception occurs inside the block.
#
# Then build a SuppressErrors(*exceptions) context manager that:
# - Accepts specific exception types.
# - Suppresses those specified exceptions.
# - Allows other exceptions to propagate normally.
#
# Example:
#
#     with SuppressErrors(ValueError, KeyError):
#         x = int("not a number")
#
#     print("Continued after suppressed error")
#
# =============================================================


# ======================== Solution ===========================

import time


class Timer:

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Calculate elapsed time
        self.elapsed = time.perf_counter() - self.start_time

        # Do not suppress exceptions
        return False


class SuppressErrors:

    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Check if the exception type is in the list of exceptions to suppress
        if exc_type is not None and issubclass(
            exc_type,
            self.exceptions
        ):
            return True

        return False


# ======================== Test Cases ==========================

# 1. Test Timer context manager

with Timer() as t:
    time.sleep(1.5)

print(f"Block took {t.elapsed:.3f} seconds")


# 2. Test SuppressErrors with ValueError

with SuppressErrors(ValueError, KeyError):
    x = int("not a number")

print("Continued after suppressed error")


# 3. Test SuppressErrors with an exception
#    that should NOT be suppressed

# with SuppressErrors(ValueError, KeyError):
#     x = 10 / 0
