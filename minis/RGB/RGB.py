from flask import Flask, render_template
from gpiozero import LEDBoard
import Adafruit_DHT
from minis.RGB.model import db
from minis.RGB.model import Myuser
import datetime



app = Flask(__name__)
id = 0
now = datetime.datetime.now()


# leds의 핀번호 정의(BCM 핀번호)
leds = LEDBoard(14, 15, 18)

# leds의 상태 정보 저장을 위한 데이터
led_states = {
        'red':0,
        'green':0,
        'yellow':0
}

@app.route('/')
def hello():
    return 'Hello World!'

# ex) 192.168.1.57:5000/red/0
@app.route('/<color>/<int:state>')
def led_switch(color, state):
    led_states[color] = state
    leds.value = tuple(led_states.values())

    myuser = Myuser()
    myuser.id = id
    myuser.time = str(now)

    myuser.red = 0
    myuser.yellow = 0
    myuser.green = 0

    if color == 'red':
        myuser.red = leds.value
    elif color == 'yellow':
        myuser.yellow = leds.value
    elif color == 'green':
        myuser.green = leds.value

    db.session.add(myuser)
    db.session.commit()
    id += 1


    return render_template('index.html', led_states=led_states)



@app.route('/all/<int:state>')
def all_on_off(state):
    myuser = Myuser()

    if state is 0:
        led_states={
            'red':0,
            'green':0,
            'yellow':0
        }
        myuser.red = 0
        myuser.yellow = 0
        myuser.green = 0
        myuser.id = id
        myuser.time = str(now)

    elif state is 1:
        led_states={
            'red':1,
            'green':1,
            'yellow':1
        }
        myuser.red = 1
        myuser.yellow = 1
        myuser.green = 1
        myuser.id = id
        myuser.time = str(now)

    db.session.add(myuser)
    db.session.commit()
    id += 1

    leds.value=tuple(led_states.values())
    return render_template('index.html', led_states=led_states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

