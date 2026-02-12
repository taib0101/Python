import asyncio

# Coroutine function define with "async func"
async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay)
    print("Data Fetched... \n")

    return "Some Data"
    
async def main():
    
    print("Start of main coroutine.")
    task =  fetch_data(delay=3)
    print("Coroutine Function : ", task)
    print("End of main coroutine. \n")

    # await runs the coroutine and pauses here until it finishes 
    #   -- without blocking other tasks
    result = await task

    print("result =", result)
    print("Ended after await. \n")


# it creates a event loop
asyncio.run(main())
