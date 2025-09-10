from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# python 객체 만드는 방식. 이전과 차이가 있다면 외부 모듈(파일)에서 가지고 온 클래스의 객체를 생성했다는 점. Scanner scanner = new Scanner(System.in);과 같음

# 이제 뭐할꺼냐면 coffee_maker / money_machine / menu 모듈은 하나도 안건들이고 main에만 코드를 작성해서 pop version과 동일한 기능을 하는 coffee_machine을 만들 것
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까? ({menu.get_items()}) >>> ')

    if choice == 'off':
        is_on = False
        print('자판기가 종료되었습니다.')
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink == None: # choice에 오타가 있을 경우  None이 반환되기 떄문에 고전적 예외 처리
            continue # continue 실행되면 이하의 코드라인 실행x,  while 가장 앞 부분으로 돌아가서 다음 반복 실행

        # 음료 이름을 입력 받은 시점부터의 프로세스를 떠올려서 코들르 작성하셔야함 함. 이때 고려해야할 것은 절차지향 방식으로 코딩했을 떄의 과정과, 현재 참조해야 하는 파이썬 모듈들의 매개변수 차이와 메서드 작동 원리의 차이를 감안해서 코드를 쓸 필요가 있다는 점
        # pop version의 함수 작성 순서대로 저희가 작동하도록 했음
        # is_resources_enough(order_ingredient) / is_resource_sufficient(drink)
        if coffee_maker.is_resource_sufficient(drink) :
            # 조건문을 이용해 process_coins()와 make_payment()를 활용하여, 모든 것이 true일 때 작동 중입니다를 출력할 수 있도록 작성
            if money_machine.make_payment(drink.cost) :
                coffee_maker.make_coffee(drink)







