'''
외부 패키지의 설치 #1 settings를 통한 방법

'''
from prettytable import PrettyTable
from pokemon_data import pokemon_data

# PrettyTable의 객체 생성
table = PrettyTable()

table.field_names = ['이름', '나이', '주소'] # column header

for pokemon in pokemon_data:
    table.add_row(pokemon)
print(table)

table.add_rows(pokemon_data)
print(table)