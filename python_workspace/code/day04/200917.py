# def view():
#     print('view start')
#     print('view')
#     print('view end')
#
# view()
#
# def explain(func):
#     def wrapper():
#         print(func.__name__, 'function activate')
#         func()
#         print(func.__name__, 'function end')
#     return wrapper()
#
# # def view():
# #     print('view')
# # a = explain(view)
# # a
#
# @explain
# def view():
#     print('view')
#
# view
#
# @explain
# def show():
#     pass
#
# show
#
# class MyString:
#
#     def __init__(self, s):
#         self.s = s
#
#     def __truediv__(self, other):
#         return self.s.split(other)
#     def __mul__(self, other):
#         return self.s * other

# s = MyString('Python Programmer is Good')
# t = s / ' '
# print(type(t))
# print(t)
# print(MyString("python")*3)
# class car:
#     def __init__(self, hp):
#         self.hp = hp
#     def __add__(self, other):
#         if isinstance(other, car):  #(instance, classname)
#             return car(self.hp  + other.hp)
#         elif isinstance(other, int):
#             return car(self.hp + other)
#     def __radd__(self,other):
#         return self.hp + other
# bmw = car(100)
# print(bmw+10)
# print((bmw+10).hp)
# print(10+bmw)

# f = open('D:/test.txt', 'w') #write attribute read
# for i in range(1,11):
#     f.write('{}번째\n'.format(i))
# f.close()
#
# f = open('D:/test.txt','r')
# li = f.readlines()
# for i in li:
#     print(i,end='')
# for idx, i in enumerate(li):
#     print('{} : {}'.format(idx+1, i), end= '')

# import sys
# args = sys.argv[1:]
# print(args,type(args))
#
#
# fr = open(args[0], 'r')
# fw = open(args[1],'w')
# text = fr.read()
# fw.write(text)

# from xml.etree.ElementTree import * # * -> 모든 변수, 함수, 클래스
#
# person = Element('person')      #<person> </person>
# name = Element('name')  #<name> </name>
# name.text = 'honggildong'   #<name> 'honggildong' </name>
# person.append(name)
#
# age = Element('age')    #<age> </age>
# age.text = '22'
# person.append(age)
#
# SubElement(person, 'address').text = '서울'
#
# tel = Element('tel')
# tel.text = '12341234'
# person.insert(1,tel)
#
# person.remove(age)
#
# person.attrib['date'] = "2020-09-17"
# dump(person)
# ElementTree(person).write('d:/test.txt')




# ElementTree(person).write('d:/test.txt')

# import xml.etree.ElementTree as EE
#
# f = EE.parse('d:/test.txt')
# root = f.getroot()
# print(root)
# print(root.tag)
#
# for i in root:
#     print(i.tag, i.text)
# print(root)
# print(root.attrib)

#json 파일    WAS(jsp, java, jquery, sorint, ajax...)

#json 파일 == dict 유사
#json 만들기
# li = [{'name':'홍철수', 'score':'90','Kor':'99', 'Eng':'100'},
#       {'name':'김영수', 'score':'90','Kor':'99', 'Eng':'100'},
#       {'name':'신짱구', 'score':'50','Kor':'49', 'Eng':'100'}]
# import json
# with open('d:/score.json','w') as f:
#     json.dump(li,f,ensure_ascii=False)

# import json
# with open('d:/score.json','r') as f:
#     data = json.load(f)
# # for i in data:
# #     print(i)
#
# for i in data:
#     sum = 0
#     for k,v in i.items():
#         print(k,v, end = ' ')
#         if isinstance(v,int):
#             sum += v
#     avg = sum //3
#     print(str(sum))
#     print('############')
# print(data)

from lib.mymath.cal import *

print(add(2,3))





























