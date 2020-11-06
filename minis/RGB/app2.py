import os
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask_wtf.csrf import CSRFProtect
from minis.RGB.model import Myuser
from minis.RGB.model import db
from minis.RGB.forms import RegisterForm

id = 0

app = Flask(__name__)


#when templates directory is built and hello.html is made,
#we automatically move to hello.html when we enter 5000/ path

@app.route('/', methods=['GET','POST'])
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    print('hello')
    # current file directory
    basedir = os.path.abspath(os.path.dirname(__file__))
    # dbfile directory
    print('basedir:{}'.format(basedir))
    dbfile = os.path.join(basedir, 'db.sqlite')
    print('file:{}'.format(dbfile))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = 'YELLOWMANGO'

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host='127.0.0.1', port = 5000, debug= True)
    #app.run(host='0.0.0.0') 할 시 가능