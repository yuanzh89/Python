import asyncio

# Coroutine and Task
async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def create_task():
    # Create tasks for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

async def gather():
    # Run coroutines concurrently and gather their return values
    # No built-in error handling
    # E.g.: if one task raises an error and failed, all other tasks will still run.
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))

    # Process the results
    for result in results:
        print(f"Received result: {result}")

async def task_group():
    tasks = []
    # Has built-in error handling.
    # E.g.: if one task raises an error and failed, task group will automatically cancel all other tasks.
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # After the Task Group block, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")

# Lock
# A shared variable
shared_resource = 0

# An asyncio lock
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        # Critical section starts
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1  # Modify the shared resource
        await asyncio.sleep(1)  # Simulate an IO operation
        print(f"Resource after modification: {shared_resource}")
        # Critical section ends

# Semaphore
async def access_resource(semaphore, resource_id):
    async with semaphore:
        # Simulate accessing a limited resource
        print(f"Access resource: {resource_id}")
        await asyncio.sleep(1)  # Simulate word with the resource
        print(f"Releasing resource: {resource_id}")

# Event
async def waiter(event):
    print("waiting for the event to be set")
    await event.wait()
    print("event has been set, continuing execution")

async def setter(event):
    await asyncio.sleep(2)  # Simulate doing some work
    event.set()
    print("event has been set")

async def main():
    # Coroutine and Task
    await create_task()
    await gather()
    await task_group()

    # Lock
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

    # Semaphore
    semaphore = asyncio.Semaphore(2)   # Allow 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))

    # Event
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

    # TODO: Add demo for asyncio Condition

asyncio.run(main())