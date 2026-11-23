import multiprocessing
import threading
import time


def make_tea(name, seconds):
    print(f"{name}: იწყება")
    time.sleep(seconds)
    print(f"{name}: მზადაა")


def cpu_task(n):
    while n > 0:
        n -= 1


def io_task(seconds):
    time.sleep(seconds)


def run_sequential(task, jobs):
    for job in jobs:
        task(job)


def run_threads(task, jobs):
    threads = []
    for job in jobs:
        thread = threading.Thread(target=task, args=(job,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


def run_processes(task, jobs):
    processes = []
    for job in jobs:
        process = multiprocessing.Process(target=task, args=(job,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


def measure(runner, task, jobs):
    start = time.perf_counter()
    runner(task, jobs)
    return time.perf_counter() - start


def print_comparison(task_name, task, jobs):
    runners = (
        ("თანმიმდევრულად", run_sequential),
        ("thread-ები", run_threads),
        ("პროცესები", run_processes),
    )
    results = [(label, measure(runner, task, jobs)) for label, runner in runners]
    sequential_time = results[0][1]

    cells = [
        f"{seconds:.2f} წმ ({sequential_time / seconds:.1f}x)"
        for _, seconds in results
    ]
    print(f"| {task_name} | {' | '.join(cells)} |")


def main():
    teas = [("მწვანე ჩაი", 1.0), ("შავი ჩაი", 1.5), ("ბალახის ჩაი", 2.0)]

    sequential_start = time.perf_counter()
    for name, seconds in teas:
        make_tea(name, seconds)
    sequential_time = time.perf_counter() - sequential_start
    print(f"თანმიმდევრულად: {sequential_time:.1f} წმ")

    threads = []
    threaded_start = time.perf_counter()
    for name, seconds in teas:
        thread = threading.Thread(target=make_tea, args=(name, seconds))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    threaded_time = time.perf_counter() - threaded_start
    print(f"thread-ებით: {threaded_time:.1f} წმ")
    print(f"დაჩქარება: {sequential_time / threaded_time:.1f}x")


    cpu_jobs = [10_000_000] * 4
    io_jobs = [1.0] * 4

    print("\n| ამოცანა | თანმიმდევრულად | thread-ები | პროცესები |")
    print("|---|---|---|---|")
    print_comparison("CPU-bound", cpu_task, cpu_jobs)
    print_comparison("I/O-bound", io_task, io_jobs)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
