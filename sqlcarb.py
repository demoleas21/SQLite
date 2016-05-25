import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE cars SET Quantity=6 WHERE MAKE='Honda'")
    c.execute("SELECT * FROM cars")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]
