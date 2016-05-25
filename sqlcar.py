"""SQL car test"""

import sqlite3

conn = sqlite3.connect("cars.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE cars
                (Make TEXT, Model TEXT, Quantity INT)
                """)

conn.close()
