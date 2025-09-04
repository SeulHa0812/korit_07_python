import random

word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)

#todo - 1 : 비어있는 list인 display
display = []
# print(display)
# display.append('김')
# print(display)
# display.append('일')
# display.append(1)
# print(display)

# todo - 2: 이상의 코드라인을 참조하여 chosen_word의 각 문자 개수 마다 '_'를 추가하시오. 예를 들어 chosen_word == 'apple'이라면 display = [ '_', '_', '_', '_', '_' ]이 되어야 함. 즉, chosen_word의 문자 개수 만큼 '_'가 있어야 함.
for _ in range(len(chosen_word)): # i 쓰이지 않아 -> _
    display.append('_')
print(display)
# todo - 3: chosen_word의 각 문자들을 반복시키시오. 만약 그 위치의 문자가 guess와 일치하면, 해당 위치의 display에서 문자 공개. 예를 들어, 사용자가 'p'를 입력, chosen_word == apple -> display = [ '_', 'p', 'p', '_', '_' ]
guess = input('알파벳을 입력하세요 >>> ').lower()
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess

print(display)