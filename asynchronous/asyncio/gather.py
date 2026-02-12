import asyncio

# Coroutine Function
async def fetch_data(id, delay):
    print(f"Fetching data id:{id}...")
    await asyncio.sleep(delay)
    print(f"Data Fetched id:{id}, delay:{delay}...")

    return f"Sample Data id: {id}"


async def main():

    # Coroutine Functions Runs through await By gather for Concurrently Execution
    print("Create Tasks...")
    tasks = asyncio.gather(
        fetch_data(id=1, delay=3),
        fetch_data(id=2, delay=2),
        fetch_data(id=3, delay=1)
    )
    print("Task Created Done...")

    print("\n")
    results = await tasks

    print("results =", results)

asyncio.run(main())