import os
import re
import shutil

QUEUE_DIR = "queue_repo"  # cloned private repo will land here

def get_last_day_number():
    pattern = re.compile(r"^Day_(\d+)\.py$")
    max_num = 0
    for fname in os.listdir("."):
        match = pattern.match(fname)
        if match:
            max_num = max(max_num, int(match.group(1)))
    return max_num

def get_next_queue_file():
    if not os.path.isdir(QUEUE_DIR):
        return None
    files = sorted(
        f for f in os.listdir(QUEUE_DIR)
        if f.endswith(".py") and not f.startswith(".")
    )
    return files[0] if files else None

def main():
    next_file = get_next_queue_file()
    if not next_file:
        print("Queue is empty. Nothing to publish today.")
        return

    next_num = get_last_day_number() + 1
    new_name = f"Day_{next_num:03d}.py"

    shutil.move(os.path.join(QUEUE_DIR, next_file), new_name)
    print(f"Published {new_name} (was {next_file} from private queue)")

if __name__ == "__main__":
    main()
