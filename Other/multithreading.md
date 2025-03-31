## Multithreading in Python
Multithreading is a technique in which multiple threads run concurrently within a single process to perform tasks in parallel. This is useful for I/O-bound tasks, where the program spends more time waiting (e.g., downloading files, network requests, reading/writing files) rather than using the CPU.

Key Concepts of Multithreading
Thread – A lightweight process that runs independently.

GIL (Global Interpreter Lock) – Python has a GIL that allows only one thread to execute Python bytecode at a time, which limits the benefits of multithreading for CPU-bound tasks.

Threading Module – Python provides the threading module to work with threads.

Parallel vs. Concurrent Execution – Due to GIL, Python threads execute concurrently (taking turns) rather than truly parallel.

When to Use Multithreading
✅ Good for: I/O-bound tasks (e.g., web scraping, network requests, file I/O).
❌ Not effective for: CPU-bound tasks (e.g., heavy computations) due to the GIL. Use multiprocessing instead.