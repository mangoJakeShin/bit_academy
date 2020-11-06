import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


def GPon(a,b):
    GPIO.output(a,True)
    time.sleep(b)
def GPoff(a,b):
    GPIO.output(a,False)
    time.sleep(b)

def GPctrl(gpnum,on,off):
    GPon(gpnum,on)
    GPoff(gpnum,off)

while(True):
    GPctrl(17, 1, 0.2)
    GPctrl(6, 1, 1)
    GPctrl(26, 1, 1)
