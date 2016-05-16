# Assignment 3b - prompt the user

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect('newnum.db')

#create a cursor object used to execute SQL
cursor = conn.cursor()

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

# loop until Exit
while True:
    x = raw_input(prompt)

    if x in set(["1", "2", "3", "4"]):
        operation = {1: 'avg', 2: 'max', 3: 'min', 4:'sum'}[int(x)]

        cursor.execute("SELECT {}(num) from numbers".format(operation))

        get = cursor.fetchone()

        print operation + ": %f" % get[0]

    elif x == '5':
        print "EXIT"

        break