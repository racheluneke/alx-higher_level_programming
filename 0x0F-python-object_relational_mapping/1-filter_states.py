i#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    script takes 3 arguments:
    mysql username, mysql password, database name
    """
    db_connect = MySQLdb.connect(host='localhost',
                                 user=argv[1], port=3306,
                                 passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states ORDER BY id")

    [print(states) for states in db_cursor.fetchall() if states[1][0] == 'N']
