#!/usr/bin/python3
""" write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the
argument. But this time, write one that is safe from MySQLinjections!"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    query_rows = cur.fetchall()
    for state in query_rows:
        if state[1] == sys.argv[4]:
            print(state)
    cur.close()
    db.close()
