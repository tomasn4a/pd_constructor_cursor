import sqlite3

conn = sqlite3.connect('test_db.db')

c = conn.cursor()

c.execute('SELECT * FROM test_table')

print(c.fetchall())
