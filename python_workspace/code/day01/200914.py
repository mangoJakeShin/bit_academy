"""
a = 0

print(a)


a=str(a) #casting : a를 스트링으로 형변환

print(a+'바보')

a=3
b=4
print('{}더하기 {}는 {}입니다.'.format(a,b,a+b))
print('{1}더하기 {0}는 {2}입니다.'.format(a,b,a+b))  #중괄호 안에 포맷 내부의 숫자 순서로 지정 가능
print('{}더하기 {}는 {}입니다.'.format(3,2,5))


print(a, end='')
print('더하기') #end='' 붙이면 한줄을 내리지 않고 두줄을 붙여서 출력

a = ['a', 'b', 'c']
print(a)

print(':'.join(a))
b='my name is'
b=b.upper()
c=b.split()
d='*'.join(c)
print(':'.join(c))
print(d)
x = input('input : ') #입력 
print(d.split(x))

a=int(input("num 1 : ")) #input = str, int()로 casting
b=int(input("num 2 : "))
print(a+b)

c= input('input 3 num: ')
c= c.split()
print(c)

c[1] = int(c[1])
c[2] = int(c[2])
c[0] = int(c[0])
c= c[0] + c[1] + c[2]
print(c)
"""
"""
li = "10 20 30"
li = li.split()
t = map(int, li)
a,b,c = t
print(a,b,c)
print(a+b+c)
print(type(t))


a, b, c = map(int, input('a b c : ').split())  #input = string, -> list(split) -> map -> int
print(a+b+c)
"""
"""
a = int(input())
if a%2 == 0 :
    print('even number')
else :
    print('X')
"""


"""
함수 y=f(x) : 출력 = f(입력)

함수 종류 4가지
    input     output
1.    x         x
2.    x         o
3.    o         x
4.    o         o

"""


"""
#함수 선언(정의) : def func_1()

#1
def func_1():
    print("func_1")

func_1()        #함수 호출

#2    
def func_2(num):
    print(num, '값입니다.')
func_2(199)


#3
def func_3():
    return 10
result = func_3()
print(result)


#4
def func_4(a,b):
    if a>b:
        return a
    elif a==b:
        return "equal"
    else:
        return b

a = int(input())
b = int(input())
print(func_4(b,a))


# 10% 추가 함수

def add(a,b):
    return (a+b) * 1.1
print(add(299,1))


# 1bit = 0 or 1
# 4bit = nibble ( x)
# 8 bit = 1 byte
"""



"""
비트의 음수화 : 1001   //'보수'
1. 첫자리 1 : 1001 : -1
2. 숫자반전 : 0110 -> +1 : 0111 : -7
3. 음수 -> 비트화 : 오른쪽 끝에 1이 나올때까지 유지 후 나머지 반전 : 0111 
"""
"""
예약어 목록
import keyword

print(keyword.kwlist)
"""


"""
#python에는 숫자 자리수 제한이 없음
a = 1
b = a == 1
print(type(b))

print(b+10)
print(True + True)


e = 2**1024
print(type(e))
"""


"""
a = 23
print(type(a))
print(isinstance(a, int)) 
 
b = 0b1101
c = 0o23
d = 0x23 
 
print(a, b, c, d)
"""

'''
float != integer
a=1.2

print(a.is_integer()) 
'''

"""
t1= 'ABCabc123A'
print(t1.isalpha())
print(t1.isdigit())
print(t1.isalnum())
print(t1.isupper())
print(t1.islower())

print(t1.index(str(t1.find('B'))))

x = str(t1.find('B'))
print(x)
t1.index('A')
"""

"""
a = 6
print(0 < a < 10) #타 언어에서는 불가능한 처리법. 아래와 같은 형태로 비교연산 실행
print(0 < a and a < 10) 

print('abed'>'abd')
"""
"""
a = 20 #not a => a = true 에서 not을 붙여 false
print(not a < 30) # false = 0, 0 < 30 의 결과 출력

print( a < 30 and a != 30)
"""
"""
a = 10
b = 5

t = a
a = b
b = t

#간편하게 a,b = b,a 로 가능

print(a,b)
a,b = b,a
print(a,b)
"""
"""
#shift 연산자
#비트를 한칸 이동시킴
a = 4<<1
print(a) #8 : 100 -> 1000
print(7<<1) #14 0111 -> 1110
print(7>>1) # 3 0111 -> 0011

#10 & 6 : 1010
#         0110
#         0010 => 논리 곱

# 10|6 :  1010
#         0110
#         1110  => 논리 합

#10^6 :     1010
#           0110
#           1100 : exclusive or : 같지 않으면 1
"""
"""
a = 3
b = 6
a^=b
b^=a
a^=b
print(a,b)
"""
"""
#0이 아닌 모든 숫자는 true

str1 = "First String"
str2 = "Second String"

print(str1 + str2)  #First StringSecond String
print(str1*3)       #First StringFirst StringFirst String
print(str1[2])      #r
print(str2[2:5])    #con
print(len(str2))    #13
print(str1[::-1])   #gnirtS tsriF : 처음부터 끝까지 거꾸로
print(str1[0:5:2])  #Frt : 시작점:끝점:띄는칸 -> 0번째부터 5번째까지 2칸씩 띄어
print(str1[::2])    #FrtSrn : 처음부터 끝까지 2칸씩 띄어서
print(str1[9:1:-1]) #irtS tsr 
print('a' + str1[0:9:-1]) #공백 : 거꾸로 출력시 0은 맨 뒤의 숫자(끝)이므로 시작점에 넣으면 안됨
print(str1[-1:6:-1])    #gnirt : 뒤에서 1번째 ~ 정상적으로 셌을 때 6번째
print(str1[-1:-3:-1]) #gn : 뒤에서부터 1번째에서 3번째까지
"""
"""
f = ' name : %s, age: %d'
print(f % ('dooley', 20))

f = 'name: %(name)s, age: %(age)d'
print(f) 

print(f % {'name': '둘리', 'age': 20}) 

a="plus"
print("{}+%(aa)d = %(bb)d".format(a) %({'aa':10,'bb':20}))

print('{} {}'.format(10,'str'))
print('%d %s' %(10, 'str'))
"""
'''
s = 'you like Python' 
 
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title()) 
 
ch = 'a'
if 'A' <= ch <= 'Z':
    print('upper')
'''
'''
li = [0, 0 ,0 ]
li[0] = int(input())
li[1] = int(input())
li[2] = int(input())

x = 0
sum = 0
avg = 0

while x < len(li):
    sum += li[x]
    x+=1
avg = sum/len(li)

max = 0

if li[0] < li[1]:
    max = li[1]
    if max < li[2]:
        max = li[2]
elif li[0] < li[2]:
    max = li[2]
else :
    max = li[0]

print(max)
print(avg)
print(sum)
'''

def funcMax(a, b, c):
    max = 0

    if a>b:
        if a>c:
            return a
        else :
            return c
    else :
        if b>c:
            return b
        else :
            return c

a,b,c = map(int,input('a b c').split())

s = a+b+c
avg = s/3.0

print('sum : {}, avg; {}'.format(s,avg))
print('max: ',funcMax(a,b,c))









































