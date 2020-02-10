"""
Database model
~~~~~~~~~~~~~~~
Collects methods for database operations.
if this is run directly, creates database and table.

COLUMNS:
id             INT PRIMARY KEY     NOT NULL,
name           CHAR(64)            NOT NULL,
uuid           CHAR(36)            NOT NULL
"""
from os.path import join, dirname, exists
import sqlite3

from src.config import logger

DB_PATH = join(dirname(dirname(__file__)), 'db', 'storage_index.db')


def insert_to_index(name, uuid_):
    """
    Adds new file record to the index
    :param name: (str)
    :param uuid_: (str)
    :return (None):
    """
    logger.debug('Inserting key in index')
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO images (name, uuid) \
              VALUES (?, ?)", (name, uuid_))
        conn.commit()


def select_from_index(uuid_):
    """
    Retrrieves a file record from the index by unique id
    :param uuid_: (str)
    :return (iterable): a cursor, a sequence of tuples
    """
    logger.debug(f'Selecting key from index {uuid_}')
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute("SELECT id, name, uuid FROM images WHERE uuid=:uuid_", {'uuid_': uuid_})


if __name__ == '__main__':
    import sqlite3

    if exists(DB_PATH):
        raise ValueError('DB file already exists')

    with sqlite3.connect(DB_PATH) as conn:
        print('Database created and opened')

        conn.execute('''CREATE TABLE images
             (id            INTEGER PRIMARY KEY     AUTOINCREMENT,
             name           CHAR(64)            NOT NULL,
             uuid           CHAR(36)            NOT NULL);''')
        print('Table created successfully')

        conn.execute('''CREATE UNIQUE INDEX
            index_uuid ON images(uuid);''')
        print('Index created successfully')

