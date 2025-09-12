from turtle import Turtle, Screen
from random import Random
# turtle 모듈에서 Turtle, Screen 클래스를 import해옴

t = Turtle() # 터틀 객체 생성, 객체명 t
screen = Screen()
# 이상의 경우만 작성했을 때 모니터가 깜빡이는 것을 확인할 수 있는데, 이는 코드가 다 돌아가면 프로그램이 종료되기 때문에, 창이 켜졌다가 꺼지는 것

t.shape('turtle') # Turtle의 메서드를 호출했는데 argument가 str
t.color('white')
screen.bgcolor('black')

# 랜덤 객체 생성
random = Random()
colors = [
    'light blue',
    'light sky blue',
    'deep sky blue',
    'sky blue',
    'steel blue',
    'light blue'
]

# 점선 그리는 반복문
# for i in range(9):
#     t.forward(20)
#     t.penup()
#     t.forward(20)
#     t.pendown()
# t.forward(20)

# .left(각도)
# for i in range(4):
#     t.forward(100)
#     t.left(90)

# 정삼각형
# for i in range(3):
#     t.forward(100)
#     t.left(120)

# 오각형
# for i in range(5):
#     t.forward(100)
#     t.left(72)

# 육각형
# for i in range(6):
#     t.forward(100)
#     t.left(60)

'''
함수화
'''
# n = int(input('몇 각형을 만드시겠습니다? >>> '))
# for i in range(n):
#     t.forward(100)
#     t.left(360/n)

# for i in range(3, 100, 1):
#     for _ in range(i):
#         t.forward(100)
#         t.left(360 / i)
#     t.color(random.choice(colors))

# 근데 도형 그릴 때마다 반복문 쓰는거 귀찮으니 함수 정의
# def draw_shape(n):
#     for _ in range(n):
#         t.forward(100)
#         t.left(360 / n)
#
# def draw_dotted_line():
#     for _ in range(10):
#         t.forward(5)
#         t.penup()
#         t.forward(5)
#         t.pendown()
#
# def draw_dotted_shape(n):
#     for _ in range(n):
#         draw_dotted_line()
#         t.left(360/n)
#     t.color(random.choice(colors))
#
# for i in range(3, 11):
#     draw_dotted_shape(i)

# t.forward(100)
# print(t.heading())
# t.left(90)
# t.forward(100)
# print(t.heading())
# t.left(30)
# t.forward(100)
# print(t.heading())
# t.right(30)
# t.forward(100)
# print(t.heading())
# t.setheading(30)
# t.forward(100)
# print(t.heading())
#
# # .heading의 return 값은 float
# # .setheading()의 parameter가 float / return None
#
# t.setheading(t.heading() + 100)

# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)


# for i in range(36):
#     t.color(random.choice(colors))
#     t.circle(100) # 원 그리는 거 완료
#     # 거북이 머리 다른 쪽으로 돌려서 다음 원리 겹치지 않게끔 하는 함수
#     t.setheading(t.heading() + 10)

# 함수화를 위한 일반식을 main에 작성
# n = 10
# for i in range(n):
#     t.color(random.choice(colors))
#     t.circle(100)
#     t.setheading(t.heading() + (360/n))

# 함수화
def draw_spirograph(size_of_gap):
    for i in range(360 // size_of_gap):     # // 몫 연산자
        t.color(random.choice(colors))
        t.circle(100)
        t.setheading(t.heading() + (360 / size_of_gap))

draw_spirograph(17)
# 이상의 코드에서의 문제점은
# 1. 매개변수인 size_of_gap은 n 번째 원과 n+1 번째 원의 각도차이를 나타내는 것 같은데,
#   실제로는 반복횟수를 통제하고 있음
# 2. 이상의 상황에서 나타나는 점은 360을 입력했을 때, 제자리에서 원이 생성 되는 것이 아니라,
#   그냥 360번을 반복한다는 점

screen.exitonclick()

