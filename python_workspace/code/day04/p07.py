import sqlite3
from lib.db.dba import getConn

def update_1(n_name,o_name):
    conn = getConn()
    cur = conn.cursor()
    upt_sql = 'update test set name=? where name=?'
    cur.execute(upt_sql,(n_name, o_name))
    rs =cur.fetchmany(2)
    conn.commit()
    conn.close()

def update_2():
    pass

def delete_1(num):
    conn = getConn()
    cur = conn.cursor()
    del_sql = 'delete from test where kor<=?'
    cur.execute(del_sql,(num,))
    conn.commit()
    conn.close()
def delete_2(name):
    pass



if __name__ == '__main__':
    update_1("hong", '홍철')
    delete_1(95)