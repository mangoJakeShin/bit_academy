from PyQt5 import uic
import sys
import cv2
from matplotlib import pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
import os
from PIL import Image
import random



form_class = uic.loadUiType("baseball.ui")[0]

class MyApp(QWidget,form_class):
    trycount = 0
    tries = [0, 0, 0]
    target = []
    targnum = []
    ball = 0
    strike = 0
    trueval = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.randrand()
        self.show()

    def initUI(self):
        self.submitbtn.clicked.connect(self.get_text)

    def get_text(self):
        self.wrongtype()
        #올바른 값이 들어올 경우 실행
        if self.trueval:
            self.play()

    def play(self):
        self.zeroappend()
        self.ball_counter()
        self.set_col()
        self.strikes()

    def set_col(self):
        self.statustable.setItem(self.trycount, 0, QTableWidgetItem("{} {} {}".format(self.tries[0],self.tries[1],self.tries[2])))
        self.statustable.setItem(self.trycount, 1, QTableWidgetItem("{} B {} S".format(self.ball,self.strike)))
        self.trycount += 1

    def randrand(self):    #숫자를 생성시켜주는 메소드
        targnum = 3
        for i in range(0,targnum):
            self.randmaker()
        print(self.target)

    def randmaker(self):    #사용자가 지정한 자리수의 숫자를 만드는 메소드
        a = random.randrange(0,10)  #랜덤 변수 1개 생성
        while (1):
            if (a in self.target): #중복값일 경우 다시 생성
                a = self.newmaker()
            else:
                break       #중복값이 아닐 경우 중지
        self.target.append(a)  #생성한 숫자를 리스트에 추가

    def newmaker(self):  # 중복값일 경우 재생성 시켜주는 메소드
        a = random.randrange(0, 10)
        return a

    def ball_counter(self):  # 볼은 스트라이크보다 맞추기가 쉬움.
        self.ball = 0
        self.strike = 0

        for i in range(0, len(self.tries)):
            if (self.tries[i] in self.target):  # 만약 숫자가 타겟 리스트에 있을 경우
                self.ball += 1  # 볼 1개 추가 후
                self.strike_counter(self.tries[i], self.target[i])  # 스트라이크 검출기에 리스트 값을 넘김


    def strike_counter(self, a, b):
        if a == b:  # 리스트에 있는 값이 같을 경우 같은 자리수를 공유중인 것임
            self.strike += 1
            self.ball -= 1

    def divider(self, num):  # 여러자리의 숫자를 편하게 리스트에 넣기 위한 메소드
        print("into divider")
        self.tries.clear()
        #재귀함수 사용 불가...?
        # if (a > 10):
        #     b = a % 10
        #     self.divider(self.tries, a // 10)
        #     self.tries.append(b)
        # else:
        #     self.tries.append(a)

        a = num // 100
        b = num % 100
        c = b % 10
        b = b // 10
        if ((a < 10) and (b < 10) and (c<10)):
            self.tries.append(a)
            self.tries.append(b)
            self.tries.append(c)
        else:
            pass

    def zeroappend(self):  # 유저가 0을 먼저(0123) 입력할 경우 자동으로 0번째 인덱스에 추가해주는 기능
        if len(self.tries) != 3:
            self.tries.insert(0, 0)

    def strikes(self):
        if ((self.strike) == 3):
            self.inputcol.setText("congratz! won the game!")

            self.quiter()
        else :
            self.inputcol.setText("")


    def quiter(self):
        time.sleep(1)
        app.quit()

    def wrongtype(self):
        self.trueval = 0
        #에러 처리
        a = self.inputcol.text()
        # a 값을 형변환 할 수 없을경우 출력
        try:
            a = int(a)
            self.divider(a)
            print(self.tries)
            if (len(self.tries) != 3):
                self.inputcol.setText("input three numbers only")
            else :
                self.trueval = 1
        except:
            self.inputcol.setText("wrong input. put three numbers")
            self.trueval = 0




if __name__ == '__main__':


    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

























