MENU = {
    '에스프레소': {
        '재료': {
            '물': 50,
            '커피' : 18,
        },
        '가격': 1.5,
    },
    '라떼': {
        '재료': {
            '물': 200,
            '우유' : 150,
            '커피' : 24,
        },
        '가격': 2.5,
    },
    '카푸치노': {
        '재료': {
            '물': 250,
            '우유' : 100,
            '커피' : 24,
        },
        '가격': 3.0,
    },
}
profit = 0
resources = {
    '물': 300,
    '우유': 200,
    '커피': 100,
}
# 함수 정의 영역
def is_resources_enough(order_ingredient): # 만약에 특정 함수/메서드의 결과값이 boolean이라면 대개 다음 조건문/반복문의 조건식으로 쓰이는 경우가 많음. 함수형 프로그래밍 개념을 떠올리면 됨
   """
   DocString: 함수 / 클래스 / 메서드가 어떤 작동을 하는지 '사람들에게' 살명해주는 기능.
   주문 받은 음료를 resources에서 재료 차감을 하고 난 후, 음료 만들기가 가능하면 True 반환 하니면 False 반환
   :param : order_ingredient
   :return : True/False
   """
   for item in order_ingredient: # order_ingredient datatype == dictionary -> 반복문 돌리면 key 나옴, 그 근거는?
       if order_ingredient[item] > resources[item]:
           print(f'죄송합니다. {item}이(가) 부족합니다.')
           return False
   return True
def process_coins() :
    """동전들을 입력 받아 전체 금액을 반환하는 함수 call3() 유형"""
    # 쿼터, 다임, 니켈, 페니 네 종류의 동전
    '''
    쿼터 = 0.25 달러
    다임 = 0.1
    니켈 = 0.05
    페니 = 0.01
    '''
    sum = 0
    # 여기에 로직
    sum += float(input('How many quarters?')) * 0.25
    sum += float(input('How many dimes?')) * 0.1
    sum += float(input('How many nickels?')) * 0.05
    sum += float(input('How many pennies?')) * 0.01
    return sum

def make_coffee(drink_name, order_ingredient):
    """
    resources에 있는 재료에서 메뉴['음료명']['재료']들을 차감함
        -> 차감은 is_resources_enough() True였기 때문에 무조건 0이상이 나옴
    :param drink_name: str
    :param order_ingredient: dict
    :return: call2()
    """
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f'{drink_name}이(가) 나왔습니다. 맛있게 드세요 !!')

# todo - 6 : 해당 총합을 가지고, 총합이 '선택한' 음료 가격보다 높다면 다음 과정으로 넘어갈 필요 있음.
def is_transaction_successful(money_received, drink_cost) :
    """process_coins()의 결과값과 음료 가격을 매개변수로 받아 받은 동전의 총합이 음료 가격보다 높으면 True or False. 그리고 True인 경우에 profit에 음료 가격만큼 추가해줘야 하고, False인 경우에는 받은 동전들을 반환해주는 안내문 출력."""
    change = money_received - drink_cost
    if change >= 0 :
        # 이러면 음료 제조 과정으로 넘어가야함. 그리고 profit에 추가도 해줘야 하고
        global profit # 전역 변수인 profit 함수 내부에서 사용하기 위한 키워드
        profit += drink_cost # 근데 함수 호출을 통한 전역 변수의 값 변화는 권장하지 않음.
        print(f'잔돈 ${change}을(를) 반환합니다.')
        return True # 그래야 음료 제조 과정의 조건식으로 쓸 수 있으니까
    else :
        print(f'금액이 충분하지 않습니다. ${money_received}를 반환합니다.')
        return False # 음료 제조 과정의 조건식으로 쓰이더라도 실행 안됨.


# todo - 1 : 커피 머신이 반복적으로 돌아가야 하는데, off를 입력 받으면 종료가 이루어져야 함.

# 관련 변수 선언 및 초기와
is_on = True
while is_on:
    # 반복문 내부에서 입력받아야 하니까 여기다가 선언 및 초기화
    choice = input('어떤 음료를 드시겠습니까? (에스프레소 / 라떼 / 카푸치노) >>> ')
    # todo - 2 만약에 choice 변수에 들어간 데이터가 'off'라면 반복문을 종료하도록 나머지 코드 작성
    if choice == 'off':
        is_on = False # 이번 반복 전부 실행, 다음 반복에서 종료
        print('자판기가 종료되었습니다.')
        #break 바로 종료
