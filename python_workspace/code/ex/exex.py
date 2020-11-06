# a = [1,3,5,4,2]
# a.sort(reverse=True)
# print(a)

# ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
# a = ['Life', 'is', 'too', 'short']
# b = ""
# for ace in a :
#     b = b + ace+" "
# print(b)


# (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
# a = (1,2,3)
# b = (4,)
#
# print(a+b)


# 다음과 같은 딕셔너리 a가 있다.
# >>> a = dict()
# >>> a
# {}
# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
# a['name'] = 'python'
# a[('a',)] = 'python'
# a[[1]] = 'python'
# a[250] = 'python'
#
# a[[1]] => 2차원 list // 나머지는 딕셔너리 키 / 밸류 선언





# 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
# >>> a = {'A':90, 'B':80, 'C':70}
# ※ 딕셔너리의 pop 함수를 사용해 보자.
# a = {'a':90,'b':80,'c':70}
# print((a.pop('b')))


# a 리스트에서 중복 숫자를 제거해 보자.
# >>> a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# ※ 집합 자료형의 요솟값이 중복될 수 없다는 특징을 사용해 보자.
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# b = set(a)
# a = list(b)
# print(b)






# 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 그리고 이런 결과가 오는 이유에 대해 설명해 보자.
# >>> a = b = [1, 2, 3]
# >>> a[1] = 4
# >>> print(b)
# a,b각각 선언된게 아닌 같은 리스트 주소값을 공유
#
#
# for i in range(2,10):
#     for j in range(2,10):
#         print(j,' * ', i , ' = ',i*j,end="\t|")
#     print('')


# 다음 코드의 결괏값은 무엇일까?
# a = "Life is too short, you need python"
# if "wife" in a: print("wife")
# elif "python" in a and "you" not in a: print("python")
# elif "shirt" not in a: print("shirt")
# elif "need" in a: print("need")
# else: print("none")
# shirt => elif문에 걸려서 끝남





# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
# num = 0
# sum = 0
# while (num <= 1000):
#     if (num % 3 == 0):
#         sum = sum + num
#     num = num + 1
# print(sum)



# while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# *
# **
# ***
# ****
# *****
# a = 1
# while (a <= 5):
#     print("*" * a)
#     a = a + 1



# for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
# for a in range(1,101):
#     print(a)


# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.
# avge = 0
# i = 0
# a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for score in a:
#     avge = avge + score
#     i = i + 1
# print(avge)
# print(avge / i)


# 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.

# numbers = [1, 2, 3, 4, 5]
# result = [n *2 for n in numbers if n % 2 == 1 ]
# print(result)










