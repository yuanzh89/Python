import multiprocessing as mp
import time

NUM_OF_PROCESSES = mp.cpu_count()

def printer(item, lock):
    with lock:
        print(f"Item: {item}")
        time.sleep(0.1)

if __name__ == "__main__":
    lock = mp.Lock()
    processes = []

    start_time = time.time()

    for i in range(NUM_OF_PROCESSES):
        p = mp.Process(target=printer, args=(i, lock))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"All done in {time.time() - start_time} seconds.")