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
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.time() - self.start_time


class SuppressErrors:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type is not None and issubclass(exc_type, self.exceptions):
                return True  # Suppress the exception
            return False  # Propagate other exceptions


        
# ======================== Test Cases ==========================
#  1] Test Timer context manager

with Timer() as t:
    time.sleep(1.5)

print(f"Block took {t.elapsed:.3f} seconds")

#  2] Test SuppressErrors context manager
with SuppressErrors(ValueError, KeyError):
    x = int("not a number")  # This will raise ValueError, but it will be suppressed

print("Continued after suppressed error")


# 3] Test SuppressErrors with an exception that is not suppressed

with SuppressErrors(ValueError, KeyError):
    x = 10 / 0  # This will raise ZeroDivisionError, which is not suppressed
