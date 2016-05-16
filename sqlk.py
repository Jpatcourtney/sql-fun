# SQLite Functions

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    # creat a dictionary of Functions
    sql = {
        'average': "SELECT avg(population) FROM population",
        'maximum': "SELECT max(population) FROM population",
        'minimum': "SELECT min(population) FROM population",
        'sum': "SELECT sum(population) FROM population",
        'count': "SELECT count(city) FROM population"
        }

    # run each query item in the dictionary
    for keys, values in sql.iteritems():

        # run the sql Function
        c.execute(values)

        # fetchone() retrievs one record from the query
        result = c.fetchone()

        # output the results
        print keys + ":", result[0]