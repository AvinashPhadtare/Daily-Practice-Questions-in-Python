class HistoryTracker:
    def __init__(self):
        self.stack = []

    def visit(self, page:str):
        self.stack.append(page)
        return print(f"Visited: {page}")
    
    def back(self):
        if not self.stack:
            return print("No history")
        self.stack.pop()
        if not self.stack:
            return print("No history")
        last_visited = self.stack[-1]
        return print(f"Back to {last_visited}")
    
    def current(self):
        if not self.stack:
            return print("No history")
        current_visit = self.stack[-1]
        return print(f"Current URL:{current_visit}")
    
    def clear(self):
        self.stack.clear()
        print("All history cleared")



# Example usage:-

tracker = HistoryTracker()


tracker.visit("/members")
tracker.visit("/members/1")
tracker.visit("/member/2")


tracker.current()
tracker.back()
tracker.current()
tracker.clear()
tracker.current()