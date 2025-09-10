'''
1. 클래스 변수 vs. 인스턴스 변수
    인스턴스 변수 : 인스턴스 마다 서로 다른 값을 가지는 변수
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수(자바에서는 정적 변수)

    인스턴스 변수
        목적 - 인스턴스마다 서로 다른 값을 저장
        접근 방식 - 인스턴스 접근(o)
                - 클래스 접근(x)
    클래스 변수
        목적 - 인스턴스가 공유하는 값을 저장
        접근 방식 - 인스턴스 접근(o)
                - 클래스 접근(o)
'''
# 클래스 변수 예시
class Korean:
    country = '한국'          # 클래스 변수 #1
    # 인스턴스 변수의 경우는 생성자 내부에 있었음(__init__내부)
    # 클래스 변수는 이상처럼 클래스 내부에 선언하고 초기화하면 됨.

    def __init__(self, name, age, address):
        self.name = name # 인스턴스 변수 #1
        self.age = age  # 인스턴스 변수 #2
        self.address = address # 인스턴스 변수 #3

# 객체 생성
man1 = Korean('김일', 21, '서울특별시 종로구')
print(man1.name)    # 인스턴스 변수 참조
print(man1.age)
print(man1.address)

print(man1.country) # result : 한국
print(Korean.country) # result : 한국

'''
객체명.클래스변수 를 통해서 클래스 변수에 접근이 가능하긴 하지만, 클래스 내부의 코드를 들여다보기 전까지는 country라는 변수가 인스턴스 변수인지 클래스 변수인지 알 방법이 없다는 문제가 있음.

이상을 이유로 클래스 변수를 확인하고자 할 때는 객체명.클래스변수명 보다는 클래스명.클래스변수명 을 통해서 참고하는 것이 권장됨.

2. 클래스 메서드 : 클래스 변수를 사용하는 메서드
'''
class Korean2:
    country = '대한민국' # 클래스 변수의 선언 및 초기화

    # 클래스 메서드 정의 방법
    @classmethod        # @classmethod 데코레이터를 달면 클래스 메서드로 인지함
    def trip(cls, travelling_site): # 그 결과 첫 번째 매개변수가 self 아니라 cls
        if cls.country == travelling_site:
            print('국내 여행 입니다.')
        else:
            print('해외 여행 입니다.')

# 클래스 메서드의 호출
Korean2.trip('대한민국')
Korean2.trip('미국')
man2 = Korean2()
man2.trip('일본')
# 클래스 변수와 마찬가지로 객체명.클래스메서드명() 으로 호출이 가능하기는 하지만 마찬가지로 이게 인스턴스 메서드인지 알 바가 아니기 때문에 클래스메서드를 호출할 때는
# 클래스명.클래스메서드명() 으로 하는 것을 권장

'''
특징 :
    1) 인스턴스 / 클래스로 호출 가능 -> 하지만 클래스로 호출하도록 권장
    2) 생성된 인스턴스가 없어도 호출 가능(클래스로 호출하면 되니까)
    3) @classmethod 데코레이터(decorator)를 표시하고 작성
    4) 매개변수 cls를 사용 -> self는 객체를 의미하고 / cls는 클래스를 의미함.

3. 정적 메서드(static method)
    : 정적 메서드 또한 self를 사용하지 않음 -> 즉, 인스턴스 변수에 접근하여 사용하는 것이 불가능함을 의미. self.속성명 을 사용하여 인스턴스 변수의 값을 참조하는데 정적 메서드는 아예 첫 번째 매개변수가 고정이 아님. - 클래스 메서드와의 공통점 #1
    
    인스턴스를 생성하지 않아도 사용할 수 있음 - 클래스 메서드와의 공통점 #2
    
    특징 :
        1) 인스턴스 / 클래스로 호출 가능 -> 클래스 메서드와의 공통점
        2) 생성된 인스턴스가 없어도 호출 가능 -> 클래스 메서드와의 공통점
        
        3) @staticmethod 데코레이터를 표기하고 작성 -> 클래스 메서드와의 차이점 #1
        4) 반드시 작성해야 할 매개변수(self / cls)가 없음 -> 클래스 메서드와의 차이점 #2
        
이상을 토대로, 정적 메서드는 self / cls를 둘 다 사용하지 않기 때문에 인스턴스 / 클래스 변수를 모두 사용하지 않는 메서드를 정희하는 경우에 적합함. 정적 메서드 자체는 클래스에 소속되어있지만 인스턴스에는 영향을 주지도 않고 받지도 않음.

즉 Java에서의 정적 메서드 = 파이썬의 클래스 메서드 + 정적 메서드
'''
class Korean3:
    country = '한국'

    @staticmethod
    def slogan():
        print('Imagine Your Korea!')

    @staticmethod
    def slogan2(str_example):
        """
        얘는 그냥 매개변수가 있는 앱니다.
        """
        print('Imagine Your Korea!' + str_example)

