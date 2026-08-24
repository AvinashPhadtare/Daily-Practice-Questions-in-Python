# ========================= Question ========================
# Q42. Async Error Handling with asyncio.gather()
#
# You have a list of member IDs. Some IDs are valid and some
# will cause errors. Simulate an error by making odd IDs raise
# an exception.
#
# Given the following asynchronous function:
#
# async def fetch_member_safe(member_id: int) -> dict:
#     await asyncio.sleep(0.1)
#     if member_id % 2 != 0:
#         raise ValueError(f"Member {member_id} not found")
#     return {"id": member_id, "status": "ok"}
#
# Write an asynchronous function:
#
#     batch_fetch(ids: list) -> dict
#
# that:
#
# 1. Fetches all member IDs concurrently.
#
# 2. Uses asyncio.gather() with return_exceptions=True
#    so that one failed request does not stop the others.
#
# 3. Separates the results into:
#
#       {
#           "success": [...],
#           "failed": [
#               {"id": x, "error": "..."}
#           ]
#       }
#
# 4. Never crashes even if all requests fail.
#
# 5. Prints a summary at the end showing:
#    - Number of successful requests
#    - Number of failed requests
#
# ============================================================


import asyncio


# ------------------------------------------------------------
# Fetch one member asynchronously
# ------------------------------------------------------------
async def fetch_member_safe(member_id: int) -> dict:

    # Simulate an asynchronous operation such as
    # an API request or database request.
    await asyncio.sleep(0.1)

    # Odd member IDs will simulate an error.
    if member_id % 2 != 0:

        # Raise an exception when the member is not found.
        raise ValueError(f"Member {member_id} not found")

    # Even IDs are considered successful.
    return {
        "id": member_id,
        "status": "ok"
    }


# ------------------------------------------------------------
# Fetch multiple members concurrently
# ------------------------------------------------------------
async def batch_fetch(ids: list) -> dict:

    # Create one coroutine for every member ID.
    #
    # Example:
    # ids = [1, 2, 3, 4]
    #
    # tasks becomes:
    # [
    #     fetch_member_safe(1),
    #     fetch_member_safe(2),
    #     fetch_member_safe(3),
    #     fetch_member_safe(4)
    # ]
    tasks = [
        fetch_member_safe(member_id)
        for member_id in ids
    ]

    # Run all coroutines concurrently.
    #
    # return_exceptions=True is VERY important.
    #
    # It tells asyncio.gather() to return exceptions
    # as results instead of stopping the whole operation.
    results = await asyncio.gather(
        *tasks,
        return_exceptions=True
    )

    # List to store successful results.
    success = []

    # List to store failed results.
    failed = []

    # Match every ID with its corresponding result.
    for member_id, result in zip(ids, results):

        # Check whether the result is an exception.
        if isinstance(result, Exception):
            failed.append({
                "id": member_id,
                "error": str(result)
            })

        else:
            success.append(result)

    # Create the final result dictionary.
    final_result = {
        "success": success,
        "failed": failed
    }

    # Print a summary.
    print("\n========== Batch Fetch Summary ==========")

    # Number of successful requests.
    print(f"Successful: {len(success)}")

    # Number of failed requests.
    print(f"Failed:     {len(failed)}")

    print("=========================================")

    return final_result


# ------------------------------------------------------------
# Example usage
# ------------------------------------------------------------
async def main():

    ids = [1, 2, 3, 4, 5, 6]

    result = await batch_fetch(ids)

    print("\nFinal Result:")
    print(result)


# ------------------------------------------------------------
# Start the asynchronous program
# ------------------------------------------------------------
asyncio.run(main())
