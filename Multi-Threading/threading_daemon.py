import threading
import time

def background_service():
    while True:
        print("Background service running...")
        time.sleep(1)

t = threading.Thread(target=background_service, daemon=True)
t.start()

time.sleep(10)
print("Main thread existing. Daemon dies now.")