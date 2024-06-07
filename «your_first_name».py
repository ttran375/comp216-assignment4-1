import time
import threading


def simulate_long_task(name: str):
    for _ in range(100_000):
        time.sleep(0.000_1)
    print(f"{name}: Task completed.")


def execute_sequentially(times: int):
    start_time = time.time()
    for i in range(times):
        simulate_long_task(f"Task {i + 1}")
    end_time = time.time()
    print(f"Sequential Execution Time: {end_time - start_time} seconds.")


def execute_with_threads(times: int):
    threads = []
    start_time = time.time()
    for i in range(times):
        thread = threading.Thread(target=simulate_long_task, args=(f"Task {i + 1}",))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Threaded Execution Time: {end_time - start_time} seconds.")


# Calling the functions
if __name__ == "__main__":
    # Call the sequential execution function 10 times
    print("Sequential Execution:")
    for _ in range(10):
        execute_sequentially(1)  # You can adjust the number of tasks if needed

    # Call the threaded execution function 10 times
    print("Threaded Execution:")
    for _ in range(10):
        execute_with_threads(1)  # You can adjust the number of tasks if needed
