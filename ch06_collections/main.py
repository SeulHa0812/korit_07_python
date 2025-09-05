'''
python 대표 collection 종류
1. list 리스트 : 추가 / 수정 / 삭제가 언제나 가능 / 순서 있음
2. tuple 튜플 : 추가 / 수정 / 삭제가 불가능 / 슌서 있음
3. set 세트 : 중복된 값의 저장이 불가능 / 순서 없음
4. dict 딕셔너리 : 키 + 값으로 관리
'''
# list_example = [30, 40, '김이', [100, '김삼']]
# tuple_example = (10, 20, 30, '김사')
# set_example = {100, 200, 300, 400, '김오'}
# dictionary_example = { '이름': '김일', '나이':20, '학교': '코리아아이티'}
#
# print(list_example)
# print(tuple_example)
# print(set_example)
# print(dictionary_example)

'''
1. list
    여러 값을 저장할 때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 리스트에 저장 가능. 하나의 배열(파이썬에서 리스트와 비슷한 개념)에 동일한 자료형만을 저장할 수 있는 C, Java에 비해 python이 가지는 장점 중 하나(근데 JS는 또 다양한 자료형이 배열에 저장되긴 함)
'''
# list의 선언 및 초기화
list1 = [ 1, 2, 3, '김사']
'''
    1)
    마이너스 인덱스 가능
'''


'''
    2) slicing
    str의 슬라이싱과 같이 '시작인덱스:종료인덱스:증감값'으로 이루어져 있음
'''
li2 = [100, 3.14, 'hello', 5,6,7,8,9] # list 선언 및 초기화 방법 1
li3 = list([ 4, 5, 6, 7, 8, 9, 0 ]) # 방법 2
# li3 = list([4,5,6,7,8])
print(li2[0:4:2]) # 0번지부터 4번지 앞까지, 2씩 증가 # 결과값 : [100, 'hello']
'''
위의 코드 자바 버전
String strExample = new String("안녕하세요"); 
String strExample = "안녕하세요";  

    3) list element의 추가와 삭제
        list에 새로운 요소를 추가할 때는 어제한 것 처럼 .append() / .insert() 'method' 사용 가능
        삭제 .pop() 메서드
        
        .append() - 항상 마지막 인덱스에 element 추가
        .inset(위치, 값) - 정해진 위치(인덱스)에 해당 값 추가
'''
scores = [30, 40, 50]
print(scores)
scores.append(100)
print(scores)
scores.insert(0, 90)
print(scores)
'''
    .pop()의 경우 빈 괄호로 사용하게 되면(call3() 유형이라면) 맨 마지막 요소가 삭제됨.
    .pop(인덱스넘버)로 작성하면 해당 인덱스의 마지막 요소를 삭제함.
'''
print(scores.pop()) # call3 유형. 즉 return 값 있음, 삭제한 element가 return되기 때문에 print(scores.pop())은 현재 scores의 맨 마지막 element인 100이 콘솔에 출력됨.
print(scores.pop(0)) # result : 90
'''
교재에 없는 삭제 메서드 : .remove(값)을 사용하면 list 내에 해당 값을 찾아 삭제( argument로 인덱스 넘버를 요구하는게 아니라 특정 데이터를 요구한다고 볼 수 있음 )
'''
print(scores.remove(50)) # result : none / 특정 값 바로 삭제
print(scores) # result : [30 , 40]

'''
li4 리스트 선언, 1-10까지 넣기
'''
li4 = []
for i in range(1, 11):
    li4.append(i)
print(li4)

'''
각 list 내의 element들을 뽑아내서 * 2
'''
for i in range(len(li4)):
    new_element = li4[i] * 2
    li4[i] = new_element
print(li4)

print()

# 향상된 for
n = 0
for element in li4:
    li4[n] = element*2
    n += 1
print(li4)
# 사실상 list의 element들에게 동일한 연산을 일괄적으로 적용하는 method 가 있기 때문에 추후 설명 할 예정

'''
    2. tuple
        저장된 값을 변경할 수 없는 list
        순서 있기 때문에 index 넘버와 slicing 가능,
        but 저장된 값 이외에 추가 / 수정 / 삭제 불가능
        
        소괄호 통해서 생성
'''
tu1 = (1, 2, 3) # 생성 방법 1
tu2 = tuple((4, 5, 6)) # 생성 방법 2
tu3 = 7, 8, 9 # 생성 방법 3     근데 얘는 변수 하나에 데이터가 여러개

a, b, c = 7, 8, 9 # 복수의 변수 선언 및 초기화 방법 -> 즉 변수 개수와 데이터 개수가 같으면 가능
print(a)
print(b)
print(c)

tu4 = 0 # datatype?
print(type(tu4)) # result : <class 'int'>
# tu4라고 해서 저희는 튜플로 생각하고 변수명을 지었지만 실제로는 그냥 int 변수명

tu5 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(tu5)

