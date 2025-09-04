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
logo = '''                                                                                      
        ,--,                        ,--.                      ____                          ,--. 
      ,--.'|   ,---,              ,--.'|  ,----..           ,'  , `.   ,---,              ,--.'| 
   ,--,  | :  '  .' \         ,--,:  : | /   /   \       ,-+-,.' _ |  '  .' \         ,--,:  : | 
,---.'|  : ' /  ;    '.    ,`--.'`|  ' :|   :     :   ,-+-. ;   , || /  ;    '.    ,`--.'`|  ' : 
|   | : _' |:  :       \   |   :  :  | |.   |  ;. /  ,--.'|'   |  ;|:  :       \   |   :  :  | | 
:   : |.'  |:  |   /\   \  :   |   \ | :.   ; /--`  |   |  ,', |  '::  |   /\   \  :   |   \ | : 
|   ' '  ; :|  :  ' ;.   : |   : '  '; |;   | ;  __ |   | /  | |  |||  :  ' ;.   : |   : '  '; | 
'   |  .'. ||  |  ;/  \   \'   ' ;.    ;|   : |.' .''   | :  | :  |,|  |  ;/  \   \'   ' ;.    ; 
|   | :  | ''  :  | \  \ ,'|   | | \   |.   | '_.' :;   . |  ; |--' '  :  | \  \ ,'|   | | \   | 
'   : |  : ;|  |  '  '--'  '   : |  ; .''   ; : \  ||   : |  | ,    |  |  '  '--'  '   : |  ; .' 
|   | '  ,/ |  :  :        |   | '`--'  '   | '/  .'|   : '  |/     |  :  :        |   | '`--'   
;   : ;--'  |  | ,'        '   : |      |   :    /  ;   | |`-'      |  | ,'        '   : |       
|   ,/      `--''          ;   |.'       \   \ .'   |   ;/          `--''          ;   |.'       
'---'                      '---'          `---`     '---'                          '---'                                                                                      
'''
print(logo)

lives = 6
word_list = [
    "abolish", "contemporary", "absorb", "accommodate", "advise", "acquire", "adequate", "affect", "afford", "aggressive",
    "aid", "alert", "allege", "allowance", "amuse", "analyze", "ancient", "announce", "anxious", "apparent",
    "appeal", "appreciate", "approach", "appropriate", "approve", "argue", "arise", "artificial", "ascend", "assert",
    "assess", "associate", "assume", "attempt", "attend", "attitude", "authority", "avoid", "aware", "benefit",
    "bizarre", "blame", "boost", "boundary", "brave", "breach", "breathe", "broad", "capture", "career",
    "cautious", "celebrate", "challenge", "character", "circumstance", "civil", "claim", "coexist", "collapse", "commit",
    "communicate", "community", "compare", "compete", "complain", "complex", "complicate", "comply", "compose", "comprehend",
    "comprise", "compromise", "conceal", "concentrate", "concept", "concern", "conclude", "concrete", "condemn", "conduct",
    "confer", "confess", "confine", "confirm", "conflict", "conform", "confront", "consecutive", "consequence", "conserve",
    "considerable", "consistent", "constitute", "construct", "consult", "consume", "contact", "contain", "contend", "context",
    "contract", "contradict", "contribute", "controversy", "convention", "convert", "convince", "cooperate", "correspond", "courage",
    "critical", "crucial", "cultivate", "curious", "decline", "decrease", "dedicate", "define", "degrade", "delay",
    "deliberate", "demand", "demonstrate", "deny", "depart", "depend", "depict", "depress", "derive", "descend",
    "describe", "deserve", "designate", "desire", "desperate", "destroy", "determine", "develop", "devise", "devote",
    "diagnose", "differ", "difficult", "diligent", "diminish", "disappear", "disappoint", "discipline", "discover", "discourage",
    "discuss", "disrupt", "distinct", "distinguish", "distort", "diverse", "divide", "domestic", "dominate", "dramatic",
    "durable", "dynamic", "eager", "eccentric", "efficient", "elaborate", "elect", "eliminate", "embrace", "emerge",
    "emphasize", "enable", "encourage", "endorse", "engage", "enhance", "enormous", "entertain", "entire", "environment",
    "erode", "essential", "establish", "evaluate", "evident", "evolve", "exaggerate", "exceed", "excellent", "exception",
    "exhaust", "exhibit", "exist", "expand", "expect", "expensive", "experience", "explain", "explicit", "explore",
    "expose", "express", "extend", "extraordinary", "fabricate", "facilitate", "familiar", "fascinate", "favorable", "feasible",
    "feature", "federal", "feeble", "fierce", "finance", "flexible", "flourish", "fluctuate", "focus", "forbid",
    "forecast", "formulate", "foster", "fragile", "frequent", "fulfill", "fundamental", "furthermore", "generate", "generous"
]
chosen_word = random.choice(word_list)
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

    print(stages[lives])

    if '_' not in display:
        print('정답입니다!')
        end_of_game = True
        print(f'정답은 {chosen_word}입니다.')

    print(' '.join(display))

# logo 유무 / word_list 부족 / 혹시나 리팩토링 가능한지 여부