"""Create a table and populate it"""

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    cities = [
        ('New York City', 'Northeast'),
        ('San Francisco', 'West'),
        ('Chicago', 'Midwest'),
        ('Houston', 'South'),
        ('Phoenix', 'West'),
        ('Boston', 'Northeast'),
        ('Los Angeles', 'West'),
        ('Houston', 'South'),
        ('Philadelphia', 'Northeast'),
        ('San Antonio', 'South'),
        ('San Diego', 'West'),
        ('Dallas', 'South'),
        ('San Jose', 'West'),
        ('Jacksonville', 'South'),
        ('Indianapolis', 'Midwest'),
        ('Austin', 'South'),
        ('Detroit', 'Midwest')
    ]

    c.execute("CREATE TABLE regions(city TEXT, region TEXT)")
    c.executemany("INSERT INTO regions VALUES(?, ?)", cities)
