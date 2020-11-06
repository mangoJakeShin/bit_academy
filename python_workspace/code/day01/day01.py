'''
li = [10,20,30,40,50]

print(li[0:2])


print(li[4])

if a>b:
    print(a)
elif b>a:
    print(b)
else:
    print('same')

1. 3개의 수를 입력(input)하여 합과 평균 구하기

2. 3개의 수중 max값을 구하시오.

3. 합  : sum 함수로 만들기
  평균 : avg 함수로 만들기
  max  : max(mymax)함수로 만들기
  

'''
def mymax(a,b,c):
    
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return  b
        else:
            return c

a,b,c = map(int,input('a b c ').split())

s = a+b+c
avg = s/3.0

print('sum : {}, avg : {}'.format(s, avg))

print('max: ', mymax(a,b,c))       

ch = 'A'

print(ord(ch)^32)


'''
ch = 'B'

if 'A' <= ch <= 'Z':
    print(int(ch)^32);
'''








'''
s = 'i like Python'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

a="plus"

print("{}+%(aa)d = %(bb)d".format(a) %{'aa':10, 'bb':20})


print('{} {}'.format(10,'str'))

print('%d %s' %(10,'str'))
'''
"""
a=10
b=10

print(a,b)
print(str(a) + str(b))
print('{} + {}'.format(a,b))
print('%d + %d = %d' %(a,b,a+b))

print('{} + %d = {}'.format(a,a+b) %(b))
"""
'''
#c : printf
#java : System.out.printf


str1 = "First String"
str2 = "Second String"
print(str1 + str2)
print(str1*3)
print(str1[2])
print(str2[2:5])
print(len(str2))
print(str1[::-1])

print(str1[0:5:2])

print(str1[::2])
print(str1[-1:-3:-1])
print(str1)
print(str1[:])



print(~5)




a=12
b=5
a^=b
b^=a
a^=b

print(a,b)

a=10
b=5
 
print(a,b)
t=a
a=b
b=t
print(a,b)

a,b=b,a
print(a,b)
'''


'''

a='abc xyz k/b/s'

x,y,z = a.split('/')

print(x,y,z)




#     0123456789
t1 = 'ABCabc123A'
t2 = '123'

print(t2.isalpha())
print(t2.isdigit())
print(t2.isalnum())
print(t2.isupper())
print(t2.islower())

print(t1.count('A'))
print(t1.find('B'))
print(t1.rfind('z'))
#print(t1.rindex('z'))

print(t1.replace('A', 'Z'))

print(t1)

a="aBc"
print(a.upper())
print(a.lower())
'''
'''
print(2**1024)

#print(2+'a')
print(str(2)+'a')

print('=' * 20)

print('=' * 20)
'''




'10더하기 5는 15입니다.'
"10더하기 5는 15입니다."
'''10더하기 5는 15입니다.'''
a="""0더하기 5는 15입니다."""

"""
print(a)
a=10
b=5

print(a,'더하기', b,'는', a+b,'입니다.')

print(str(a)+'더하기') #casting : 형변환

print('{1}더하기 {0}는 {2}입니다.'.format(a, b, a+b))

print(a, end='')
print('더하기')


b="a b c"
c=b.split()
print(c)

a = ['a', 'b', 'c']
print(a)

b="my:name:is"
c=b.split(':')
print(c)
dd = '*'.join(c)
print('*'.join(c))
print(dd)
#
a=int(input("Num 1 : "))
b=int(input("Num 2 : "))
print(a+b)

c = input("Num 3 :  ")

print(c)
x = c.split()
print(x)
"""
'''
li="10 20 30"
li = li.split() #li = ['10','20','30]
t = map(int, li)
print(type(t))
a, b, c = t
print(type(a))
print(a,b,c)
'''
'''
a, b, c = map(int, input('a b c :').split())
print(a+b+c)
'''
'''
a=9
if a%2 == 0 :
    print('even number')
else :
    print("odd number")
'''
#함수    y=f(x) :  출력= f(입력)
'''

def func_1(): #함수의 정의 (자동차 정의)
    print("func_1")

func_1() #함수의 호출(자동차 사용)

def func_2(num):
    print(num,'값입니다.')

func_2(200)

def func_3():
    return 10
result = func_3()
print(result)

def func_4(a, b):
    if a>b:
        return a
    else:
        return b

print(func_4(10,20))


print(10+20)

def add(a,b):
    return (a+b)*1.1

print(add(10,20))
'''





