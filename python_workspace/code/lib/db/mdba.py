import mysql.connector

config = {
    'user': 'root',
    'password' : '1234',
    'host' : '127.0.0.1',
    'database' : 'pythondb',
    'port':'3306'

}

def getConn():
    conn = mysql.connector.connect(**config)
    return conn

def get_test(**con):    #(*?) : tuple, (**?) : dictionary 로 자동으로 전달
    print(con)

# get_test(a=1,b=2,c=3,d=5)

