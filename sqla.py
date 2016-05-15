# script to create a SQLite3 database and table

# import the SQLite3 library
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object for executing SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population (city TEXT, state TEXT, population INT)""")

# close the database connection
conn.close()