import asyncio
import time

#This sychronous program takes 4 seconds 
# def fetch_data1():
#     print("Fetching data 1...")
#     time.sleep(2)
#     print("Data 1 fetched")

# def fetch_data2():
#     print("Fetching data 2...")
#     time.sleep(2)
#     print("Data 2 fetched")

# def main():
#     fetch_data1()
#     fetch_data2()
#     print("Continuing execution...")

# main()

#This Asynchronous program takes only 2 seconds

async def fetch_data1():
    print("Fetching data 1...")
    await asyncio.sleep(2)             # Simulating a network request
    print("Data 1 fetched")

async def fetch_data2():
    print("Fetching data 2...")
    await asyncio.sleep(2)             # Simulating a network request
    print("Data 2 fetched")

async def main():
    # Running both tasks concurrently
    await asyncio.gather(fetch_data1(), fetch_data2())
    print("Continuing execution...")

asyncio.run(main())
