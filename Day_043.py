# Question:-

# Implement an LRU (Least Recently Used) Cache using a Python class named
# LRUCache.
#
# The cache should store key-value pairs and should have a fixed capacity.
# When the cache becomes full and a new item is added, the item that has
# been used least recently must be removed.
#
# Implement the following operations:
#
# 1. __init__(capacity):
#    Initialize the cache with the given maximum capacity.
#
# 2. get(key):
#    Return the value associated with the key if it exists.
#    If the key does not exist, return -1.
#    Whenever a key is accessed successfully, mark it as the most recently
#    used item.
#
# 3. put(key, value):
#    Insert a new key-value pair into the cache or update the value if the
#    key already exists.
#    The inserted or updated key must become the most recently used item.
#    If adding the item makes the cache exceed its capacity, remove the
#    least recently used item.


# Solution:-
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# Example usage:-

cache = LRUCache(3)

cache.put("member:1", {"name": "Avinash"})
cache.put("member:2", {"name": "Rahul"})
cache.put("member:3", {"name": "Priya"})

print(cache.get("member:1"))

cache.put("member:4", {"name": "Sneha"})

print(cache.get("member:2"))
