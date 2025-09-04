import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
'''
이상의 코드라인을 확인하면 내부의 element가 복수의 라인으로 이루어진 str인 list라고 할 수 있음
'''
# todo - 1 : 남은 기회 숫자 추적 위한 lives 변수 선언 및 6으로 초기화
lives = 6

# todo - 2 : hangman03 참조하여 while 반복문 바깥 완성
word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for _ in range(len(chosen_word)): # i 쓰이지 않아 -> _
    display.append('_')
print(display)

# todo - 3 : whlie문의 조건을 수정하여 6 번의 기회가 소진되면 반복문 종료
end_of_game = False
while not end_of_game:
    guess = input('알파벳을 입력하세요 >>> ').lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f'{lives} 번의 기회가 남았습니다.')
        if lives == 0:
            print(f'모든 기회를 잃었습니다. 정답은: {chosen_word} 입니다.')
            end_of_game = True

    print(stages[lives])

    if '_' not in display:
        print('정답입니다!')
        end_of_game = True # 이 시점에 end_of_game이 True가 되었으므로 다음 반복문 실행 x -> 99 line 실행
        # break # 99 line 실행 x
        print(f'정답은 {chosen_word}입니다.')

    print(' '.join(display))

# todo - 4 : lives의 변수와 stages 리스트의 관계를 파악하여 guess를 입력할 때 마다 올바른 stages의 element가 출력될 수 있도록 작성

# logo 유무 / word_list 부족 / 혹시나 리팩토링 가능한지 여부