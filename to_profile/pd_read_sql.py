import sqlite3

import pandas as pd
from config import *


def main():
    conn = sqlite3.connect(PATH_TO_DB)
    if not CHUNKSIZE:
        df = pd.read_sql('SELECT * FROM {}'.format(TABLE_NAME), conn)
    else:
        df = pd.DataFrame(columns=['name', 'age', 'rand'])
        for table in pd.read_sql('SELECT * FROM {}'.format(TABLE_NAME), conn, chunksize=CHUNKSIZE):
            df = pd.concat([df, table])
    return df


if __name__ == '__main__':
    main()