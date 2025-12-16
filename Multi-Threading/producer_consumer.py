import threading
import time
import queue
import random

NUM_PRODUCERS = 5
NUM_CONSUMERS = 5
EVENTS_PER_PRODUCER = 20
SENTINEL = None

event_queue = queue.Queue()


def producer_worker(producer_id: int):
    thread_name = f"Producer_{producer_id}"

    for i in range(EVENTS_PER_PRODUCER):
        event_name = f"Producer-{producer_id}: Event-{i}"
        time.sleep(random.uniform(0.1, 0.5))
        event_queue.put(event_name)
        print(f"[{thread_name}] ➡️ Sent: **{event_name}**")

    print(f"Producer-{producer_id} has finished")


def consumer_worker(consumer_id: int):
    thread_name = f"Consumer_{consumer_id}"

    while True:
        try:
            message = event_queue.get(block=True)
            if message is SENTINEL:
                event_queue.put(SENTINEL)  # Relays the signal
                print(f"[{thread_name}] 🛑 Received sentinel. Shutting down gracefully.")
                break  # Exit hte infinite loop

            print(f"[{thread_name}] 📬 Received: **{message}**")
            time.sleep(random.uniform(0.3, 0.8))
            event_queue.task_done()
        except Exception as e:
            print(f"[{thread_name}] ⚠️ An error occurred: {e}")
            break


if __name__ == "__main__":
    consumers = []
    for i in range(1, NUM_CONSUMERS + 1):
        c = threading.Thread(target=consumer_worker, args=(i,), name=f"Consumer-{i}")
        c.start()
        consumers.append(c)

    print("\n--- All Consumers are Listening ---\n")

    producers = []
    for i in range(1, NUM_PRODUCERS + 1):
        p = threading.Thread(target=producer_worker, args=(i,), name="Producer-{i}")
        p.start()
        producers.append(p)

    print("\n--- All Producers are Working ---\n")

    for p in producers:
        p.join()

    print("Main Thread: 🎯 **All producers have finished sending events.**")

    print("Main Thread: Waiting for all produced events to be consumed...")
    event_queue.join()
    print("Main Thread: ✅ All events consumed. Queue is empty.")

    print(f"Main Thread: Sending {NUM_CONSUMERS} sentinel signals to consumers...")
    for _ in range(NUM_CONSUMERS):
        event_queue.put(SENTINEL)

    for c in consumers:
        c.join()

    print("Main Thread: All consumer threads have been gracefully joined.")
    print("--- Program finished successfully. ---")
