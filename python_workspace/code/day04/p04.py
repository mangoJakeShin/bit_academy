import sqlite3
from lib.db.dba import getConn
def create_table():
    conn=getConn()          #db와 접속 정보
    cur = conn.cursor()     #db를 보는 포인터
    cur.execute('''
        create table test(name text, kor int, eng int, mat int)    
    ''')
    conn.commit()   #데이터베이스의 변경사항 확정시킴
    conn.close()    #db 닫기

    

if __name__ == '__main__':
    create_table()
    














