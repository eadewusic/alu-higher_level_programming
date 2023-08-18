#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
Your script should take 4 arguments: mysql username, mysql password,
database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server
running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], password=sys.argv[2],
                               database=sys.argv[3], use_unicode=True)
    name = sys.argv[4]
    c = database.cursor()
    c.execute("""SELECT cities.name
               FROM cities INNER JOIN states
               ON states.id = cities.state_id
               WHERE states.name = %s
               ORDER BY cities.id ASC;""", (name,))
    rows = c.fetchall()
    if rows == ():
        print()
    else:
        for i in range(len(rows)):
            if i < len(rows) - 1:
                print(rows[i][0], end=", ")
            else:
                print(rows[i][0], end="\n")
    c.close()
