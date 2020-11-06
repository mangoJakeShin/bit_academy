
class person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
class contact(person):
    def __init__(self, tel):
        super().__init__()
        self.tel = tel

class container:

    list_content = []
    cnt_ppl = 0

    def create(self):
        new_contact = [3]
        x = print(input('name? = '))
        y = print(int(input('age? = ')))
        z = print(input('phone no? = '))
        new_contact.append(x)
        new_contact.append(y)
        new_contact.append(z)

    def modify(self):
        pass
    def view(self):
        pass
    def delete(self):
        pass


def display_head():
    title = '연락처 프로그램'
    print('='*30)
    print(title.center(26,'='))
    print('='*30)

def display():
    print('1. 생성')
    print('2. 수정')
    print('3. 조회')
    print('4. 삭제')
    print('5. 종료')

def main():
    display_head()
    con1 = container()
    while True:
        display()
        select   = input('번호 입력 : ')
        if select =='1':
            con1.create()
        elif select =='2':
            con1.modify()
        elif select =='3':
            con1.view()
        elif select =='4':
            con1.delete()
        elif select =='5':
            break

main()