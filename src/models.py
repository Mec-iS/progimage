"""
Database model
~~~~~~~~~~~~~~~

if run directly, creates the table.
"""
from os.path import join, dirname, exists
DB_PATH = join(dirname(dirname(__file__)), 'db', 'storage_index.db')

if __name__ == '__main__':
    import sqlite3

    if exists(DB_PATH):
        raise ValueError('DB file already exists')

    conn = sqlite3.connect(DB_PATH)
    print('Database created and opened')

    conn.execute('''CREATE TABLE images
             (id            INT PRIMARY KEY     NOT NULL,
             name           CHAR(64)            NOT NULL,
             uuid           CHAR(36)            NOT NULL);''')
    print('Table created successfully')

    conn.close()
