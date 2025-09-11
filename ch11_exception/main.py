'''
1. 예외 처리의 필요성
    1) 예외(exception): 개발자가 직접 처리할 수 있는 문제
    2) 오류(error): 개발자가 처리할 수 없는 문제

    3) 예외 처리의 목적:
        어떤 문제가 발생했을 때 그 문제를 해결해주는 것이 안리ㅏ, 발생된 문제로 인해 프로그램이 비정상적으로 종료되는 것을 막고, 사용자에게 발생한 문제에 대해 정보를 전달하기 위함.

2. 예외 처리
    1) 고전적 예외 처리
'''
from prettytable import PrettyTable

# a = int(input('나누는 수(제수)를 입력하세요 >>> '))
# b =int(input('나누어지는 수(피제수)를 입력하세요 >>> '))
# result = b / a
# if a == 0:
#     print('0으로 나눌 수 없습니다.')
# else:
#     result = b / a
'''
어떤 값이든 0으로 나눌 수 없기 때문에 if a == 0 을 통해 0으로 나누는 것을 아예 시도할 수 없도록 예외처리를 함.

여기서 생각할 수 있는 문제는:
    1) 어떤 문제가 발생할 지 예상할 수 있어야 미리 대비 가능
    2) 어떤 문제가 발생할 지 예상할 수 있더라도 대비할 수 없는 경우가 있음

3) 예외 처리의 종류
'''
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.field_names = ['순번', '예외 클래스', '의미']
#
# table.add_row([1, "BaseException", "최상위 예외 클래스"])
# table.add_row([2, "Exception", "대부분 예외 클래스의 슈퍼 클래스"])
# table.add_row([3, "ArithemeticError", "산술 연산에 문제가 있을 때"])
# table.add_row([4, "AttributeError", "잘못된 속성을 참조할 때"])
# table.add_row([5, "EOFError", "파일에서 더 이상 읽어 들일 데이터가 없을 때"])
# table.add_row([6, "ModuleNotFoundError", "import할 모듈이 없을 때"])
# table.add_row([7, "FileNotFoundError", "존재하지 않는 파일일 때"])
# table.add_row([8, "IndexError", "잘못된 인덱스를 사용할 때"])
# table.add_row([9, "NameError", "잘못된 이름(변수)을 사용할 때"])
# table.add_row([10, "SyntaxError", "문법이 틀렸을 때"])
# table.add_row([11, "TypeError", "계산하려는 데이터의 유형이 잘못되었을 때"])
# table.add_row([12, "ValueError", "계산하려는 데이터의 값이 잘못되었을 때"])
#
# print(table)
'''
4. 예외 처리 방식
    1) 모든 예외를 처리하는 방식 -> try / except / finally
    형식 :
try :
    코드 작성 영역
except :
    예외 발생 시 처리 영역
finally :
    언제나 실행되는 영역
'''
# try :
#     a = int(input('나누는 수(제수)를 입력하세요 >>> '))
#     b = int(input('나누어지는 수(피제수)를 입력하세요 >>> '))
#     print('b / a = {b/a}')
# except :
#     print('예외가 발생했습니다.')

'''
기본 예제

다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램
'''
# try :
#     height = input('키를 입력하세요 >>> ')
#     height = round(height)
#     print(f'입력하신 키는 {height}cm로 처리됩니다.')
# except :
#     print('예외가 발생했습니다.')

