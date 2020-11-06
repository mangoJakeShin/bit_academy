import sqlite3
from lib.db.dba import getConn

def select_1():
    conn=getConn()
    cur=conn.cursor()
    cur.execute('select * from test')
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()
def select_2():
    conn=getConn()
    cur=conn.cursor()
    cur.execute('select * from test where name="hong"')
    rs = cur.fetchall()
    for i in rs:
        print(i)
def select_3(name):
    conn=getConn()
    cur=conn.cursor()
    cur.execute('select * from test where name=?',(name,))
    rs = cur.fetchmany(6)
    for i in rs:
        print(i)


    conn.close()

if __name__ == '__main__':
    select_3(('hong'))