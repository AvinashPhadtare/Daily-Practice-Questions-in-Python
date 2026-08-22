# ========================= Question =========================
#
# You need to fetch data for 20 members from an external API
# that allows only 3 concurrent requests.
#
# The following function simulates an API call:
#
# async def fetch_member_data(member_id: int) -> dict:
#     await asyncio.sleep(0.2)  # Simulates API call
#     return {
#         "id": member_id,
#         "data": f"data_for_{member_id}"
#     }
#
# Write the function:
#
#     fetch_with_limit(member_ids: list, max_concurrent: int) -> list
#
# using asyncio.Semaphore.
#
# Requirements:
#
# 1. Fetch data for all member IDs asynchronously.
#
# 2. Use asyncio.Semaphore to make sure that no more than
#    max_concurrent requests run at the same time.
#
# 3. For this problem, max_concurrent will be 3.
#
# 4. Verify that at no point are more than max_concurrent
#    requests running simultaneously.
#
# 5. Print which batch/request is running and how many
#    requests are currently active.
#
# 6. Return the list of all fetched member data.
#
# Example:
#
# member_ids = [1, 2, 3, ..., 20]
# results = await fetch_with_limit(member_ids, 3)
#
# The important rule is:
#
#     Active requests <= 3
#
# =============================================================

import asyncio


# Simulates an external API call
async def fetch_member_data(member_id: int) -> dict:
    await asyncio.sleep(0.2)

    return {
        "id": member_id,
        "data": f"data_for_{member_id}"
    }


async def fetch_with_limit(member_ids: list, max_concurrent: int) -> list:

    # Create a semaphore with the maximum number
    # of requests that are allowed at the same time.
    semaphore = asyncio.Semaphore(max_concurrent)

    # Keeps track of how many requests are currently running.
    active_requests = 0

    # Used to safely update active_requests.
    counter_lock = asyncio.Lock()

    # Counts the order in which requests enter.
    request_number = 0

    # This function performs one limited API request.
    async def limited_fetch(member_id):

        # These variables belong to the outer function,
        # so Python needs 'nonlocal' when we modify them.
        nonlocal active_requests, request_number

        # Wait here until a semaphore slot is available.
        async with semaphore:

            # Safely increase the active request counter.
            async with counter_lock:
                active_requests += 1
                request_number += 1

                current_request = request_number

                print(
                    f"Request {current_request}: "
                    f"Member {member_id} started | "
                    f"Active requests = {active_requests}"
                )

                # Verify that the limit is never exceeded.
                assert active_requests <= max_concurrent

            try:
                # Perform the simulated API request.
                result = await fetch_member_data(member_id)

                return result

            finally:
                # Decrease the active request counter
                # when the request finishes.
                async with counter_lock:
                    active_requests -= 1

                    print(
                        f"Member {member_id} finished | "
                        f"Active requests = {active_requests}"
                    )

    # Create one asynchronous operation for every member.
    tasks = [
        limited_fetch(member_id)
        for member_id in member_ids
    ]

    # Run all tasks concurrently.
    #
    # The semaphore inside limited_fetch() ensures
    # that only max_concurrent tasks can actually
    # perform the API call at one time.
    results = await asyncio.gather(*tasks)

    return results


# -------------------------------------------------------------
# Example Usage
# -------------------------------------------------------------

async def main():

    # Create 20 member IDs.
    member_ids = list(range(1, 21))

    # The API allows only 3 concurrent requests.
    max_concurrent = 3

    # Fetch all member data with the concurrency limit.
    results = await fetch_with_limit(
        member_ids,
        max_concurrent
    )

    print("\nAll requests completed!")

    print("\nResults:")
    for result in results:
        print(result)


# Start the asynchronous program.
asyncio.run(main())
