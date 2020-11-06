import sqlite3
#
def getConn(dbpath):
#     #mydb.db 가 있으면 사용 / 없으면 새로 만듦
    conn = sqlite3.connect(dbpath)
    return conn     #접속 정보