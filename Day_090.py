# ========================= Question ========================
# Write a Python program to create a @memoize decorator that:
#
# 1. Caches function results based on argument values.
#
# 2. Tracks cache hits and misses.
#
# 3. Provides a method on the decorated function that returns:
#
#       {"hits": int, "misses": int, "cached_keys": int}
#
# 4. Provides a cache_clear() method to reset the cache.
#
# 5. Implement the memoization manually.
#
#    Do NOT use functools.lru_cache.
#
# 6. Consider whether the function arguments are hashable, since
#    lists and dictionaries cannot be used directly as dictionary keys.
#
# 7. Test the decorator using a slow recursive Fibonacci function.
#
# 8. Compare the execution time of the Fibonacci function with
#    and without using cached results.
# =============================================================


# ========================= Solution ========================
import time
from functools import wraps
def memoize(func):
    cache = {}
    hits = 0
    misses = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal hits, misses
        # Create a hashable key from the function arguments
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            hits += 1
            return cache[key]
        else:
            misses += 1
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    def cache_info():
        return {
            "hits": hits,
            "misses": misses, 
            "cached_keys": len(cache)
        }

    def cache_clear():
        nonlocal hits, misses
        hits = 0
        misses = 0
        cache.clear()

    wrapper.cache_info = cache_info
    wrapper.cache_clear = cache_clear

    return wrapper

# Slow recursive Fibonacci function
def fibonacci_slow(n):
    if n <= 1:
        return n

    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)


# Memoized Fibonacci function
@memoize
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# ======================== Without Memoization =======================

start = time.perf_counter()

result1 = fibonacci_slow(35)

end = time.perf_counter()

print("Without memoization:")
print("Result:", result1)
print("Time:", end - start)


# ======================== With Memoization =====================

start = time.perf_counter()

result2 = fibonacci(35)

end = time.perf_counter()

print("\nWith memoization:")
print("Result:", result2)
print("Time:", end - start)

print("Cache Info:", fibonacci.cache_info())


# ======================= Clear Cache =======================

fibonacci.cache_clear()

print("\nAfter cache_clear():")
print(fibonacci.cache_info())
