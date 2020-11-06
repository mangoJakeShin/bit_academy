import sqlite3

from lib.db.dba import getConn

class db:
    conn = getConn('d:/phone.db')
    cur = conn.cursor()
    def createtable(self):
        db.cur.execute('create table tel(name text, telno text)')
    def inserttable(self):
        self.name = input('name : ')
        self.telno = input('no : ')
        self.ist_sql = 'insert into tel values(?,?)'
        db.cur.execute(self.ist_sql,(self.name,self.telno))
    def selecttable(self):
        self.sel_sql = 'select * from tel'
        db.cur.execute(self.sel_sql)
        rs = db.cur.fetchall()
        print('==출력==')
        for k,v in rs:
            print(k,v)
    def updatetable(self):
        self.upt_sql = 'update tel set=? where name=?'
        self.oname = input('old name? : ')
        self.nname = input('new name? : ')
        db.cur.execute(self.upt_sql,(self.oname,self.nname))

    def deletetable(self):
        self.del_sql = 'delete from tel where name=?'
        self.delname = input('delete who? : ')
        db.cur.execute(self.del_sql,(self.delname,))


def main():
    tt = db()   #실제 db를 위한 인스턴스 생성
    while True:
        n = input('a. Create table // 1. input 2. view 3. update 4. delete 5. end')
        if n=='a':
            tt.createtable()
        elif n=='1':
            tt.inserttable()
        elif n=='2':
            tt.selecttable()
        elif n=='3':
            tt.updatetable()
        elif n=='4':
            tt.deletetable()
        elif n=='5':
            tt.conn.commit()
            tt.conn.commit()
            break
    print('exit')

if __name__ == '__main__':
    main()