tu6 = 'hello. ', 'good morning ', 'my name is ', 'kim-il ', 'i am ', '20 ', 'years old.'
for word in tu6:
    print(word.title(), end='')

print() # result : Hello. Good Morning My Name Is Kim-Il I Am 20 Years Old.

print(tu6)
'''
굳이 이상의 예시를 남겨두는 이유는 우리가 배우는 collection의 개념과 내부 element의 자료형이 서로 다르다는 점. tuple의 정의는 내부 element의 추가 / 수정 / 삭제가 불가능한 collection이지만, element들은 가공 가능

가동해서 tuple에 대입하는 것이 불가능. 수정이 불가능하니까
'''
'''
    3. set 
    수학의 집합 개념. 자바에서와 같음
'''
set1 = {1,2,3} # 세트 생성 방법 #1
set2 =  set({4,5,6}) # 세트 생성 방법 #2
print(set1)
print(set2)
# 굳이 # 1, 2를 나눈 이유 : 비어있는 list /tuple/set 생성 방법
li = []
tu = ()
se = {}

print(type(li)) # result : <class 'list'>
print(type(tu)) # result : <class 'tuple'>
print(type(se)) # result : <class 'dict'>
'''
se = {} 형태로 비어있는 set을 생성 -> 'dict'으로 나옴.
그래서 비어있는 set을 생성하기 위해서는 반드시 #2 방식으로 만들어줘야함
'''
se2 = set({})
print(type(se2)) # result : <class 'set'>
'''
    list / tuple은 index 존재. 이 두개를 sequence라고 하고, set / dictionary 의 경우에는 index가 없어서 비시퀀스라는 표현을 씀. 슬라이싱 없음
        element 관련 메서드
        1. .add() - set에 새로운 element 추가
        2. .remove() - 기존 element 삭제
        3. .discard() - 기존 element 삭제
'''
se3 = {10, 20, 30}
se3.add(50)
print(se3) # result : {10, 20, 50, 30} - 순서가 없어서.
se3.remove(30) # 순서가 없기 때문에 '값'을 정확하게 입력해야 함
print(se3) # result : {10, 20, 50}

# remove() vs. discard()
# se3.remove(70) # 오류 발생 - '값을 정확하게 입력'해야만 한다고 했기 때문
se3.discard(70) # 오류 방생 x / 정확한 값 없으면 그냥 종료

# 향상된 for문으로 element를 추출할 수 있음. 순서 보장 x
for element in se3:
    print(element)

'''
    4. dict(dictionary) - Java에서의 Map / JS에서의 Object / JSON과 같은 형식
    
'''
dict1 = {
    '이름': '김일',
    '나이': 20,
    '주소': ['서울특별시', '마포구', '목동'],
}
'''
    전에 수업했던 것처럼 위 라인에 지금 key-value pair가 있는게 콤마치고 엔터치고 키-값 입력하면 번거로우니까 맨 마지막 property에 콤마 찍어주는게 매너
    
    딕셔너리에는 인덱스는 존재하지 않지만 key를 인덱스와 유사하게 사용함. 즉 key를 알면 값을 확인할 수 있는 구조
'''
# list의 element 추출 반복문 작성
li01 = [10,20,30,40]
for num in li01:
    print(num)

# dictionary 에서 같은 방식의 반복문을 활용하게 될 때,
# 진짜 중요 - dictionary/ JS Object에서 향상된 for 문으로 반복문 돌리면 key가 빠져나옴
# 그래서 딕셔너리명[key]로 작성해야 value 조회가능
for key in dict1:
    print(key) # key
    print(dict1[key]) # value

# key들만 추출하는 메서드
print(dict1.keys()) # result : dict_keys(['이름', '나이', '주소'])
print(type(dict1.keys())) # <class 'dict_keys'>

# value들만 추출하는 메서드
print(dict1.values()) # result : dict_values(['김일', 20, ['서울특별시', '마포구', '목동']])
print(type(dict1.values())) # <class 'dict_values'>

# key들만 뽑아서 list를 만든다든지 / value들만 뽑아서 list를 만들고 싶다면 형변환 함수를 사용해야 함

keys = list(dict1.keys())
values = list(dict1.values())
print(keys)     # 그럼 이제는 인덱스로 추출하는 것이 가능
print(values)
'''
그래서 collections 수업 상황에서 매우 중요한 것은 list를 배웠을 때 list만 생각할 것이 아니라,
set이나 tuple, dictionary로 자료형 변경이 가능한가, 어떤 식으로 가능한가, 어떨 때 써야하는가와 같이 종합적인 고려를 하는 역량이 데이터를 다룰 

        1) dictionary에서 property 추가 / 삭제
        
'''
dict1['직업'] = '웹 퍼블리셔' # 기존에 없는 ley를 입력하고 = value 지정
print(dict1)
dict1['직업'] = '웹 개발자' # key 하나당 value는 고정이기 때문에 재대입이 이루어짐.
print(dict1)
# 삭제 방법
print(dict1.pop('직업')) # key를 알아야지 삭제 가능 / .pop()의 return 특성 중요
print(dict1)

