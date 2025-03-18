import time

i = 0

start_time = time.time()
while(i < 50000):
    i += 1
elapsed_time_while = time.time() - start_time

start_time = time.time()
for j in range(50000):
    pass
elapsed_time_for = time.time() - start_time

print(f"While loop time: {elapsed_time_while:.6f} seconds")
print(f"For loop time: {elapsed_time_for:.6f} seconds")

