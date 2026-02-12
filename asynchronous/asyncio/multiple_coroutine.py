import asyncio

# Coroutine
async def fetch_data(id, delay):
    print(f"Fetching data id:{id}...")
    await asyncio.sleep(delay)
    print(f"Data Fetched id:{id}, delay:{delay}... \n")

async def main():

    print("Start of main coroutine.")

    task1 = fetch_data(id=1, delay=4)
    task2 = fetch_data(id=2, delay=3)

    print("End of main coroutine. \n")

    # await runs first coroutine function, 
    # first one in done, after it runs second coroutine function.
    # it takes time of (4+3) ~= 7s
    # and it doesn't run Concurrently
    # Concurrently: Multiple tasks are in progress during the same time period.
    # if needs to use concurrently, try asyncio.gather() or asyncio.create_task()

    result1 = await task1
    result2 = await task2

    print("result1 = ", result1)
    print("result2 = ", result2)
    print("\n")

    print("Ended after await. \n")

    return


asyncio.run(main())