'''
1) 특정 예외만 처리하는 방식
    try / except 사용 -> 기본적으로 예외 종류 상관없이 모든 예외가 처리됨
    
    1)-1. 0으로 나누려고하는 경우 -> 0으로 나눌 수 없습니다.
    1)-2. 정수가 아닌 값을 입력하는 경우 -> 정수만 입력할 수 있습니다.
    등으로 특정 예외에 따른 서로 다른 안내문을 제시한다고 하면,
    except문 뒤에 처리하고자 하는 예외를 모두 명시하면 됨.
'''
# try :
#     a = int(input('나누는 수(정수)를 입력하세요 >>> '))
#     b = int(input('나누어지는 수(정수)를 입력하세요 >>> '))
#     print('b / a = {b/a}')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except TypeError:
#     print('나눌 때 자료형이 일치하지 않습니다.')
# except ValueError:
#     print('정수만 입력할 수 있습니다.')
'''
    거의 모든 예외는 Exception 클래스의 서브 클래스에 해당함. 따라서 모든 예외는 Exception의 인스턴스가 됨. 다음과 같이 except의 마지막에 exception을 명시하면 예상하지 못한 예외들도 웬만하면 처리 됨.
    
형식:
try :
    코드 작성 영역
except 예외클래스1 :
    예외메시지1
except 예외클래스2 :
    예외메시지2
...
except Exception :
    예외메시지n
finally :
    항시 실행되는 코드 영역
    
자바에서와 동일하게 exception이 가장 상위에 있게 되면 모든 예외가 전부 Exception으로 잡히기 때문에 순서 역시 중요

3. 예외 메시지 처리하기
    이상까지는 특정 예외가 발생했을 떄 저희가 메시지를 커스텀해서 사용했지만, 기본적으로 이미 에외 메시지를 가지고 있는 경우도 있음.
    default exception message를 출력하는 방식 학습

형식 :
try :
    코드 작성 영역
except 예외클래스 as 예외메시지:
    예외 발생 시 처리 영역
'''
# z = [ 10, 20, 30, 40, 50 ]
#
# try :
#     print(z[10])
# except IndexError as e:
#     print(e)

'''
4. else / finally
    try / except 문에 else / finally를 달 수 있는데,
    else: 예외가 발생하지 않으면 처리되는 구문
    finally: 예외 발생 여부과 관계 없이 맨 마지막에 항상 처리되는 구문
'''
# try:
#     a = int(input('나누는 수를 정수로 입력하세요 >>> '))
#     b = int(input('나누어지는 수를 정수로 입력하세요 >>> '))
#     result = b / a # 예외가 발생할 수 있는 구간이 try문 내에 있어야만 함.
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else :
#     print(f'b / a = {result}')
# finally:
#     print('프로그램이 종료되었습니다.')

'''
5. 강제로 예외를 발생시키기
    어떤 사람이 나이를 정수로 입력받는 프로그램을 사용한다고 가정했을 때,
    컴퓨터 상으로는(그리고 파이썬 상으로는) -1000이 정수이기 때문에 예외가 발생하지 않음(그래서 우리는 0미만 200초과를 조건문으로 처리하는 것을 학습했음).
    하지만 -1000살이 되는 것이 불가능하기 때문에 조건문이 아니라 직접 예외를 발생시켜서 처리하는 방법을 학습함. -> raise 문

형식 :
raise 예외클래스()

또는 
raise 예외클래스(예외메시지)

raise의 경우 강제로 예외를 발생시키다는 점에서 주로 사용되는 예외 클래스는 
Exception임
'''
# try :
#     age = int(input('나이를 입력하세요  >>> '))
#     if age < 0 or age > 200:
#         raise Exception('강제로 발생시킨 예외입니다.') # 생성자 호출
# except Exception as e:
#     print('발생한 예외 메시지는 다음과 같습니다.')
#     print(e)

'''
이상은 특정 예외가 아니라 173번으로 넘어가기만 하면 바로 예외 발생

즉 age에 가능한 정수값을 넣더라도 예외가 발생하기 때문에 단독으로 처리가 안됨.
그렇다면 이 부분에서는 조건문을 이용해서 특정 조건일 때만 예외로 넘기는 추가 코드가 필요하다고 할 수 있음.

6. 사용자 정의 예외 클래스
    음수를 입력 받을 때 강제로 예외를 발생시키는 예외 클래스를 정의
'''
# class NegativeAgeError(Exception):  # Exception 클래스를 상속받았다는 의미
#     """사용자 정의 예외 클래스 : 나이가 음수일 때 발생"""
#     pass
# # 예외를 발생시키지만 하면 되기 때문에 뭐 굳이 코드를 쓸 필요는 없음.
# # Exception 클래스를 상속 받았으면 슈퍼 클래스의 속성/method를 사용할 수 있음
# class TooManyAgeError(Exception):
#     pass
#
# try :
#     age = int(input('나이를 입력하세요 >>> '))
#     if age < 0 :
#         raise NegativeAgeError('나이는 음수일 수 없습니다.')
#     elif age > 200 :
#         raise TooManyAgeError('200살 초과된 나이를 입력할 수 없습니다.')
#
# except NegativeAgeError as e:
#     print('발생한 예외 메시지는 다음과 같습니다.')
#     print(e)
#
# except TooManyAgeError as e:
#     print('발생한 예외 메시지는 다음과 같습니다.')
#     print(e)
# else :
#     print(f'당신의 나이는 {age} 살 입니다.')

