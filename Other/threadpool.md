## Threadpool
A ThreadPool is a collection of pre-initialized worker threads that can be used to execute tasks concurrently. Instead of creating and managing threads manually, a thread pool allows efficient reuse of threads for multiple tasks.

## concurrent.futures
The ThreadPoolExecutor from the concurrent.futures module provides a high-level API for managing a thread pool.

## How executor.map(func, l) Works Internally
Tasks Start Concurrently:
When executor.map(func, l) is called, all tasks (func(1), func(3), func(4), and func(2)) start executing in separate threads simultaneously.

Blocking Behavior:

executor.map(func, l) waits for all tasks to complete, but it does not collect all results at once.

Instead, it yields results in the same order as input (l) when they complete.

Iterating Over results:

for result in results:
    print(result)

This does not instantly print all results because results is a generator.

Each result becomes available only when the corresponding function execution finishes.

Since func(n) has time.sleep(n), each result takes time to complete before being printed.