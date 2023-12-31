#!/usr/bin/python3
"""Task 5 script to take in name of state and list cities
from  states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    mysql_username, mysql_password, mysql_db_name = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_db_name
    )
    cursor = db.cursor()
    query = """
    SELECT name FROM cities
    WHERE cities.state_id = (SELECT id FROM states WHERE name = %s)
    ORDER BY cities.id ASC"""
    all_states = cursor.execute(query, (argv[4],))
    flag = -1

    for row in cursor.fetchall():
        print(("" if flag == -1 else ", ") + row[0], end="")
        flag = 1
    print("")
    # Close the cursor and database connection
    cursor.close()
    db.close()
