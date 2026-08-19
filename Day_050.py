# ========================= Question ========================
# Simulate an async member data fetcher.
#
# A member is fetched using the given async function:
#
# fetch_member(member_id)
#    - Waits for 0.5 seconds to simulate a database/API delay.
#    - Returns member details as a dictionary.
#
# Write an async function fetch_multiple(ids: list) -> list
# that fetches all members in the list CONCURRENTLY
# (not sequentially).
#
# Measure:
# - Fetching 6 members sequentially should take approximately 3 seconds.
# - Fetching 6 members concurrently should take approximately 0.5 seconds.
# - Prove the difference using timing.
#
# Constraints:
# - Use Python's asyncio module.
# - Use async and await.
# - Use asyncio.gather() to fetch members concurrently.
# ============================================================


# Solution:-
import asyncio
import time


async def fetch_member(member_id: int) -> dict:
    await asyncio.sleep(0.5)  # simulates DB or API delay

    return {
        "id": member_id,
        "name": f"Member_{member_id}",
        "plan": "basic"
    }


async def fetch_multiple(ids: list) -> list:
    # Create a coroutine for each member
    tasks = [fetch_member(member_id) for member_id in ids]

    # Fetch all members concurrently
    results = await asyncio.gather(*tasks)

    return results


# Example Usage
async def main():
    ids = [1, 2, 3, 4, 5, 6]

    # Start timer
    start = time.perf_counter()

    # Fetch members concurrently
    members = await fetch_multiple(ids)

    # Stop timer
    end = time.perf_counter()

    print("Members:")

    for member in members:
        print(member)

    print(f"\nTime taken: {end - start:.2f} seconds")


asyncio.run(main())