# # 응용 예제 1
# li001 = []
# for i in range(10, 101, 10):
#     li001.append(i)
# print(li001)
# # 일반적인 강의에서 하는 단계별 슬라이싱 추출
# a = li001[2:7]
# print(f'3 번째 요소로부터 7 번째 요소 = {a}')
# b = a[1]
# print(f'3 번째 요소로부터 7 번째 요소 중 2 번째 요소 = {b}')
#
# # 강사님 ver
# list_sliced = li001[2:7]
# print(f'3 번째 요소로부터 7 번째 요소 = {list_sliced}')
# print(f'3 번째 요소로부터 7 번째 요소 중 2 번째 요소 = {li001[2:7][1]}')
#
# # 응용 예제 2
# # method 1
# month1 = int(input('1 ~ 12 사이의 월을 입력하세요 >>> '))
# days1 = {
#     1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
#     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
# }
# days_result1 = days1[month1]
# print(f'{month1}월은 {days_result1}일까지입니다.')
#
# # method 2
# month2 = int(input('1 ~ 12 사이의 월을 입력하세요 >>> '))
# days2 = [28, 30, 31]
# if month2 == 2:
#     days_result2 = days2[0]
# elif month2 in [4, 6, 9, 11]:
#     days_result2 = days2[1]
# elif month2 in [1, 3, 5, 7, 8, 10, 12]:
#     days_result2 = days2[2]
# print(f'{month2}월은 {days_result2}일까지입니다.')
'''
이상의 코드 라인에서 중요한 것은 in 개념
in 뒤에는 다양한 것들이 올 수 있는데, 특히 반복가능객체가 올 수 있음
그래서 
elif month2 in [1, 3, 5, 7, 8, 10, 12]:
    days_result2 = days2[2]
의 해석 부분이 중요한데, in 다음의 임의의 list를 초기화하여 month_int가 임의의 list의 element 값을 가지고 있는지 여부를 조건 검토했다고 해석할 수 있음
( 1, 3, 5, 7, 8, 10, 12 ) 이렇게 초기화 하더라도 전혀 문제 없음. tuple 사례
'''
# # method 3
# month3 = int(input('1 ~ 12 사이의 월을 입력하세요 >>> '))
# days3 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# days_result3 = days3[month3 - 1]
# 
# print(f'{month3}월은 {days_result3}일까지입니다.')
# 
# # 응용 예제 3
# nums_student = 3
# destinations_set = set({})
# for i in range(nums_student):
#     destination = input('희망하는 수학여행지를 입력하세요 >>> ')
#     destinations_set.add(destination)
# 
# destinations_list = list(destinations_set)
# print(f'조사된 수학여행지는 {destinations_list}입니다.')

# # 응용 예제 4
# num = int(input('몇 개의 숫자를 입력할까요? >>> '))
# numbers_list =[]
# for i in range(num):
#     numbers = int(input(f'{i+1}번째 숫자를 입력하세요 >>> '))
#     numbers_list.append(numbers)
# print(f'입력 받은 숫자는 {numbers_list}입니다.')
#
# numbers_even_list = []
# for i in numbers_list:
#     if i % 2 == 0:
#         numbers_even_list.append(i)
# print(f'입력 받은 숫자들 중 짝수는 {numbers_even_list}입니다.')

# 응용 예제 5
# contact_info = {}
# for i in range(3):
#     name = input(f'{i+1} 번째 사람의 이름을 입력하세요 >>> ')
#     number = input(f'{i+1} 번째 사람의 연락처를 입력하세요 >>> ')
#     contact_info[name] = number
# print(f'입력 받은 연락처는 {contact_info}입니다.')

# 응용 예제 6 collection + function
numbers1 = []
def add_number1(n) :
    for i in range(1, n+1):
        numbers1.append(i)
    print(numbers1)

numbers2 = []
def add_number2(n) :
    for i in range(1, n+1):
        numbers2.append(i)
    return numbers2

hello = ['안', '녕', '하', '세', '요']
numbers3 = []
def add_number3(n, temp_list) :
    for i in range(n):
        numbers3.append(i+1)
    result = numbers3 + temp_list
    print(result)

def add_number4(n, temp_list) :
    for i in range(n):
        temp_list.insert(i, i+1)
    print(temp_list)

last_num = int(input('숫자 몇 까지 입력하시겠습니까? >>> '))
add_number1(last_num)
print(add_number2(last_num))
add_number3(last_num, hello)
add_number4(last_num, hello)

# 응용 예제 7
def count_even_odd(numbers) :
    even_count = 0
    odd_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f'짝수의 개수 : {even_count}개')
    print(f'홀수의 개수 : {odd_count}개')

count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])




