# 2번

# li = []
# print(li)
#
# for i in range(5):
#     li.append(int(input('정수 입력 : [%d/%d]' %(i+1, 5))))
#     print(li)

# 3번
#
# old = "password is 1234"
#
# print(old.replace("1234","5678"))

# 4번

# url = 'http://www.naver.com/news/today=20200131'
# user = 'name:홍길동 age:22 sex:남자 nation:대한민국'
#
# url = url.split('/')
# print(url)
#
# user = user.split(':')
# print(user)
#
# user = "->".join(user)
# print(user)


# 5번
#
# space= ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성','지구']
#
# for i in range(len(space)):
#     if space[i] == '지구':
#         space[i] = 'earth'
#         print(i)
# print(space)

# 6번
# covid = {'January':4500, 'February':5000, 'March':2500, 'April':1200,
#             'May':567, 'June':434, 'July':323}
# # values = covid.values()
# values = list(covid.values())
# print(values)
# sum = 0
# #print(sum(values)) # => 간소화 버전
# for i in range(len(values)):
#     sum += values[i]
#     print(sum)
#     print(i)
# print(sum // (i+1))

# 7번
# import random as r
# print("숫자 맞추기 게임(1~100사이 값중 하나를 고르시오)")
# randNum = r.randint(1,100)
# guessNum = int(input())
# i = 0
# print(randNum)
# while guessNum != randNum:
#     if guessNum < randNum:
#         print("%d 보다 큰 숫자입니다." %(guessNum))
#         print("숫자 입력 : ", end="")
#         i += 1
#         guessNum = int(input())
#     elif guessNum > randNum:
#         print("%d 보다 작은 숫자입니다." %(guessNum))
#         print("숫자 입력 : ", end="")
#         i += 1
#         guessNum = int(input())
#     else:
#         break
# print("정답. %d번만에 맞춤" %(i+1))
# while문 대신 continue 사용 가능

# s = 12//3
# s1 = 12%3
#
# ss = s//3
# ss1 = ss%3
# print(s)
# print(s1)
# print(ss)
# print(ss1)

































