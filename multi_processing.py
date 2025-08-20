import time
import multiprocessing as mp

ITER_ROUND = 100_000_000
NUM_OF_TASKS = 4

# pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 + ...)
def calculate_pi(start: int, end: int) -> float:
    result = 0.0
    sign = start % 2 == 0
    for i in range(start, end):
        element = 1.0 / (float(i * 2) + 1.0)
        if sign:
            result += element
        else:
            result -= element
        sign = not sign

    return result * 4.0

def single_process() -> float:
    start_time = time.time()
    result = calculate_pi(0, ITER_ROUND)
    print(f"Single process time: {time.time() - start_time}")
    return result

def multi_process() -> float:
    start_time = time.time()
    params = []
    step = ITER_ROUND // NUM_OF_TASKS

    for i in range(0, ITER_ROUND, step):
        params.append((i, i + step))

    with mp.Pool(NUM_OF_TASKS) as pool:
        result = pool.starmap(calculate_pi, params)

    print(f"Multi process time: {time.time() - start_time}")

    return sum(result)

def main():
    print(f"PI = {single_process()}, with {ITER_ROUND} iterations")
    print(f"PI = {multi_process()}, with {ITER_ROUND} iterations")

if __name__ == '__main__':
    main()