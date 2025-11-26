import multiprocessing as mp

def increment(shared_counter, lock):
    for i in range(100):
        with lock:
            shared_counter.value += 1

if __name__ == "__main__":
    shared_counter = mp.Value('i', 0)
    lock = mp.Lock()

    processes = [mp.Process(target=increment, args=(shared_counter, lock)) for _ in range(mp.cpu_count())]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"Result: {shared_counter.value}")
