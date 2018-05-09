import os
import sqlite3
import random

import click
from config import *


@click.group()
def entry_point():
    pass


@entry_point.command()
@click.option('--path-to-db', type=click.Path(), help='path to new db location', default=PATH_TO_DB)
@click.option('--table-name', type=click.STRING, help='table name', default=TABLE_NAME)
@click.option('--n-rows', type=click.INT, help='number of rows', default=N_ROWS)
def create_db(path_to_db, table_name, n_rows):
    try:
        os.remove(path_to_db)
    except FileNotFoundError:
        pass

    conn = sqlite3.connect(path_to_db)

    c = conn.cursor()

    c.execute("CREATE TABLE {} (name text, age integer, r_float real)".format(table_name))

    for i in range(n_rows):
        c.execute("INSERT INTO test_table VALUES ('name_{}', {}, {})".format(i % 10,
                                                                             random.randint(18, 80),
                                                                             random.uniform(0, 10)))
    conn.commit()
    click.echo('Created table {} in db {}, of shape ({}, 3)'.format(table_name, path_to_db, n_rows))
    conn.close()


if __name__ == '__main__':
    entry_point()
