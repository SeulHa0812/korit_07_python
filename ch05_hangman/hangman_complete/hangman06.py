import random
import hangman_arts
import hangman_word_list

# 즉 logo / stages와 같은 변수는 아님

# 외부의 hangman_word_list에 있는 word_list를 참조해서 저희는 chosen_word를 만들 필요 있음
print(hangman_arts.logo)
chosen_word = random.choice(hangman_word_list.word_list)
print(chosen_word)

lives = 6
display = []
for _ in range(len(chosen_word)):
    display.append('_')

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

    print(hangman_arts.stages[lives])

    if '_' not in display:
        print('정답입니다!')
        end_of_game = True
        print(f'정답은 {chosen_word}입니다.')

    print(' '.join(display))