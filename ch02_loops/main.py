'''
1. while 반복문
형식 :
while 조건식1:
    반복실행문

당연히 특정 시점에 while 반복문이 종료될 수 있도록 지정해둬야 함
'''
n1 = 1
while n1 < 11:
    print(n1)
    n1 += 1     # python 에는 ++ 없음

'''
기본 예제
10부터 1까지 역순으로 출력
'''
n2 = 10
while n2 > 0:
    print(n2)
    n2 -= 1

'''
중첩 while 문 (while문 뿐만 아니라 내부에 if를 쓸 수도 있음)
중첩 while 및 f-string 활용하여
실행 예
2 x 1 = 2
...
9 x 9 = 81
'''

num = 2
while num < 10:
    num2 = 1
    while num2 < 10:
        print(f'{num} x {num2} = {num*num2}')
        num2 += 1
    num += 1