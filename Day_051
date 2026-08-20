# ========================= Question ========================
# Simulate an async gym attendance data fetcher.
#
# Each attendance record is fetched using the given async function:
#
# fetch_attendance(member_id)
#    - Waits for 0.3 seconds to simulate a database/API delay.
#    - Returns attendance information as a dictionary.
#
# Write an async function fetch_all_attendance(ids: list) -> list
# that fetches the attendance data of all members in the list
# CONCURRENTLY (not sequentially).
#
# Measure:
# - Fetching 5 members sequentially should take approximately 1.5 seconds.
# - Fetching 5 members concurrently should take approximately 0.3 seconds.
# - Prove the difference using timing.
#
# Constraints:
# - Use Python's asyncio module.
# - Use async and await.
# - Use asyncio.gather() to fetch all attendance records concurrently.
# - Do NOT use threading or multiprocessing.
# ============================================================


# Solution:-
import asyncio
import time


async def fetch_attendance(member_id: int) -> dict:
    await asyncio.sleep(0.3)  # simulates DB or API delay

    return {
        "member_id": member_id,
        "attendance": "present",
        "days": 20
    }


async def fetch_all_attendance(ids: list) -> list:
    # Create a coroutine for each member
    tasks = [fetch_attendance(member_id) for member_id in ids]

    # Fetch all attendance records concurrently
    results = await asyncio.gather(*tasks)

    return results


# Example Usage
async def main():
    ids = [101, 102, 103, 104, 105]

    # Start timer
    start = time.perf_counter()

    # Fetch attendance concurrently
    attendance = await fetch_all_attendance(ids)

    # Stop timer
    end = time.perf_counter()

    print("Attendance Records:")

    for record in attendance:
        print(record)

    print(f"\nTime taken: {end - start:.2f} seconds")


asyncio.run(main())
