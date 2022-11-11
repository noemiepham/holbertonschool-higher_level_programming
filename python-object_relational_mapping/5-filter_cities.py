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
    cur.execute("SELECT ct.name\
                         FROM cities AS ct \
                         INNER JOIN states AS st\
                         ON ct.state_id = st.id\
                         WHERE st.name = %s\
                         ORDER BY ct.id ", (sys.argv[4],))
    query_rows = cur.fetchall()
    results = []
    for row in query_rows:
        for field in row:
            results.append(field)
    cur.close()
    db.close()
    for i in range(len(results)):
        if i == len(results) - 1:
            print("{}".format(results[i]))
        else:
            print("{}, ".format(results[i]), end="")
