import time

start_time = time.perf_counter()

# Your code goes here
for i in range(1000000):
    pass

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"Elapsed time : {elapsed_time:.1f} seconds")