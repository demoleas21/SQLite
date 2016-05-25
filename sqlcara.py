import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    vehicles = [
        ('Ford', 'Explorer', 2),
        ('Ford', 'Escape', 4),
        ('Honda', 'Accord', 3),
        ('Honda', 'Genesis', 5),
        ('Ford', 'F-150', 8)
    ]

    c. executemany("INSERT INTO cars VALUES(?, ?, ?)", vehicles)
