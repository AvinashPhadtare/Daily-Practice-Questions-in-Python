# ========================= Question ========================
#
# Write an asynchronous Python program using asyncio.as_completed()
# to check multiple payment gateways concurrently.
#
# Each gateway has a different response time.
#
# Implement the following:
#
# 1. check_payment_gateway(gateway, delay)
#    - Simulate an API call using asyncio.sleep(delay).
#    - Return a dictionary containing:
#        gateway
#        status
#        response_time_s
#
# 2. check_all_gateways(gateways)
#    - Check ALL payment gateways concurrently.
#    - Use asyncio.as_completed() to process each result
#      as soon as that gateway finishes.
#    - Print each result immediately when it arrives.
#    - Do not wait for all gateways to finish before processing results.
#    - Return the fastest gateway overall.
#
# Gateway response times:
#
# Razorpay  -> 1.5 seconds
# PayU      -> 0.3 seconds
# Cashfree  -> 0.8 seconds
# Paytm     -> 2.1 seconds
# Stripe    -> 0.5 seconds
#
# ============================================================


import asyncio


# ------------------------------------------------------------
# Function 1: Simulate a payment gateway API call
# ------------------------------------------------------------
async def check_payment_gateway(gateway: str, delay: float) -> dict:

    # Simulate the time taken by the API to respond.
    # While this task is sleeping, other async tasks can run.
    await asyncio.sleep(delay)

    # Return the result of the simulated API call.
    return {
        "gateway": gateway,
        "status": "online",
        "response_time_s": delay
    }


# ------------------------------------------------------------
# Function 2: Check all gateways concurrently
# ------------------------------------------------------------
async def check_all_gateways(gateways):

    # Create an empty list to store all async tasks.
    tasks = []

    # Go through every gateway and its delay.
    for gateway, delay in gateways:

        # Create an async task for each gateway.
        # create_task() schedules the coroutine to run concurrently.
        task = asyncio.create_task(
            check_payment_gateway(gateway, delay)
        )

        # Store the task in the list.
        tasks.append(task)

    # This will store the fastest gateway.
    fastest = None

    # as_completed() gives us tasks in the order
    # in which they finish, NOT the order in which
    # they were submitted.
    for task in asyncio.as_completed(tasks):

        # Wait for the completed task and get its result.
        result = await task

        # Print the result immediately.
        print(
            f"{result['gateway']} -> "
            f"{result['status']} -> "
            f"{result['response_time_s']} seconds"
        )

        # The first completed task is the fastest gateway.
        if fastest is None:
            fastest = result["gateway"]

    # Return the fastest gateway.
    return fastest


# ------------------------------------------------------------
# Example usage
# ------------------------------------------------------------

gateways = [
    ("Razorpay", 1.5),
    ("PayU", 0.3),
    ("Cashfree", 0.8),
    ("Paytm", 2.1),
    ("Stripe", 0.5)
]


# Run the asynchronous function.
fastest_gateway = asyncio.run(
    check_all_gateways(gateways)
)


# Display the fastest gateway.
print(f"\nFastest gateway: {fastest_gateway}")
