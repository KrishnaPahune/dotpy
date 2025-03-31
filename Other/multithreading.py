import threading
import time

def func(delay):
    print(f"Waiting for {delay} seconds...")
    time.sleep(delay)

# def main():
#     time1 = time.perf_counter() #performance counter 
#     func(1)
#     func(3)
#     func(4)
#     func(2)
#     time2 = time.perf_counter()
#     print(time2-time1) #prints 10 after processing all functions one by one

# main()

#Same Code using threading

t1 = threading.Thread(target=func, args=[1])
t2 = threading.Thread(target=func, args=[3])
t3 = threading.Thread(target=func, args=[4])
t4 = threading.Thread(target=func, args=[2])

time1 = time.perf_counter()
# thread.start() will start the threads concurrently, print the print statements and push time consuming process in background
t1.start()
t2.start()
t3.start()
t4.start()

#This will be printed before the threads complete the processess pushed in the background
print("All the threads started")

#Wait for all the threads to finish their background processes
t1.join()
t2.join()
t3.join()
t4.join()
print("All processes finished")
time2 = time.perf_counter()
print(time2-time1) #this prints 4 since all the threads ran simultaneously
