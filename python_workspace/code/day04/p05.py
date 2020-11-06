import sqlite3
from lib.db.dba import getConn

def insert_1():
    conn = getConn()
    cur = conn.cursor()
    cur.execute('''
        insert into test values('hong',60,60,90)    
    ''')
    conn.commit()
    conn.close()

def insert_2(x,y,z,c):
    conn = getConn()
    cur = conn.cursor()
    ins_sql = 'insert into test values(?,?,?,?)'    #동적 쿼리
    cur.execute(ins_sql, (x,y,z,c))       #튜플 형태
    conn.commit()
    conn.close()

def insert_3():
    conn=getConn()
    cur = conn.cursor()
    li = [('수철', 92, 40, 20),('명수', 20,50,89)]
    ins_sql = 'insert into test values(?,?,?,?)'    #동적 쿼리
    cur.executemany(ins_sql,li)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    insert_1()
    insert_2('coffee',75,34,9)
    insert_3()