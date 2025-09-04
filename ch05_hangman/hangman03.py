import random
'''
''.join(반복가능객체) method : '.' 앞에 있는 문자열을 기준으로 반복 가능 객체의 element들을 합쳐서 str로 합쳐주는 method
'''
temp = ['배', '고', '프', '다']
feeling = ''.join(temp)
print(feeling)
result = ''

# for letter in temp:
#     result += letter

print(result)

feeling2 = '/'.join(temp)
print(feeling2)
'''
이상의 예시는 display를 다시 재조합하여 str으로 바꿀 때 사용할 것
'''

word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)

# todo - 1 : 비어있는 리스트 선언
display = []

# todo - 2 : chosen_word의 문자 개수만금 '_' display에 추가
for _ in range(len(chosen_word)): # i 쓰이지 않아 -> _
    display.append('_')
print(display)

# todo - 3 : 사용자가 추측을 반복할 수 있도록 while 반복문 작성. 사용자가 chosen_word의 모든 문자열들을 맞추었을 때, 즉 display에 더이상 '_'가 없을 때 반복문 종료, 종료 후 print('정답입니다 !')


while '_' in display:
    guess = input('알파벳을 입력하세요 >>> ').lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)

print('정답입니다 !')

# todo - 4 : 정답을 보여줄 때 apple 이라면 a p p l e 로 출력 ( .join 메서드 사용 )
correct_word = ' '.join(display)
print(correct_word)