Korean3.slogan()
Korean3.slogan2('근데 너무 덥다')

'''
기본 예제
'''
# 클래스 정의
class Bag:
    # 클래스 변수의 선언 및 초기화
    count = 0

    def __init__(self): # 생성자 호출 및 인스턴스 변수들 정의할 용도. 그럼 생성자도 인스턴스 변수라고 할 수 있겠음(self잇으니까)
        Bag.count += 1 # 생성자가 호출될 때마다(=객체가 생성될 때마다) ㅡㄹ래스 변수인 count가 1씩 증가함. cls.count가 아니라 클래스명.count라는 것에 주목해야 함.
        print('가방 객체가 생성되었습니다.')

    # 클래스 메서드 정의
    @classmethod
    def sell(cls):
        print('가방이 팔렸습니다.')
        cls.count -= 1
        # 얘는 클래스 메서드가 클래스 변수에 접근한 것이기 때문에 Bag.count가 아님

    @classmethod
    def remain_bag(cls):
        return cls.count

print(f'현재 가방 재고 : {Bag.count}')
print(f'현재 가방 재고 : {Bag.remain_bag()}')

# 객체 생성
bag1 = Bag()
print(f'현재 가방 재고 : {Bag.remain_bag()}')
bag2 = Bag()
bag3 = Bag()
print(f'현재 가방 재고 : {Bag.remain_bag()}')
bag1.sell()
print(f'현재 가방 재고 : {Bag.remain_bag()}')

'''
예제 2
'''
# class Person:
#     # class variable
#     population = 0
#
#     # constructor
#     def __init__(self, name):
#         self.name = name
#         Person.population += 1
#         print(f'{self.name}이(가) 태어났습니다.')
#
#     @classmethod
#     def get_population(self):
#         return self.population
#
#
#     def __del__(self):
#         Person.population -= 1
#         print(f'RIP {self.name}')
#
# print(f'전체 인구수 : {Person.get_population()}')
# man = Person('김일')
# woman = Person('김이')
# print(f'전체 인구수 : {Person.get_population()}')
# del man
# print(f'전체 인구수 : {Person.get_population()}')
# print('프로그램 종료')

'''
예제 3
'''
class Shop:
    total = 0
    menu_list = [{ '떡볶이': 3000}, { '순대': 4000 }, { '튀김': 500 }, { '김밥': 2000 }] # dict inside list

    @classmethod
    def sales(cls, menu, count):
        for menu_item in cls.menu_list:
            if menu in menu_item: # key 값 확인
                cls.total += menu_item[menu] * count # dict[key] -> result : value
                print(f"{menu}을(를) {count}개 판매")

    @classmethod
    def get_total(self):
        return self.total


Shop.sales('떡볶이', 1) # 떡볶이을(를) 1 개 판매
Shop.sales('김밥', 2)
Shop.sales('튀김', 5)

print(f'매출 : {Shop.get_total()}원')

