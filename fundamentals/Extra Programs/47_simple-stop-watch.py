import time

input("Press Enter to start stopwatch...")

start_time = time.time()

input("Press Enter to stop stopwatch...")

end_time = time.time()

total_time = end_time - start_time

print(f"Elapsed Time: {total_time:.2f} seconds")
