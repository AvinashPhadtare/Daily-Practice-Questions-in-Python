# ======================== Question ========================
# Default Arguments
#
# You are given two classes:
# - EvenStream: generates 0, 2, 4, 6, ...
# - OddStream: generates 1, 3, 5, 7, ...
#
# Complete/debug the print_from_stream() function.
#
# Requirements:
# - Print the first n values from the given stream.
# - If no stream is provided, use a NEW EvenStream object.
# - Avoid reusing the same default EvenStream object between calls.
#
# Example Input:
# 3
# odd 2
# even 3
# odd 5
#
# Example Output:
# 1
# 3
# 0
# 2
# 4
# 1
# 3
# 5
# 7
# 9
# ============================================================

# Soltion:-
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream = None):
    if stream is None:
        stream = EvenStream()

    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
