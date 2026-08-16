# ========================= Question ========================

# Build a simple log file system for a gym API.
# Implement the following functions:
# 1. append_log(filepath, level, member_id, event)
# - Write a new log entry with the current timestamp.
# - Format: "YYYY-MM-DD HH:MM:SS | LEVEL | member:<id> | <event>"
# 2. parse_logs(filepath) -> list
# - Read all log lines.
# - Return a list of dictionaries with keys:
# "timestamp", "level", "member_id", "event".
# 3. filter_by_level(filepath, level: str) -> list
# - Return only log entries matching the given level.
# 4. error_count_per_member(filepath) -> dict
# - Return a dictionary mapping each member_id to their error count.

# ============================================================


# Solution:-
from datetime import datetime

def append_log(filepath, level, member_id, event):
    """Append a new log entry with current timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | {level} | member:{member_id} | {event}\n"
    with open(filepath, "a") as file:
        file.write(log_entry)


def parse_logs(filepath):
    """Parse log file into structured list of dicts."""
    logs = []
    with open(filepath, "r") as file:
        for line in file:
            parts = [p.strip() for p in line.strip().split("|")]
            if len(parts) == 4:
                timestamp, level, member_part, event = parts
                member_id = member_part.split(":")[1]
                logs.append({
                    "timestamp": timestamp,
                    "level": level,
                    "member_id": member_id,
                    "event": event
                })
    return logs


def filter_by_level(filepath, level):
    """Return logs filtered by level."""
    logs = parse_logs(filepath)
    return [log for log in logs if log["level"] == level]


def error_count_per_member(filepath):
    """Count number of ERROR logs per member."""
    logs = parse_logs(filepath)
    error_counts = {}
    for log in logs:
        if log["level"] == "ERROR":
            member_id = log["member_id"]
            error_counts[member_id] = error_counts.get(member_id, 0) + 1
    return error_counts



# Example Usage:-

# Create and append logs
append_log("gym_logs.txt", "INFO", 42, "checked_in")
append_log("gym_logs.txt", "ERROR", 17, "payment_failed")
append_log("gym_logs.txt", "INFO", 42, "checked_out")
append_log("gym_logs.txt", "ERROR", 17, "card_declined")

# Parse all logs
print("All Logs:")
print(parse_logs("gym_logs.txt"))

# Filter only ERROR logs
print("\nError Logs:")
print(filter_by_level("gym_logs.txt", "ERROR"))

# Count errors per member
print("\nError Count per Member:")
print(error_count_per_member("gym_logs.txt"))
