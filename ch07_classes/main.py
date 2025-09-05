'''
클래스 정의 형식 :
class 클래스명(pascal case) :
    본문

객체 생성 형식 :
객체이름 = 클래스명() # new 아님

'''
# 클래스 정의 형식 예시
class WaffleMachine:
    pass

# 객체 생성 에시
waffle = WaffleMachine()
print(waffle)   # result : <__main__.WaffleMachine object at 0x0000022104F11550>

'''
1. 클래스의 기본 구성
    객체를 만들어내는 클래스는 객체가 가져야 할 구성 요소를 지님
    객체를 생성하기 위해서는 객체가 가져야 할 '값'과 '기능'을 지녀야 함

    값 = 속성(attribute)
    기능 = 메서드(method)

    클래스를 구성하는 속성은 두 가지로 구분됨
        1) 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수(java -> static)
        2) 인스턴스 변수 : 인스턴트들이 개별적으로 가지는 변수
    
    메서드는 특징에 따라서
        1) 클래스 메서드
        2) 정적 메서드
        3) 인스턴스 메서드 
        자바에서 정적 메서드 = 파이썬 클래스 메서드
        정적 메서드는 따로 있다고 볼 수도 있고 자바의 정적 메서드가 파이썬의 클래스메서드 + 정적메서드라고 볼 수도 있음
        
        그리고 자바에서는 this 썼는데(아직 생성되지 않은 객체명을 도입할 수 없으니 하용하는 키워드), 파이썬 에서는 self씀
        
        self 키워드
        인스턴스 변수에서 각각의 객체를 의미하기 위해서 self 키워드를 붙여줌
        인스턴스 메서드에서의 첫 번째 매개변수로 '항상' self를 추가해야 함
'''
# 클래스 정의
class Person:
    # 메서드 정의(함수가 클래스 내에 있으니까)
    def set_info(self, name, age, tel, address): # call2() / setter
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

    def show_info(self):    #call1()
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'연락처 : {self.tel}')
        print(f'주소 : {self.address}')

    def display_info(self):
        return (f'제 이름은 {self.name}이고, {self.age}살입니다.\n연락처는 {self.tel}인데, {self.address}에 살고 있습니다.')


# 객체 생성
person01 = Person()
# 메서드 호출
person01.set_info('김일', 20, '010-1234-5678', '서울특별시 마포구')
person01.show_info()

# ex
person02 = Person()
person02.set_info('하슬', 22, '010-9742-1812', '부산광역시 강서구')
print(person02.display_info())

