# g_a = 1
# g_b = 'symbol'
#
#
# def f():
#     l_a = 2
#     l_b = 'table'
#     print(locals())
#
# for i in range(2):
#     g_c = 3
#     g_d = 'python'
#     print(locals())
#
# f()
# print(globals())


# def add20(a):
#     return a+20
#
# print(add20(2))
#
# add10 = lambda a: a+10
# print(add10(20))
#

# li = [1, 2, 3]
#
# def mul(x):
#     return x*10
# print(list(map(mul, li)))
#
# print(list(map(lambda  x: x*10, li)))

# ex = list(range(1,11))
# print(ex)
#
# for i in range(len(ex)):
#     if i%2 == 1:
#         ex[i] = "even"
#
# print(ex)
#
# li = list(range(1,11))
# print(list(map(lambda  x: 'even' if x%2==0 else x, li)))
#
# li = [-2,-1, 0,1,2]
# print(list(map(lambda x: "-" if x<0 else '+' if x>0 else x,li)))

#
# def func(x):
#     return x>3
# print(list(filter(func,[1,2,3,4,5,6,7,8])))
# #filter(함수, 리스트) : 함수에 정의된 조건에 맞게 true인 것만 반환
#
# print(func(10))
#
# print(list(filter(lambda x: x>3, [1,2,3,4,5,5])))

# from functools import reduce
#
# def func(x,y):
#     return x+y
# li = [1,2,3,4,5,6,7]
#
# print(reduce(func,li))

# x=10
# def f1():
#     global x    #전역변수 호출
#     x=20        #전역변수 변경
#     print(x)
#
# f1()
# print(locals())
# print(globals())
#
# def outter():
#     string = 'hello'
#     def inner_f():
#         print(string)
#     return inner_f()
# f = outter()    #클로져
# f
#
# def aaaa(text):
#     tag = text
#     def bbbb(ttt):
#         hhh = ttt
#         print('<{0}>{1}<{0}>{1}'.format(tag,ttt))
#     return bbbb
#
# f = aaaa('not')
# f('bbb')

# 1,2,3을 홀수로 만들어 1,3,5 값을 누적시키는 함수

# def adder():
#     w = 2
#     b = 1
#     tot = 0
#     def addnum(x):
#         nonlocal tot
#         tot = tot + x*w+b
#         print(tot)
#     return adder
# c = adder()
# c()

# class car:  #__init__ : special method, magic method, 초기화함수, 생성자
#     # def __init__(self, hd_size,pw): #인스턴스 생성시 자동 호출
#     # def __init__(self,*aarrggs):
#     #     self.handle=aarrggs[0]
#     #     self.power = aarrggs[1]
#         #변수를 입력해주는것에 제한이 없어짐
#
#     def __init__(self,**dictt):
#         self.handle = dictt['a']
#         self.power = dictt['b']
#
#     def display(self):
#         print('handle size: ' + str(self.handle))
#         print('마력 : ' + str(self.power))
#     def run(self):
#         print("달림")
#
#     def fast_run(self):
#         print("빠르게",end=" ")
#         self.run()
#
# bus = car(15,19)
# bus.run()
# bus.fast_run()
# print(bus.handle)
# bus.display()
#
# li = [0,20]
# sport = car(*li)
# sport.display()

# dd = dict(a=10,b=20)
# sedan = car(**dd)
# sedan.display()
#
# class car2: #파이썬은 비어있는 클래스 생성 가능
#     pass
#
# bus = car2()
# bus.numer = 10
# print(bus.numer)
#
#
#
# class car3:
#     __slots__ = ['number', 'power'] #나열된 2개의 속성만 허용
#
# buuus = car3()
# buuus.number = 20
# buuus.power = 30
#
# class car4:
#     def __init__(self):
#         self.aa=10
#         self.__bb=20    #__ 2개 : private
#     def __set__bb(self):    #비공개 메소드
#         print(self.__bb)
#     def show__bb(self):
#         self.__set__bb()
# truck = car4()
# truck.show__bb()

# class car:
#     number = []     #class variabe, 모든 인스턴스가 공유
#     __flag = 80     #비공개 클래스 변수
#
#     def add_num(self,x):
#         car.number.append(x)
#         # self.number+=x  #instance variable
#     def view_flag(self):
#         print(car.__flag)
#
# bus1 = car()
# bus2 = car()
#
# bus2.add_num(40)
# print(bus1.number)
#
# bus1.add_num(10)
# print(bus2.number)
#
# print(bus1.__dict__)
# print(car.__dict__) #속성이나 메소드를 찾는 순서
# bus1.view_flag()

# class car:
#     '''car class'''
#
#     def bonnet(self):
#         '''engine box'''
#         pass
# print(car.bonnet.__doc__)
# print(int.__doc__)
#
# class car:
#     @staticmethod #정적메소드
#     def add(a,b):
#         return a+b
#
# print(car.add(10,3))
#
# a={1,2}
# b={3,4}
# print(set.union(a,b))

# class car:
#     cnt = 0
#     def __init__(self):
#         car.cnt = car.cnt + 1
#     @classmethod    # @는 decorator
#     def view_cnt(cls):
#         print(car.cnt)
# car1 = car()
# car1.view_cnt()

# 상속

# class old_car:
#     def __init__(self):
#         self.power = 100
#     def run(self):
#         print('vroooong')
#     def dp_power(self):
#         print(self.power)
#
#
# class new_car(old_car):
#     def __init__(self): #생성자 함수 사용시 부모생성자의 명시적 호출
#         self.sport=1000
#         super().__init__()
#
# n1 = new_car()
# n1.dp_power()


# class old_car:
#     def __init__(self):
#         self.power = 100
#         self.sport = 800
#     def run(self):
#         print('vroooong')
#     def dp_power(self):
#         print(self.power)
#     def dp_sport(self):
#         print(self.sport)
#
# class new_car(old_car):
#     def __init__(self): #생성자 함수 사용시 부모생성자의 명시적 호출
#         self.sport=1000
#         super().__init__()
#     def run(self):  #if same method exists, 'overriding' happens
#         print('vrvrvrv')    #vroooong -> vrvrvrvr
#
# n1 = old_car()
# n2 = new_car()
# n1.dp_power()
# n1.run()
# n2.run()
# n1.dp_sport()
# n2.dp_sport()

# class sport:
#     def run(self):
#         print('sports mode')
# class sedan:
#     def run(self):
#         print('comfort mode')
# class car(sport,sedan): #다중 상속 시 왼쪽이 우선
#     pass
#
# my_car = sedan()
# your_car = sport()
# suv = car()
# suv.run()
#
# print(car.mro())

# from abc import *   #from module(file) : 추상크래스를 만들때 필요한 모듈
# class bone(metaclass=ABCMeta):  #추상 클래스 : 내용은 없고 포장만 있음
#     @abstractmethod
#     def wheel(self):
#         pass
#     @abstractmethod
#     def body(self):
#         pass
# class car(bone):    #추상클래스 상속받은 클래스는 모든 함수를 오버라이딩 해야 함
#     def wheel(self):
#         print('22inch')
#     def body(self):
#         print('titanium')
#
# bmw = car()
# bmw.wheel()

# def g(t):
#     t[0] = 0
#     print(id(t))
#
# a = [1, 2, 3]
# g(a)
# print(a)
# print(id(a))

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']


def clean_strings(strings):
    results = []
    for string in strings:
        string = string.strip()
        string = re.sub('[!#?]', '', string)
        string = string.title()
        results.append(string)
    return results
































