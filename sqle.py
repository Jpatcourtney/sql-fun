# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # us a for loop to iterate throught the database, printing the results
    for row in c.execute("SELECT firstname, lastname from employees"):
        print row