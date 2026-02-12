import asyncio

# Coroutine Function
async def fetch_data(id, delay):
    print(f"Fetching data id:{id}...")
    await asyncio.sleep(delay)
    print(f"Data Fetched id:{id}, delay:{delay}...")

    return f"Sample Data id: {id}"

async def main():
    print("Create Task1...")
    task1 = asyncio.create_task(fetch_data(id=1, delay=3))
    print("Task1 creation done...")

    print("Create Task2...")
    task2 = asyncio.create_task(fetch_data(id=2, delay=2))
    print("Task2 creation done...")

    print("Create Task3...")
    task3 = asyncio.create_task(fetch_data(id=3, delay=1))
    print("Task3 creation done...\n")

    # Does Coroutine Runs Concurrently, because create_task uses in here
    # It take max time ~= 3s
    result1 = await task1
    result2 = await task2
    result3 = await task3
    print("\n")

    print("result1 =", result1)
    print("result2 =", result2)
    print("result3 =", result3)

    print("Ended after await. \n")

asyncio.run(main())