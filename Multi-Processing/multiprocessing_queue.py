import multiprocessing as mp

NUM_OF_PRODUCTS = 50

def producer_func(queue):
    for i in range(NUM_OF_PRODUCTS):
        queue.put(i)
        print("Producer #", i)
    queue.put(None)

def consumer_func(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print("Consumer #", item)

if __name__ == '__main__':
    q = mp.Queue()

    producer = mp.Process(target=producer_func, args=(q,))
    consumer = mp.Process(target=consumer_func, args=(q,))

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
