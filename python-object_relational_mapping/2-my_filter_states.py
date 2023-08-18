#!/usr/bin/python3
"""
a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument.
Your script should take 4 arguments
mysql username, mysql password, database name and state
name searched (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running
on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""


if __name__ == "__main__":
    import sys
    import MySQLdb
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], password=sys.argv[2],
                               database=sys.argv[3], use_unicode=True)
    name = sys.argv[4]
    c = database.cursor()
    c.execute("""SELECT * FROM states WHERE name LIKE BINARY %s
               ORDER BY id ASC""", (name,))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
