from lib.db.mdba import getConn

def create_table():
    conn = getConn()
    cur = conn.cursor()
    conn.commit()
    cur.execute("""
    create table score(
    name varchar(10),
    kor int,
    eng int,
    mat int)    
    """)
    conn.close

def insert_a():
    conn = getConn()
    cur = conn.cursor()
    ins_query='insert into score value(%s, %s, %s, %s)'

    cur.execute(ins_query,('jake', 80,70,60))
    conn.commit()
    conn.closef

def insert_b():
    conn = getConn()
    cur = conn.cursor()
    li = [('hong', 70,80,90),('chul',80,56,98),('soo',85,86,97)]
    ins_query='insert into score value(%s, %s, %s, %s)'
    cur.executemany(ins_query,li)
    conn.commit()
    conn.close


# def insert_c():
#     conn = getConn()
#     cur = conn.cursor()
#     # li = [('', , , ),]
#     ins_query='insert into score value(%s, %s, %s, %s)'
#     cur.executemany(ins_query,li)
#     conn.commit()
#     conn.close


def insert_li():
    pass

def select_a():
    conn = getConn()
    cur = conn.cursor()
    sel_sql = 'select * from score'
    cur.execute(sel_sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.commit()
    conn.close

def select_b(name):
    conn = getConn()
    cur = conn.cursor()
    sel_sql = 'select * from score where name like %s'
    cur.execute(sel_sql,(name,))
    rs = cur.fetchall()
    display(rs)
    conn.commit()
    conn.close

def update_a(oname,nname):
    conn = getConn()
    cur = conn.cursor()
    upt_sql = 'update score set name=%s where name=%s'
    cur.execute(upt_sql,(nname,oname))
    conn.commit()
    conn.close

def update_b(name,kor):
    conn = getConn()
    cur = conn.cursor()
    upt_sql = 'update score set kor=%s where name=%s'
    cur.execute(upt_sql,(kor,name))
    conn.commit()
    conn.close

def update_c(name,eng):
    conn = getConn()
    cur = conn.cursor()
    upt_sql = 'update score set eng=%s where name=%s'
    cur.execute(upt_sql,(eng,name))
    conn.commit()
    conn.close

def update_d(name,mat):
    conn = getConn()
    cur = conn.cursor()
    upt_sql = 'update score set mat=%s where name=%s'
    cur.execute(upt_sql,(mat,name))
    conn.commit()
    conn.close

def delete_a(name):
    conn = getConn()
    cur = conn.cursor()
    del_sql = 'delete from score where name=%s'
    cur.execute(del_sql,(name,))
    conn.commit()
    conn.close


def display(rs):
    for i, ai in enumerate(rs):
        print("이름 : ", ai[0],
              '/kor',ai[1],
              '/eng',ai[2],
              '/mat',ai[3],'\n',
              '//총점: ', (ai[1]+ai[2]+ai[3]))


if __name__ == '__main__':
    # create_table()
    # insert_a()
    # select_b('chul')
    # insert_b()
    # delete_a('chul')
    update_d('chul', '90')

# conn = getConn()
# print(conn)