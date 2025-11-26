import multiprocessing as mp
import time
import os

def custom_func(name):
    print(f"Process {name}: starting, PID: {os.getpid()}")
    process_start_time = time.time()
    time.sleep(2)
    print(f"Process {name}: PID: {os.getpid()} finished in {time.time() - process_start_time} seconds")

if __name__ == "__main__":
    print(f"Main Process ID: {os.getpid()}")

    # Create process objects
    p1 = mp.Process(target=custom_func, args=("p1",))
    p2 = mp.Process(target=custom_func, args=("p2",))

    start_time = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"All processes done in {time.time() - start_time} seconds")