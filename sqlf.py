# SELECT statement without unicode chars

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    c.execute("SELECT firstname, lastname from employees")

    #fetchall() retrieves all records
    rows = c.fetchall()

    # output the rows to screen, row by row
    for r in rows:
        print r[0], r[1]