'''
과제: 
나이가 200살 초과일 때 TooManyAgeError 예외를 발생시켜서 
'200살 초과된 나이를 입력할 수 없습니다.' 라는 메시지를 출력할 수 있도록 이상의 코드 수정
'''

'''
추가 과제
'''
# class ScoreOutOfRangeError(Exception):
#     pass
#
# try :
#     str_score = input('점수를 입력하세요 >>> ')
#     score = int(str_score)
#     if score < 0 or score > 100:
#         raise ScoreOutOfRangeError('점수는 0이상 100이하입니다.')
#
# except ScoreOutOfRangeError as e:
#     print(e)
#
# except ValueError:
#     if "." in str_score:
#         print('정수로 입력해야 합니다.')
#     else:
#         print('점수는 숫자로 입력해야 합니다.')
#
# except Exception as e:
#     print(e)
#
# else:
#     if score >= 80:
#         print("합격")
#     else:
#         print("불합격")
#
#
# finally:
#     print('프로그램이 종료되었습니다.')

'''
예제 3
'''
# try :
#     number = input('숫자를 입력하세요 >>> ')
#     number = int(number)
#     result = 100 / number
#
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
#
# except ValueError:
#     print('숫자만 입력할 수 있습니다.')
#
# else :
#     print(result)
#     print('정상적으로 처리되었습니다.')
# finally:
#     print('프로그램이 종료되었습니다.')

'''
예제 4
'''
# class NegativeNumIndexError(Exception):
#     pass
# my_list = [10, 20, 30, 40, 50]
#
# try :
#     index_number = int(input('인덱스 넘버를 입력하세요 >>> '))
#
#     if index_number < 0:
#         raise NegativeNumIndexError
#     print(my_list[index_number])
#
# except NegativeNumIndexError:
#     print('음수는 입력할 수 없습니다.')
#
# except IndexError:
#     print('리스트의 범위를 벗어났습니다.')
#
# except ValueError as e:
#     print(e)
#
# except Exception as e:
#     print(e)
#
# else:
#     print('정상적으로 처리되었습니다.')
#
# finally:
#     print('프로그램 종료')

'''
예제 5
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 객체 생성
person1 = Person(name='김일', age=21)
print(vars(person1)) # vars(객체명) : 객체의 속성명 - 값을 dictionary로 만들어줌
print(getattr(person1, 'age')) # 결과값 : 21
# getattr()의 두 번째 argument는 인스턴스 변수명을 받음 -> 그 데이터를 str로 받음
print(getattr(person1, 'name')) # 결과값 : 김일

try :
    attr = input('속성명을 입력하세요 >>> ')
    attr_value = getattr(person1, attr)
    print(attr_value)

except AttributeError:
    print('존재하지 않는 속성입니다,')
else:
    print('정상적으로 처리되었습니다.')
finally:
    print('프로그램 종료')

'''
getattr(객체명, 속성명_str) - 특정 객체의 두번째 argument와 일치하는 속성명의 값을 return
vars(객체명) - 특정 객체의 속성명-속성값 쌍을 dictionary 형태의 key-value 쌍으로 변환
'''
person1_dict = vars(person1)
print(person1_dict)
attr_key = input('출력할 속성명을 입력하세요 >>> ')
print(person1_dict[attr_key])

