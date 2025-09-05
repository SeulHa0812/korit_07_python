'''
일종의 setter 활용하여 속성에 속성값 넣어줌
자바에서 처럼 속성값이 대입되지 않은 객체를 생성한 다음에
속성값을 집어넣어주는 과정 거쳐야함

근데 매개변수 생성자를 정의해버리면 객체 생성시에 속성값을 넣을 수 있음
'''
# 클래스 정의
class Candy:
    def set_info(self, shape, color):
        self.shape = shape
        self.color = color

    def show_info(self):
        print(f'사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')

# 객체 생성 (빈 객체 -> 속성값 대입 -> 속성값 출력)
satang = Candy()
satang.set_info('구형', '갈색')

'''
이게 굳이 속성값에 대한 제한이 있지 않다면 빈 객체 만들어놓고 거기에 값 대입하는게 비효율적으로 느껴짐. 그래서 생성자 도입 예정

자바 / 자바스크립트 등에서는 생성자 명은 클래스명과 동일하거나 constructor 인데, 또 파이썬만 이상한걸로 생성자 만듬
'''
class Candy2():
    # 생성자 정의
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def show_info(self):
        print(f'사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')

# 객체 생성 방식에서의 차이가 있음
satang2 = Candy2('정육면체', '흰색')
satang2.show_info()

class Sample:
    # 생성자 정의
    def __init__(self):
        print('인스턴스가 생성되었습니다.')
    # 소멸자 정의
    def __del__(self):
        print('인스턴스가 소멸되었습니다.')

# 객체 생성
sample = Sample()
print()
# 객체 소멸자 호출 방법
del sample # del 객체명
print('객체 지운 후의 코드라인입니다.')
'''
굳이 소멸자로 학습하는 이유 -> 객체가 생성되면 메모리 공간을 차지해서, 객체가 호출될 때마다 그곳에서 불려나오게 됨.

하지만 특정 객체가 일정 코드라인 이후로 전혀 사용되지 않을 때에도 여전히 메모리를 차지하기 때문에 소멸자를 통해서
강제로 객체를 삭제해주면 메모리 관리가 편함

우리 프젝에선 굳이 안 쓸 것
'''
class USB:
    def __init__(self, capacity):
        print(f'USB 객체가 생성되었습니다.')
        self.capacity = capacity

    def get_info(self):
        print(f'{self.capacity}GB USB')

usb = USB(64)
usb.get_info()

# # 응용 예제 1
# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f'{name} is born.')
#
#     def __del__(self):
#         print(f'{self.name} is dead.')
#
# man = Person('james')
# woman = Person('emily')
#
# del man
# '''
# james is born.
# emily is born.
# james is dead.
# emily is dead.
# 라고 나오게 됨. 이 이유는 모든 코드블럭이 다 읽어지면 메모리에 할당된 객체는 자동소멸하기 때문
# 그래서 강제로 emily is dead. 를 출력하고 싶지 않다면 꼼수가 좀 필요함.
# '''
# input('소멸자가 호출되는 것을 막는 중입니다.')

'''
파이썬 getter / setter

setter -> call2() -> 매개변수 o / 리턴 x
getter -> call3() -> 매개변수 x / 리턴 o
'''
'''
age / address / score 속성 setter 통해서 추가
이상의 속성에 맞는 getter 추가

student 1 객체 생성
김일, 20, 4.5 각각 이름/나이/점수에 대입

getter 활용
김일 학생의 나이는 20살로, 파이썬 과목의 점수는 4.5점입니다. 출력
'''
class Student:
    # 생성자 정의
    def __init__(self, name, age, address, score):
        self.name = name
        self.age = age
        self.address = address
        self.score = score

    # setter 정의
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_address(self, address):
        self.address = address

    def set_score(self, score):
        self.score = score

    # getter 정의
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address

    def get_score(self):
        return self.score

student1 = Student('김일', 20, '부산광역시', 4.5)
print(f'{student1.get_name()} 학생의 나이는 {student1.get_age()} 살로, 파이썬 과목의 점수는 {student1.get_score()}점입니다.')