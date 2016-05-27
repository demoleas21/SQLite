"""User Aggregations"""

import sqlite3

prompt = """
Select the operation that you want to perform:
1: Average
2: Max
3: Min
4: Sum
5: Exit
"""

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    while True:
        # Ask user to enter '1'(avg), '2'(max), '3'(min), '4'(sum) or '5' to exit
        user_choice = int(raw_input(prompt))

        # Perform aggregation
        if user_choice == 1:
            c.execute("SELECT avg(num) FROM numbers")
        elif user_choice == 2:
            c.execute("SELECT max(num) FROM numbers")
        elif user_choice == 3:
            c.execute("SELECT min(num) FROM numbers")
        elif user_choice == 4:
            c.execute("SELECT sum(num) FROM numbers")
        elif user_choice == 5:
            print "Exit"
            break

        result = c.fetchone()
        print result[0]
