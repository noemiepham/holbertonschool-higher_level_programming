#!/usr/bin/python3
"""Write a script that takes in the name
of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT *\
                         FROM cities AS ct \
                         INNER JOIN states AS st\
                         ON ct.state_id = st.id\
                         WHERE st.name = %s\
                         ORDER BY ct.id ", (sys.argv[4],))
    print(", ".join([ct[2] for ct in cur.fetchall() if ct[4] == sys.argv[4]]))
