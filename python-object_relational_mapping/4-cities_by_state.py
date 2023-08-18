#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server
running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], password=sys.argv[2],
                               database=sys.argv[3], use_unicode=True)
    c = database.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
               FROM cities INNER JOIN states
               ON states.id = cities.state_id
               ORDER BY cities.id ASC;""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
