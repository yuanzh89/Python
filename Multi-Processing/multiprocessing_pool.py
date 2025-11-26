import multiprocessing as mp
import time
import os

def square_number(n):
    print(f"Process PID: {os.getpid()} starting")
    process_start_time = time.time()
    time.sleep(2)
    print(f"Process PID: {os.getpid()} finished in {time.time() - process_start_time} seconds")
    return n * n

if __name__ == '__main__':
    NUM_PROCESSES = mp.cpu_count()
    print(f"Number of Processes: {NUM_PROCESSES}")

    numbers = list(range(1, 1 + NUM_PROCESSES))
    start_time = time.time()

    # Create a process pool with workers
    with mp.Pool() as pool:
        results = pool.map(square_number, numbers)

    print(f"Get results: {results} in {time.time() - start_time} seconds.")