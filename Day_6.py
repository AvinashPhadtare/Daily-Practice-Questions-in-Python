class HistoryTracker:
    def __init__(self):
        self.stack = []

    def visit(self, page: str):
        self.stack.append(page)
        return f"Visited: {page}"

    def back(self):
        if not self.stack:
            return "No history"
        self.stack.pop()
        if not self.stack:
            return "No history"
        return self.stack[-1]

    def current(self):
        if not self.stack:
            return "No history"
        return self.stack[-1]

    def clear(self):
        self.stack.clear()
        print("All history cleared")


# Example usage:
tracker = HistoryTracker()

tracker.visit("/members")
tracker.visit("/members/1")
tracker.visit("/member/2")

print(tracker.current())
print(tracker.back())
print(tracker.current())
tracker.clear()
print(tracker.current())