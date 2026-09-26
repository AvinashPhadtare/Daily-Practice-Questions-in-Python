# ========================= Question ========================
# Build a stateful running average calculator using a generator
# with send().
#
# The generator should:
#
# - Receive new numbers using send()
# - Maintain the running state
# - Yield the current running average after each new number
#
# Example:
#
# avg = running_average()
# next(avg)              # Prime the generator
#
# print(avg.send(10))    # 10.0
# print(avg.send(20))    # 15.0
# print(avg.send(30))    # 20.0
# print(avg.send(40))    # 25.0
#
#
# Then build running_stats() that tracks:
#
# - count
# - mean
# - min
# - max
#
# Send a new number and get back a dictionary containing
# all the current statistics.
#
# Example:
#
# stats = running_stats()
# next(stats)             # Prime the generator
#
# print(stats.send(10))
# print(stats.send(20))
# print(stats.send(5))
# print(stats.send(30))
#
# Expected output:
#
# {'count': 1, 'mean': 10.0, 'min': 10, 'max': 10}
# {'count': 2, 'mean': 15.0, 'min': 10, 'max': 20}
# {'count': 3, 'mean': 11.666666666666666, 'min': 5, 'max': 20}
# {'count': 4, 'mean': 16.25, 'min': 5, 'max': 30}
#
# ============================================================



# ========================= Solution =========================
def running_average():
    total = 0
    count = 0

    while True:
        number = yield total / count if count else None

        total += number
        count += 1


def running_stats():
    count = 0
    total = 0
    minimum = None
    maximum = None

    while True:
        number = yield {
            "count": count,
            "mean": total / count if count else None,
            "min": minimum,
            "max": maximum
        }

        count += 1
        total += number

        if minimum is None or number < minimum:
            minimum = number

        if maximum is None or number > maximum:
            maximum = number


# ====================== Running Average =====================

avg = running_average()

next(avg)

print(avg.send(10))   # 10.0
print(avg.send(20))   # 15.0
print(avg.send(30))   # 20.0
print(avg.send(40))   # 25.0


# ======================= Running Stats ======================

stats = running_stats()

next(stats)

print(stats.send(10))
print(stats.send(20))
print(stats.send(5))
print(stats.send(30))

# Output:

# {'count': 1, 'mean': 10.0, 'min': 10, 'max': 10}
# {'count': 2, 'mean': 15.0, 'min': 10, 'max': 20}
# {'count': 3, 'mean': 11.666666666666666, 'min': 5, 'max': 20}
# {'count': 4, 'mean': 16.25, 'min': 5, 'max': 30}
