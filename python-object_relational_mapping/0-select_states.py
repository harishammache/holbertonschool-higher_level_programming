#!/usr/bin/python3
import MySQLdb
import sys
""" lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    """function list_states with 3 arguments"""
    connection = MySQLdb.connect(host='localhost', port='3306',
                                 user=sys.argv[1], passw=sys.argv[2],
                                 data=sys.argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    stats = cursor.fetchall()
    for stat in stats:
        print(stat)
    cursor.close()
    connection.close()
