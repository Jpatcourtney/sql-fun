# importing from a CSV

# import the csv library
import csv

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    #open the csv file and assign to a variable
    employees = csv.reader(open('employees.csv', 'rU'))

    # create a new table
    #c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

    # insert data to new table
    c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)