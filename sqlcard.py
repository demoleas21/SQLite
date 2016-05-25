import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    vehicles = [
        ('Ford', 'Explorer', '2016-05-12'),
        ('Ford', 'Escape', '2014-02-29'),
        ('Honda', 'Accord', '2015-12-25'),
        ('Honda', 'Genesis', '2009-04-04'),
        ('Ford', 'F-150', '2002-09-19')
    ]

    c.execute("CREATE TABLE orders(Make TEXT, Model TEXT, Order_date TEXT)")
    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", vehicles)
    c.execute("""SELECT cars.Make, cars.Model, cars.Quantity, orders.Order_date
            FROM cars, orders WHERE cars.Model=orders.Model""")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]
        print r[2]
        print r[3], '\n'
