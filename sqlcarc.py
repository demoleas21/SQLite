import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * FROM cars WHERE Make='Ford'")

    row = c.fetchall()

    for r in row:
        print r[0], r[1], r[2]
