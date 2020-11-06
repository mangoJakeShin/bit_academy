#temp.py

import datetime

import Adafruit_DHT as dht

#온습도센서 모듈에 따라 DHT11, DHT22 변경해야 함

#DHT센서의 핀번호 보통 4를 입력

h,t = dht.read_retry(dht.DHT11,4)

 

print (h)

print (t)

