import threading
import time

def sleep_task(name, duration):
    print(f"Thread {name} took {duration} seconds")
    time.sleep(duration)

if __name__ == '__main__':
    print("Main Thread Starting")

    t1 = threading.Thread(target=sleep_task, args=("T1", 2))
    t2 = threading.Thread(target=sleep_task, args=("T2", 2))

    start_time = time.time()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Main Thread Consumes: {time.time() - start_time} seconds")