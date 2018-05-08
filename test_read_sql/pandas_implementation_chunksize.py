import time
import sqlite3
import pandas as pd


time.sleep(1)
conn = sqlite3.connect('../test_db.db')

time.sleep(1)
df = pd.DataFrame(columns=['name', 'age', 'rand'])
for table in pd.read_sql('SELECT * FROM test_table', conn, chunksize=10000):
    df = pd.concat([df, table])
time.sleep(1)
