import time
from concurrent.futures import ThreadPoolExecutor

def func(delay):
    print(f"waiting for {delay} seconds.")
    time.sleep(delay)
    return delay


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        l = [1,3,4,2]
        time1 = time.perf_counter()
        results = executor.map(func,l) #Starts all the functions concurrently. it blocks until all tasks are completed before proceeding to the next line of code.
        for result in results:
            print(result)
        time2 = time.perf_counter()
        print(time2-time1) # Prints 4
poolingDemo()