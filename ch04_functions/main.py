'''
1. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드(methods)
    3) 사용자 정의 함수

2. 함수 용어 정리
    1) 함수 정의 : 사용자 함수를 새로 만드는 것을 의미(def : define)
    2) 인수(argument) : 함수에 전달할 입력값(input)
    3) 매개변수(parameter) : 인수를 받아서 저장하는 변수를 의미
    4) 반환값 / 결과값 / 리턴값 : 함수의 출력값(output)
    5) 함수 호출(call) : 함수를 실제로 사용하는 것을 의미

3. (사용자) 함수의 형식:
def 함수_이름(매개변수1, 매개변수2):
    실행문
    return

변수 = 함수_이름(argument1, argument2)
'''
# 함수 정의
def display_name(name):
    print(f'당신의 이름은 {name}입니다')

# 함수 호출
display_name('김일')

def display_name_age(name, age):
    print(f'당신의 이름은 {name}이고, 나이는 {age}살입니다.')

display_name_age('김이', 30)
display_name_age(age=23, name='김삼') # keyword argument
'''
우리가 예를 들어 input('이름을 입력하세요 >>> ')을 이용해서 이것을 name이라는 변수에 담았다고 가정하면,
name = input('이름을 입력하세요 >>> ')이라고 작성해옴.

그러면 여태까지 input()이라는 파이썬 내장 함수를 사용하고 있었다고 볼 수 있음.
파이썬 내장 함수는 이미 정의가 되어있고, 개발잦들은 함수 호출만 잘하면 됨.

사용자 정의 함수의 경우 개발자 자신이 함수를 정의하고, 그 후에 호출까지 하는 것까지의 과정이라고 보면 됨.

내장 함수 예시
print() / type() / int() / float() / input()

2. 메서드(methods) : 특정 객체가 가지고 있는 함수를 의미. 특정 자료형에 포함되어있는 함수. 사실 함수와 메서드는 동일한 개념이지만, 호출 방식에 있어서의 차이가 있음.

함수는 독립적으로 사용 가능 / 메서드는 특정 객체를 통해서만 호출 가능
'''
# 메서드의 예시
eng_name = input('당신의 이름을 영어로 입력하세요 >>> ')
'''
이상의 코드는 함수 호출을 해서 그 결과값을 eng_name이라는 변수에 담았다고 볼 수 있음.

그리고 어제 저희가 수업한 것처럼 input(0의 결과값의 자료형은 str
'''
print(eng_name)
eng_name = eng_name.upper()
print(eng_name)
'''
그렇다면 eng_name.upper()의 경우 .upper()가 메서드에 해당하고, 해당 메서드는 str 자료형에 종속되어있다고 볼 수 있음.
그리고 그 결과값을 '다시 eng_name'이라는 변수에 담았기 때문에 위 두 결과값 차이 발생.

함수(메서드)의 유형
'''
# 매개 변수 x / 리턴 x
def call1():
    print('[ x | x ]')

# 매개 변수 o / 리턴 x
def call2(unknown_parameter):
    print('[ o | x ]')
    print(f'{unknown_parameter}라고 입력하셨나보네요')

# 매개 변수 x / 리턴 o
def call3():
    print('[ x | o ]')
    return 1

# 매개 변수 o / 리턴 o
def call4(unknown1, unknown2):
    print('[ o | o ]')
    return unknown1 + unknown2

# 함수 호출
call1()
call2('오늘의 날씨는 선선한 편')
call2(123456)
call3()
print(call4('안녕', '하세요'))

'''
700원짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하시오. 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지, 그리고 잔돈은 얼마인지
모든 경우의 수를 출력하도록 함.

함수 정의
- 반환값 : 없음
- 함수 이름 : vending_machine()
- 매개변수 : 정수 money
'''
def vending_machine(money):
    num = 0
    print(f'음료수 = {num}개, 잔돈 = {money}원')
    while money >= 700:
            money = money - 700
            num += 1
            print(f'음료수 = {num}개, 잔돈 = {money}원')

vending_machine(3000)
vending_machine(600)

# 강사님 ver.
my_money = 3000
drink_price = 700

# #1 for
for i in range(my_money // drink_price + 1):
    print(f'음료수 = {i}개, 잔돈 = {my_money-(drink_price*i)}원')

# #2 while

# 일단 for 문 기준 으로 함수화
def vending_machine(money):
    drink_price = 700
    for i in range(my_money // drink_price + 1):
        print(f'음료수 = {i}개, 잔돈 = {my_money - (drink_price * i)}원')

vending_machine(3000)

'''
예제 : 구구단 출력하기
함수 정의
함수 이름 : multiply
매개변수 : 정수 n
리턴값 : 없음

함수 호출 :
multiply(dan)

'''
def multiply(n):
    for i in range(1, 10):
        print(f'{n} x {i} = {n * i}')

dan = int(input('몇 단을 출력하시겠습니까? >>> '))
multiply(dan)

'''
range() 함수의 parameter 적용 순서
1 개만 있을 때 : 한계값
2 개 있을 때 : 시작값, 한계값
3 개 있을 때 : 시작값, 한계값, 증감값

그럼 현재 multiply를 call2() 유형으로 정의했다고 볼 수 있음

multiply2를 call1() 유형으로 정의하기
'''
def multiply2():
    dan = int(input('몇 단을 출력하시겠습니까? >>> ')) # 지역 변수 (scope)
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')


multiply2()