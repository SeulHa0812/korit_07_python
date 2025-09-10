'''
사용자로부터 여러 개의 숫자를 입력 받아 리스트에 저장한 후, 해당 리스트에 포함된 숫자들 중 양수, 음수, 0의 개수를 각각 세어 출력하는 프로그램을 작성하시오.

지시사항:

1. 몇 개의 숫자를 입력할지 사용자로부터 입력 받으시오.
2. 입력받은 숫자들을 저장할 빈 리스트(numbers)를 생성하시오.

3. 양수, 음수, 0의 개수를 저장할 변수 3개를 0으로 초기화하시오.

4. for 반복문을 사용하여 입력 받은 횟수만큼 숫자들을 입력 받아 numbers 리스트에 추가하고, 동시에 각 숫자를 판별하여 해당 변수의 값을 1씩 증가 시키시오.

최종적으로 각 변수에 저장된 개수를 출력하시오.

실행 예:

몇 개의 숫자를 입력하시겠습니까? >>> 5

1번째 숫자를 입력하시오 >>> 10

2번째 숫자를 입력하시오 >>> -5

3번째 숫자를 입력하시오 >>> 0

4번째 숫자를 입력하시오 >>> 20

5번째 숫자를 입력하시오 >>> -15

양수: 2개

음수: 2개

0: 1개
'''

# count = int(input('몇 개의 숫자를 입력하시겠습니까? >>> '))
# numbers = []
#
# pos = 0
# neg = 0
# zero = 0
#
# for i in range(1, count+1):
#     num = int(input(f'{i}번째 숫자를 입력하시오 >>> '))
#     numbers.append(i)
#
#     if num == 0:
#         zero += 1
#     elif num > 0:
#         pos += 1
#     else:
#         neg += 1
#
# print(f'양수 : {pos}개')
# print(f'음수 : {neg}개')
# print(f'0 : {zero}개')

'''
	
사용자로부터 전화번호를 입력받아, 특정 조건에 부합하는지 확인하고 전화번호의 중간 4자리를 출력하는 프로그램을 작성하시오. 전화번호는 하이픈(-)을 포함하여 총 13자리(예: 010-1234-5678)여야 한다.

지시사항:

1. 사용자로부터 전화번호를 입력받으시오.
 
2. 입력된 전화번호의 길이가 13자리가 아닐 경우, "유효하지 않은 전화번호 형식입니다."라고 출력하시오.

3. 전화번호가 13자리일 경우, 전화번호의 중간 4자리(예: 1234)를 추출하여 출력하시오.

4. 출력 시 f-string을 사용하시오.

실행 예:

전화번호를 입력하시오 >>> 010-9876-5432 전화번호의 중간 4자리는 9876입니다.

전화번호를 입력하시오 >>> 010-123-4567 유효하지 않은 전화번호 형식입니다.
'''
# phone_number = input('전화번호를 입력하시오 >>> ')
#
# if len(phone_number) != 13:
#     print(f'{phone_number} 유효하지 않은 전화번호 형식입니다.')
# else :
#     print(f'{phone_number} 전화번호의 중간 4자리는 {phone_number[4:8]}입니다.')

'''
학생의 이름과 학번, 그리고 과목별 성적을 관리하는 Student 클래스를 작성하시오. 

이 클래스는 생성자를 통해 학생 정보와 성적 딕셔너리를 초기화하고, 성적을 추가하는 메서드와 평균 성적을 계산하여 반환하는 메서드를 포함해야 한다.

지시사항:

1. Student 클래스를 정의하고, 생성자(__init__)를 통해 name과 student_id를 초기화하시오. 성적을 저장할 빈 딕셔너리(grades)도 초기화하시오.
참고 - 

self.name = name

self.student_id = student_id

self.grade = {}

2. add_grade라는 메서드를 정의하여 subject와 score를 매개변수로 받아 grades 딕셔너리에 추가하시오.

3. get_average_grade라는 메서드를 정의하여 grades 딕셔너리의 점수들을 기반으로 평균 성적을 계산하여 반환하시오.

4. Student 객체를 생성하고, 성적을 추가한 뒤, 평균 성적을 출력하시오.

실행 예:

학생 이름: 김일

평균 성적: 90.0점
'''
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        total = sum(self.grades.values())
        avg = total / len(self.grades)
        return avg

student1 = Student('김일', 00000000)

student1.add_grade('Korean', 90)
student1.add_grade('English', 80)
student1.add_grade('Math', 100)

print(f'학생 이름 : {student1.name}')
print(f'평균 성적 : {student1.get_average_grade()}점')

'''
다음 예시와 같이, 여러 후보자에 대한 투표 결과를 집계하는 프로그램을 작성하시오. 사용자는 먼저 후보자의 수를 입력하고, 그에 맞춰 후보자들의 이름을 입력한다. 이후 투표 횟수와 각 투표 결과를 숫자로 입력받아 최종 결과를 딕셔너리에 저장하여 출력하시오.

지시사항:

1.전체 후보자의 수를 사용자로부터 입력받으시오.
2. for 반복문을 사용하여 후보자 수만큼 후보자들의 이름을 입력받고, candidates 리스트에 저장하시오.

3. 각 후보자의 투표 수를 저장할 딕셔너리(votes)를 생성하고, candidates 리스트의 이름을 키로, 초기 투표 수(0)를 값으로 설정하시오.

4. 전체 투표 횟수를 입력받으시오.

5. for 반복문을 사용하여 투표 횟수만큼 사용자로부터 각 투표 결과를 입력받으시오. 입력은 후보자의 순서 번호(1, 2, 3...)로 받으시오.

6. 입력받은 투표 결과에 따라 해당 후보자의 투표 수를 1씩 증가시키시오.

7. 최종적으로 딕셔너리에 저장된 각 후보자의 투표 수를 출력하시오.

실행 예:

후보자 수를 입력하시오 >>> 3

1번째 후보자의 이름을 입력하시오 >>> 김일

2번째 후보자의 이름을 입력하시오 >>> 김이

3번째 후보자의 이름을 입력하시오 >>> 김삼

전체 투표 횟수를 입력하시오 >>> 5

1번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 1

2번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 2

3번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 1

4번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 3

5번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> 1

--- 투표 결과 ---

김일: 3표

김이: 1표

김삼: 1표
'''
num = int(input('후보자 수를 입력하시오 >>> '))

candidates = []
for i in range(1, num + 1):
    name = input(f'{i}번째 후보자의 이름을 입력하시오 >>> ')
    candidates.append(name)

votes = {}
for candidate in candidates:
    votes[candidate] = 0

num_votes = int(input(f'전체 투표 횟수를 입력하시오 >>> '))
for j in range(1, num_votes + 1):
    selected_candidate = int(input(f'{j}번째 투표 (1: 김일, 2: 김이, 3: 김삼) >>> '))
    if selected_candidate <= len(candidates):
        votes[selected_candidate] += 1
    else:
        print('잘못된 입력 값입니다.')

print('--- 투표 결과 ---')
for selected_candidate in candidates:
    print('f{selected_candidate}: {votes[selected_candidate]}표')