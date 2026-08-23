# ========================= Question =========================
#
# Simulate an async task processing system for a gym.
#
# Tasks:
# - Generate 10 random gym-related tasks.
# - Example:
#   "send_reminder:1"
#   "process_payment:2"
#   "send_reminder:3"
#
# Build:
#
# 1. An async producer:
#    - Generate tasks one by one.
#    - Add each task to an asyncio.Queue.
#    - Wait 0.1 seconds after adding each task.
#
# 2. An async consumer:
#    - Take tasks from the queue.
#    - Process each task.
#    - Wait 0.3 seconds while processing.
#    - Print the processing result.
#
# 3. Run:
#    - 1 producer
#    - 3 consumers
#    - All concurrently.
#
# 4. Use asyncio.Queue.
#
# 5. After producing all tasks, the producer must signal
#    the consumers to stop using sentinel values.
#
#    Since there are 3 consumers, send 3 sentinel values.
#
# =============================================================


import asyncio
import random


# List of possible gym tasks
TASK_TYPES = [
    "send_reminder",
    "process_payment",
    "update_membership",
    "generate_report",
    "send_notification"
]


# -------------------------------------------------------------
# Producer
# -------------------------------------------------------------
# The producer creates tasks and puts them into the queue.
async def producer(queue):

    # Generate 10 tasks
    for i in range(1, 11):

        # Randomly select a task type
        task_type = random.choice(TASK_TYPES)

        # Create the task
        task = f"{task_type}:{i}"

        # Add task to the queue
        await queue.put(task)

        print(f"Producer added: {task}")

        # Wait 0.1 seconds before creating the next task
        await asyncio.sleep(0.1)

    # We have 3 consumers.
    # Therefore, we need 3 sentinel values.
    for _ in range(3):

        # None is our sentinel value.
        # It tells a consumer that there are no more tasks.
        await queue.put(None)

    print("Producer finished producing tasks.")


# -------------------------------------------------------------
# Consumer
# -------------------------------------------------------------
# Each consumer continuously takes tasks from the queue
# and processes them.
async def consumer(queue, consumer_id):

    while True:

        # Get the next task from the queue
        task = await queue.get()

        # Check whether the task is the sentinel value
        if task is None:

            print(f"Consumer {consumer_id} stopped.")

            # Tell the queue that this item is finished
            queue.task_done()

            # Exit the consumer
            break

        # Simulate task processing
        print(f"Consumer {consumer_id} processing: {task}")

        # Processing takes 0.3 seconds
        await asyncio.sleep(0.3)

        # Print processing result
        print(f"Consumer {consumer_id} completed: {task}")

        # Tell the queue that this task has been processed
        queue.task_done()


# -------------------------------------------------------------
# Main function
# -------------------------------------------------------------
async def main():

    # Create an asynchronous queue
    queue = asyncio.Queue()

    # Create the producer task
    producer_task = asyncio.create_task(
        producer(queue)
    )

    # Create 3 consumer tasks
    consumer_tasks = [
        asyncio.create_task(
            consumer(queue, 1)
        ),
        asyncio.create_task(
            consumer(queue, 2)
        ),
        asyncio.create_task(
            consumer(queue, 3)
        )
    ]

    # Wait for the producer to finish
    await producer_task

    # Wait until all items in the queue are processed
    await queue.join()

    # Wait for all 3 consumers to stop
    await asyncio.gather(*consumer_tasks)

    print("All tasks completed.")


# -------------------------------------------------------------
# Program entry point
# -------------------------------------------------------------

# Start the async event loop and run main()
asyncio.run(main())
