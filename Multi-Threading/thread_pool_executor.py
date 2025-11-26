import concurrent.futures
import time

def fetch_url(url):
    print(f"Fetching {url}")
    time.sleep(1)  # Simulate network delay
    return f"Content of {url}"

urls = ["google.com", "youtube.com", "yahoo.com"]

if __name__ == "__main__":
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(fetch_url, urls))

    print(f"Result: {results}")
    print(f"Total time: {time.time() - start_time}")