import multiprocessing
import requests
import time

def downloadFile(name, url):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(fr"Other\files\file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")

url = "https://picsum.photos/2000/3000"
pros = []

# Start time
t1 = time.perf_counter()

if __name__ == '__main__':
    # Start processes
    for i in range(5):
        p = multiprocessing.Process(target=downloadFile, args=(i, url))
        p.start()
        pros.append(p)

    # Wait for all processes to complete
    for p in pros:
        p.join()

# End time
t2 = time.perf_counter()

# Print total time taken
print(f"Total Time: {t2 - t1} seconds")
