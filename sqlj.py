#JOIN data from multiple tables

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    # fretrieve the data from two tables
    c.execute("SELECT DISTINCT population.city, population.population, regions.region FROM population, regions WHERE population.city = regions.city ORDER by population.city ASC")

    rows = c.fetchall()

    for r in rows:
        print "City:", r[0]
        print "Population:", r[1]
        print "Region:", r[2]
        print