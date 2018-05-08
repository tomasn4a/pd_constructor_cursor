import sqlite3
import random

conn = sqlite3.connect('test_db.db')

c = conn.cursor()

c.execute('''CREATE TABLE test_table
             (name text, age integer, r_float real)''')

for i in range(10000):
    c.execute("INSERT INTO test_table VALUES ('name_{}', {}, {})".format(i%10, random.randint(18, 80), random.uniform(0, 10))

conn.commit()

conn.close()
