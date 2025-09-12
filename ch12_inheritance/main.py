'''
상속

형식 :
class 슈퍼클래스:
    본문

class 서브클래스(슈퍼클래스):
    본문
'''
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, food):
#         print(f'{self.name}이(가) {food}를 먹습니다.')
#
# class Student(Person):
#     def __init__(self, name, school):
#         super().__init__(name)
#         self.school = school
#
#     def study(self):
#         print(f'{self.name}은(는) {self.school}에서 공부를 합니다.')
#
# # 객체 생성
# potter = Student('해리 포터', '호그와트')
# potter.eat('감자')
# potter.study()

'''
1. 서브 클래스의 __init__()
    서브 클래스는 슈퍼 클래스가 없으면 존재할 수 없음. 그래서 서브 클래스의 생성자를 구현할 때는 '반드시 슈퍼 클래스의 생성자를 먼저 호출'하는 코드를 작성해야만 함.
    
    super(). 에서 super -> 슈퍼 클래스를 의미. 즉 이상의 코드에서 Student의 생성자를 호출하려면 super().__init__(name)에 의해서 슈퍼 클래스인 Person의 생성자가 먼저 호출되면 '슈퍼 클래스의 객체가 생성'됨.
    이후에 슈퍼 클래스에서 생성된 인스턴스 변수인 name이 서브 클래스로 전달되고, 이후에 서브 클래스에서 school 인스턴스 변수를 선언 및 초기화하여 저장하면서 서브 클래스의 인스턴스가 생성됨.
    
    : 생성자를 호출했다면 -> 객체가 생성되었다고 봐야하기 때문에 / 부모 클래스의 인스턴스와 자식 클래스의 인스턴스가 있다고 봐도 무방함. -> 그런데 별개의 객체냐고 물으면 그건 또 그럴 때도 있고 아닐 때고 있음.

2. 서브 클래스의 인스턴스 자료형
    슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
    하지만 서브 클래스의 인스턴스는 서브 클래스의 인스턴스이면서 동시에 슈퍼 클래스의 인스턴스
    Student 클래스의 객체는 Student의 인스턴스이면서 Person의 인스턴스
    
    자바를 기준으로 instanceof 연산자 역할을 하는 함수가 python에도 있는데 -> isinstance() : 다 소문자
    
    형식 :
        isinstance(객체명, 클래스먕) -> boolean
'''
# print(isinstance(potter, Person)) # result : True
# print(isinstance(potter, Student)) # result : True
'''
Hybrid 클래스 구현
'''
class Car:
    max_oil = 50
    def __init__(self, oil, amount):
        self.oil = oil
        self.amount = amount

    def add_oil(self, oil):
        if oil <= 0:
            return
        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil
        print(f'기름을 {oil} 주유 했습니다.')

    def car_info(self):
        print(f'현재 주유 상태 : {self.oil}')

class Hybrid(Car):
    max_battery = 30
    def __init__(self, oil, amount):
        super().__init__(oil, amount)
        self.battery = amount
        print('하이브리드 차량이 생산되었습니다.')

    def charge(self, amount_elec):
        if amount_elec <= 0:
            return
        elif self.battery + amount_elec >= Hybrid.max_battery:
            self.battery = Hybrid.max_battery
        else:
            self.battery += amount_elec
        print(f'전기를 {amount_elec} 충전 했습니다.')

    def hybrid_info(self):
        print(f'현재 주유 상태 : {self.oil}')
        print(f'현재 충전 상태 : {self.battery}')

car = Hybrid(oil=0, amount=0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

'''
Shape 예제
'''
class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        return self.name

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius # 초기화
        print(f'반지름이 {self.radius}인 원이 생성되었습니다.')

    def draw(self):
        # super().draw() # override를 받기는 했지만 부모 부분 사용 x
        print(f'이름이 {self.name}인 원의 넓이는 {self.area()}입니다.')

    def area(self):
        return (self.radius**2)*3.14

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        print(f'너비가 {width}, 높이가 {height}인 {self.name}이 생성되었습니다.')

    def area(self):
        return self.width * self.height

    def draw(self):
        print(f'이름이 {self.name}인 직사각형의 넓이는 {self.area()} 입니다.')

        return super().draw()

circle = Circle('원1', 5)
circle.draw()

rectangle = Rectangle('직사각형', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')
