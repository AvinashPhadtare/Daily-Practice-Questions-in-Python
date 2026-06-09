from collections import deque

class GymEntryQueue:
    def __init__(self):
        self.deque = deque()

    def scan_in(self, member_name):
        self.deque.append(member_name)
        position = len(self.deque)
        print(f"{member_name} joined the queue. Position: {position}")
        return position

    def process_next(self):
        if self.is_empty():
            print("No members to process. The queue is empty.")
            return None
        member_name = self.deque.popleft()
        print(f"Processing: {member_name}")
        return member_name

    def queue_status(self):
        if self.is_empty():
            print("Queue is empty. No members waiting.")
            return
        count = len(self.deque)
        print(f"Members waiting: {count}")
        print("Queue:")
        for position, member in enumerate(self.deque, start=1):
            print(f"  {position}. {member}")

    def is_empty(self):
        return not self.deque


# Simulation
gym_queue = GymEntryQueue()

# Scan in 4 members
gym_queue.scan_in("Avinash")
gym_queue.scan_in("Rohan")
gym_queue.scan_in("Priya")
gym_queue.scan_in("Vikram")

# Process 2
gym_queue.process_next()
gym_queue.process_next()

# Scan in 1 more
gym_queue.scan_in("Neha")

# Print queue status
gym_queue.queue_status()