# Pandas DataFrame constructor for DB cursor

We will be using the `memory_profiler` module to monitor memory usage.

To use `memory_profiler` simply run `mprof run <python_exec>`, and visualize with `mprof plot`. You can modify the interval of the memory checks with the `--interval` flag. For example `mprof run --interval 0.01 <python_exec>`.

The test database contains 10,000 rows and 3 columns of type TEXT, INTEGER, and REAL. You can quickly modify the database with `db_creator.py`.
