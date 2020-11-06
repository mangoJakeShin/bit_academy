#200915

#    0123456789

#
# s = 'I Like Python. I Like Java Also'
# print(s.count('Like'))
#
# print(s.find('Like'))
# print(s.find('Like', 5))
# print(s.find('JS'))
# print(s.rfind('Like'))
#
# print(s.index('JS')) print(s.rindex('Like'))
#
# print(s.startswith('I Like'))
# print(s.startswith('Like', 2))
# print(s.endswith('Also'))
# print(s.endswith('Java', 0, 26)) #뒤에가 java로 끝나는지
#
#
#
# s = 'spam and ham'
# t = s.split()
# print(t)
#
# t = s.split('and')
# print(t)
#
# s2 = ":".join(t)
# print(s2)

#
# name = 'hong gil dong'
# email = 'daum.net'
#
# name2 = name.split()
# print(name2)
#
#

# print(''.isspace())

# # print('20'.zfill(5))
# f = 'name: {}, age: {}'
# print(f)
# print(
#     f.format("둘리", 10)
# )
# print('{:3}의 제곱근은{:.5}입니다.'.format(2,2**0.5))
# # :3 -> 3칸 할당 후 오른쪽부터 채움, :.5 -> 소수점 이하 5번째 자리 까지
#
# print('{1:05}의 제곱근은 {0:.5}입니다'.format(12**0.5,12))
# # :05 => 5칸 할당 후 빈칸은 0으로 채우기
#
#
# # list
# #     0  1   2
# li = [1, 2, 'python']
# #    -3 -2  -1
# print(li[-2],li[-1])
#
# print(li*2)
# print(li+[3,4,5])
# print(len(li))
# print(2 in li)
#
# del li[0]
# print(len(li))
# print(li)

#
#
# li = list()
# print(len(li))
#
# li = list(range(16, 10, -2))
# print(li)

# a = list(range(-20, 21,5))
# print(a)
#
# a = list
# b = int(input("start"))
# c = int(input("end"))
# d = int(input("interval"))
#
#
# a = [1, 2, 3, 4, 5]
# a[:0] = [12,3,45]
# print(a)
#
# a.extend(2)
# print(a)
#
# stack = []
#
# stack.append(10)
# stack.append(20)
# stack.append(30)
#
# print(stack)
#
# print(stack.pop(1))
# print(stack)
# print(stack.pop())

# import sys
#
# print(sys.argv)
#
# args = sys.argv[0:]
# print(args)

# a = {1, 2, 3}
# print(a,type(a))
#
# a.add(4)
# print(a)
# a.remove(4)
# print(a)
# a.clear()
# print(a)
# a.update({2, 5})
# print(a)
#
# print(4 in a)
#
# s1 = {1,2,3,4,5,6,7,8,9,10}
# s2 = {10, 20, 30}
#
# s3 = s1.union(s2)  #합집합
# print(s3)
#
# s4 = s1.difference(s2)
# print(s4)   #여집합
#
# s4 = s1.intersection(s2)
# print(s4)   #교집합
#
# s5 = s1.symmetric_difference(s2)
# print(s5)
# print(s1.issuperset(s4)) #포함 여부
# print(s5.issuperset(s1))
# print(s2.issubset(s3))

#
# t = (1, 2, 3)
# print(t, type(t))
#
# t = 1, 2, 'python'
# print(t, type(t))
#
# print(t[-2], t[-1], t[0], t[1], t[2])
# print(t[1:3])
# print(t[:])
#
# print(t * 2)
# t += (3, 4, 5)
# print(len(t))
# print(5 in t)

# li = list(range(10))
# print(li)
#
# li = [i for i in range(10)]
# print(li)
#
# li2 = [(i*2)+1 for i in range(10)]
# print(li)
#
# li = [i for i in range(10) if i % 2 == 1]
# print(li)
#
# li1 = [ i for i in range(10)]
# print(li1)
#
# li1 = [ i for i in range(11) if i > 0]
# print(li1)
#
# li1 = [ i for i in range(1,101)]
# print(li1)
#
# li1 = [ i for i in range(1,101) if i % 3 == 0]
# print(li1)
#
# sum = 0
# for i in range(1, 11):
#     sum+= i
# print(sum)
#
# sum = 0
# for i in range(1,101):
#     if i % 2 == 1:
#         sum += i
#
# print(sum)
#
# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     print(i)
#     i+=1
#
# for i in range(1, 10):
#     for j in range (1, 10):
#         print("%2d*%2d=%2d" %(j,i,i*j),end = '  ')
#
#
#     print("\n")
#
# print('{} %(bb)d {} %(aa)d'.format('string', 100) %({'aa':10, 'bb': 200}))


# i = 0
# for value in ['red', 'yellow', 'blue', 'white', 'gray']:
#     print('{0}: {1}'.format(i, value))
#     i += 1
#
# # 비교 : enumerate 함수를  사용했을  때
# print("\n")
# for i, value in enumerate(['red', 'yellow', 'blue', 'white', 'gray']):
#     print('{0}: {1}'.format(i, value))

seq1 = {'foo', 'bar', 'baz'}
seq2 = {'one', 'two', 'three'}
#
# z = zip(seq1, seq2)
# print(z)
# print(type(z))
#
# for t in z:
#     print(t, type(t))
#
# z = zip(seq1, seq2)
#
# for idx, (a, b) in enumerate(z):
#     print('%d: %s, %s' % (idx, a, b))
# d1 = [('foo', 'one'), ('oer', 'two'), ('baz', 'three')]
#
# seq1, seq2 = zip(*d1)
# print(seq1)
# print(seq2)

#
# results = []
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     result = i * i
#     results.append(result)
# print(results)
#
# results = [result*result for result in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
# print(results)

#
# threes = [i for i in range(1, 100) if i % 10 == 3 or i % 10 == 6 or i % 10 == 9 ]
# print(threes)

# import random as r
#
# print(r.random())
# print("%2d" %(r.random()*100))
# --> randint(a,b) 로 간소화 가능
# print(r.uniform(2,9))
# print(r.randint(2,49))
#
# li = list(range(1,10))
# r.shuffle(li)
# print(li)

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
lens = [len(s) for s in strings]
print(lens)

lens = {len(s) for s in strings}
print(lens)

strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
dicts = {s: len(s) for s in strings}
print(dicts)





















