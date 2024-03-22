#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3])
    curs = connection.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    stats = curs.fetchall()
    for stat in stats:
        print(stat)
    curs.close()
    connection.close()
