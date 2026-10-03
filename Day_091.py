# ========================= Question ========================
#
# Write a @rate_limit(max_calls: int, period: float) decorator
# that allows at most max_calls calls in any rolling
# period-second window.
#
# If the limit is exceeded, raise:
# RateLimitError("Too many calls. Try again in Xs")
#
# Requirements:
#
# 1. Use time.time() to track the current time.
#
# 2. Use collections.deque to store timestamps of recent calls.
#
# 3. Remove timestamps that are older than the rolling period.
#
# 4. If the number of recent calls reaches max_calls,
#    raise RateLimitError without calling the function.
#
# 5. If the call is allowed, store its timestamp and
#    execute the decorated function.
#
# ============================================================


# ========================= Solution =========================
from collections import deque
from functools import wraps
import time


class RateLimitError(Exception):
    pass


def rate_limit(max_calls: int, period: float):

    def decorator(func):
        timestamps = deque()

        @wraps(func)
        def wrapper(*args, **kwargs):

            current_time = time.time()

            # Remove timestamps outside the rolling time window
            while timestamps and current_time - timestamps[0] >= period:
                timestamps.popleft()

            # Check rate limit
            if len(timestamps) >= max_calls:
                retry_after = period - (current_time - timestamps[0])

                raise RateLimitError(
                    f"Too many calls. Try again in {retry_after:.1f}s"
                )

            # Store current call timestamp
            timestamps.append(current_time)

            # Execute original function
            return func(*args, **kwargs)
        return wrapper
    return decorator

# ======================== Example Usage =========================
@rate_limit(max_calls=3, period=5.0)
def send_sms_alert(member_id: int):
    print(f"SMS sent to member {member_id}")


send_sms_alert(1)
send_sms_alert(2)
send_sms_alert(3)
# This Below call will raise a RateLimitError since it exceeds the max_calls limit within the 5-second period.
send_sms_alert(4)
