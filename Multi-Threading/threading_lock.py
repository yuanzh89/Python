import threading

database_value = 0
lock = threading.Lock()

def update_database():
    global database_value

    with lock:
        database_value += 1

if __name__ == "__main__":
    threads = []

    for i in range(100):
        t = threading.Thread(target=update_database)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"Result: {database_value}")