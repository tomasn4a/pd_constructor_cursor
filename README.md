# Pandas DataFrame constructor for DB cursor

## Create toy database
To create a toy sqlite database with a chosen number of rows and three columns of type TEXT, INTEGER, and REAL
run

    python cli.py create_db
 
 To see available parameters to `create_db` run `python cli.py create_db --help`
 
 ## Memory profiling
 Functions to be profiled live in the `to_profile` directory. We will use the 
 [memory_profiler](https://pypi.org/project/memory_profiler/) module to profile our memory usage. To profile a 
 python executable (for example, `to_profile/pd_read_sql.py`) at the desired interval (for example, 0.5 s)run:
 
     mprof run --interval 0.5 to_profile/pd_read_sql.py
     
 The profiler generates a `.dat` file that you can visualize with:
 
     mprof plot <.dat file>
     
 Omitting the `<.dat>` file above simply plots the latest profile generated.
 
 **Note**: `mprof` takes a python executable so it is not possible to pass arguments with argparse/click. Change
 parameters through the `config.py` file.