"""Database Population"""

import sqlite3
import random

# Create a new database
with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # Create a new table
    c.execute("DROP TABLE if EXISTS numbers")
    c.execute("CREATE TABLE numbers(num INT)")

    # Generate random numbers and fill the database
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0, 100),))
