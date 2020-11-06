import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy

#current file direcory
basedir = os.past.abspath(os.path.dirname(__file__))

#dbfile path

dbfile = os.path.join(basedir,"db.sqlite")

conn =sqlite3.connect('/home/mango/Downloads/chadwick.db')
print("Opened successfully")

cursor = conn.execute("select yearID from Salaries Limit 10")

for row in cursor:
    print("YearID = ", row[0])

app = Flask(__name__)

app.config['SQLALCHEMY+DATABASE_URI']= 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Test(db.Model):
    __tablename__ = 'test_table'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.string(32), unique = True)

db.create_all()