# todo - 3 : 사용자가 프롬포트에 "report"를 입력하면 현재 자원 값을 보여주는 보고서 생성
    elif choice == 'report':
        print(f'물 : {resources['물']}ml')
        print(f'우유 : {resources['우유']}ml')
        print(f'커피 : {resources['커피']}g')
        print(f'수익 : ${profit}')
# todo - 4 : choice == 에스프레소 / 라떼 / 카푸치노 중 하나일 때 작성하는 부분
    elif choice in ['에스프레소', '라떼', '카푸치노']:
        # 자판기에서 choice에 정확한 음료 이름을 입력했을 때의 처리 과정
        # 1. 자원 충분한지 확인 ( T / F )
        # 2. T라면 돈을 입력 받을 수 있도록 -> 동전 입력 받아서 합 연산한 후에 음료의 가격 이상인지 확인하여 T / F 반환
        # 3. T라면 음료를 반환해야하는데, resources에 있는 수량 감소, profit에는 음료 가격만큼 증가 시킬 필요 있음. 그리고 동전 받은 것에서 음료 가격 만큼 배고 반환도 해줘야 함.
        if is_resources_enough(MENU[choice]['재료']) : # resources가 아니라 order_ingredient를 반복문 돌리는 이유는 에스프레소일 때 오류 발생 때문. 에스프레소의 재료에는 우유가 없는데 resources에는 있는 상태가 됨. 그래서 order_ingredient['우유'] 부분에서 오류가 발생하게 됨
            # 이상의 조건식이 True라면 동전 처리해야함
            money_received = process_coins()
            # 여기의 money_reveived는 전역 변수. 그리고 process_coin()의 결과값을 변수에 담음
            if is_transaction_successful(money_received=money_received, drink_cost=MENU[choice]['가격']) :
                # 이제 여기에 음료 제조 과정을 작성하면 됨
                # 재료를 이제 실질적으로 차감하고, 음료를 만들어서 사용자에게 제공해야 함
                # 재료 차감 파트를 is_resources_enough() 함수를 참조하여 여기서 작성하세요.
                # 해당 작성 결과를 함수화하도록 할 예정
                # for key in MENU[choice]['재료']:
                #     resources[key] -= MENU[choice]['재료'][key]
                # print(f'{choice}이(가) 나왔습니다. 맛있게 드세요 !!')
                make_coffee(drink_name=choice, order_ingredient=MENU[choice]['재료'])

# todo - 5 : choice가 이상의 조건을 충족하지 않을 때 '잘못 입력하셨습니다. 다시 입력하세요'를 출력하는 부분
    else:
        print('잘못 입력하셨습니다. 다시 입력하세요.')
'''
현재 자판기 내에 있는 물 / 우유 / 커피 / 금액 양에서 라떼 한잔을 뽑고 나서의 물 / 우유 / 커피 / 금액의 변동을 콘솔에 출력하시오.

실행 예
물 : xml
우유 : xml
커피 : xg
수익 : $x
'''
# profit += MENU['라떼']['가격']
# print(f'수익 : ${profit}')
#
# for key in MENU['라떼']['재료'] :
#     resources[key] -= MENU['라떼']['재료'][key]
#
# print(f'물 : {resources['물']}ml')
# print(f'우유 : {resources['우유']}ml')
# print(f'커피 : {resources['커피']}g')
'''
금일 수업에서 필요한 value들을 다양한 방법을(key를 일일이 지정해서 넘어가거나 / 반복문을 작성하거나) 통해 추출한 후에 이를 연산하는 것까지 처리하고 있음.
이상의 코드는 그 예시이고, 앞으로의 데이터를 다루는 부분에 있어서 매우 중요함.
SQL에서도 각각 칼럼에 있는 값들을 필요한 것들을 추출해서 연산한 후에 깁계함수를 하용하는 등의 으용ㅇ이 있을 수 있으니 파이썬으로 작성하는 법 뿐만 아니라 원리 자체를 학습하는게 좋음.
'''
