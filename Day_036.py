# ========================= Question ========================
# Simulate a gym support ticket system with priority.

# Each ticket has:
# - ticket_id
# - member_name
# - issue
# - priority (1 = Low, 2 = Medium, 3 = High)

# Build a class `SupportQueue` with the following methods:

# 1. submit(ticket_id, member_name, issue, priority)
#    - Add a new support ticket to the queue.

# 2. resolve_next() -> dict
#    - Resolve and return the highest-priority ticket.
#    - If multiple tickets have the same priority, resolve the one that arrived first (FIFO).

# 3. pending_count() -> int
#    - Return the number of pending tickets.

# 4. show_queue()
#    - Display all pending tickets in the order they would be resolved.

# Constraints:
# - Do NOT use Python's `heapq` module.
# - Implement the priority queue logic manually.==============================================================



# Solution:- 
class SupportQueue:
    def __init__(self):
        self.queue = []

    def submit(self, ticket_id, member_name, issue, priority):
        ticket = {
            "ticket_id": ticket_id,
            "member_name": member_name,
            "issue": issue,
            "priority": priority
        }
        self.queue.append(ticket)

    def resolve_next(self):
        if not self.queue:
            return None

        highest_index = 0

        for i in range(1, len(self.queue)):
            if self.queue[i]["priority"] > self.queue[highest_index]["priority"]:
                highest_index = i

        return self.queue.pop(highest_index)

    def pending_count(self):
        return len(self.queue)

    def show_queue(self):
        sorted_queue = sorted(self.queue, key=lambda x: x["priority"], reverse=True)

        for ticket in sorted_queue:
            print(ticket)


# Example Usage
support = SupportQueue()

support.submit(101, "Rahul", "Payment Failed", 2)
support.submit(102, "Amit", "Equipment Broken", 3)
support.submit(103, "Riya", "Membership Renewal", 3)
support.submit(104, "Karan", "App Login Issue", 1)

print("Pending Tickets:", support.pending_count())

print("\nQueue in Resolution Order:")
support.show_queue()

print("\nResolved Ticket:")
print(support.resolve_next())

print("\nRemaining Tickets:", support.pending_count())
