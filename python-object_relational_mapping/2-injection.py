#!/usr/bin/python3
"""
Testing sql injection
"""


if __name__ == "__main__":
    import sys
    import MySQLdb
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], password=sys.argv[2],
                               database=sys.argv[3], use_unicode=True)
    name = sys.argv[4]

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
ORDER BY id ASC".format(name)
    c = database.cursor()
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
