import time
import sqlite3
import pandas as pd


time.sleep(1)
conn = sqlite3.connect('../test_db.db')

time.sleep(1)
pd.read_sql('SELECT * FROM test_table', conn)
time.sleep(1)
