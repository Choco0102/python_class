# 9주차 정규수업(10:00~12:00) mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[8주차 복습]
1. 반복문 mission: 무지개 그리기
2. 함수 (정의, 제어)
3. 튜플 자료형(이론)
'''

# [튜플과 딕셔너리]
## [튜플]
## : 간단하게 말해 "수정, 추가, 삭제가 불가능한 리스트" 라고 간주할 수 있다.
## 연습문제1: 튜플 만들기
## 2가지 방법으로 튜플을 선언해보고, 두 변수의 값고 자료형을 출력해보자.
'''
numbers1 = (1,2,3,4)             # ()로 튜플 만들기
numbers2 = 1,2,3,4             # ()없이 튜플 만들기
print(numbers1, type(numbers1))     #tuple
print(numbers2, type(numbers2))     #tuple
'''
## 연습문제2: 원소가 하나인 튜플 만들기
## 선언시 ,(쉽표)를 넣지 않은 경우와 쉼표를 넣어 변수를 만들고, 변수들의 값과 자료형을 비교해보자.
## ※ 결과를 비교해보는 것이 중요!!
'''
num1 = (23)         # ()로 만든 경우         #int
num2 = (23,)         # (,)로 만든 경우       #tuple
num3 = 23         # 숫자 1개만 넣어준 경우    #int
num4 = 23,         # 숫자, 로 만들어준 경우   #tuple
print("num1: ", num1, type(num1))
print("num2: ", num2, type(num2))
print("num3: ", num3, type(num3))
print("num4: ", num4, type(num4))
'''
## 연습문제3: 튜플 ↔ 리스트로 변환
## : tuple을 만들고 이를 list로 변환 후 값과 자료형을 출력한 후, 이를 다시 튜플로 바꾸어 같은 과정을 반복해보자.
'''
numbers = (100, 110, 10)
numbers = list(numbers)     # 튜플을 list로 변환하기
print(numbers, type(numbers))
numbers = tuple(numbers)    #list를 튜플로 변환하기
print(numbers, type(numbers))
'''
## 연습문제4: 패킹과 언패킹 그리고 a, b 값 바꾸기
## 4-1) 패킹과 언패킹을 하여 자료형을 출력해보자.
## 4-2) 패킹 언패킹 개념을 활용하여 a, b의 값 바꾸어보자
## ※ 결과를 확인하는 것이 중요!!
'''
# 패킹
a = 9
b = 27
numbers = a, b              # numbers로 a,b를 패킹해주기
print("numbers:", numbers, type(numbers))   # 결과확인(데이터 값, 자료형 확인)

# 언패킹
c, d = numbers      # numbers에 포함된 숫자를 c, d로 언패킹해주기 
print("c: ", c, type(c))
print("d: ", d, type(d), end='\n\n')        # 결과확인(데이터 값, 자료형 확인)

# 응용: a, b의 값 바꿔주기
print("a: ", a)
print("b: ", b)
a, b = b, a         
print("a: ", a)     # 결과 확인
print("b: ", b)

'''
## 연습문제5: 튜플과 관련된 함수
## ※ 결과 확인이 중요!!
'''
numbers = 100, 546, 896, 10, 777
print(max(numbers))         # max(): 튜플에서 최댓값을 반환하는 함수
print(min(numbers))         # min(): 튜플에서 최솟값을 반환하는 함수
print(sum(numbers))         # sum(): 튜플에 포함된 원소들의 함을 반환하는 함수
print(numbers.count(777))   # .count(): 입력한 숫자가 튜플에 몇 개 있는지 세어주는 함수(메서드)
print(numbers.index(246))   # .index(): 입력한 숫자의 인덱스를 반환해주는 함수(메서드)
'''

## [딕셔너리]
## : 키(key)와 데이터(value)를 가지고 있는 "사전과 같은 자료형"
## key값을 통해 value값을 불러올 수 있다.
'''
## 연습문제1: 딕셔너리 만들기
## : 자신이 좋아하는 youtuber 3~5명의 채널이름(key)과 구독자 수(value)로 dictionary 자료형을 만들어보자
## 만약, 남은 시간이 얼마 없다면, 미리 작성해놓은 데이터를 사용하도록 하자

youtuber = {
    "승우아빠" : 1460000,
    "백종원의 요리비책" : 5110000,
    "잇섭" : 1830000,
    "옥냥이" : 460000,
    "오킹TV" : 1110000
}
print(youtuber)

## 연습문제2: 딕셔너리 제어1-값에 접근하기
## : 자신이 가장 좋아하는 youtuber의 구독자 수를 출력해보자

print(youtuber["백종원의 요리비책"])     # ()안에 값에 접근하는 문장 넣어주기

## 연습문제3: 딕셔너리 제어2-값 할당(or 수정)하기
## : 자신이 가장 좋아하는 유투버의 구독자 수에 1000이 더 큰 숫자를 넣고 이를 출력해보자

youtuber["승우아빠"] += 1000                              # 딕셔너리 값 할당 명령 수행
print(youtuber["승우아빠"])

## 연습문제3: 딕셔너리 제어3-삭제하기
## : 자신이 두번째로 좋아하는 youtuber를 딕셔너리에서 삭제해보자

del youtuber["옥냥이"]                              # 딕셔너리 값 지우기 명령 수행
print(youtuber)

## 연습문제4: 딕셔너리 관련 함수
## .items(), .keys(), .values()의 결과와 데이터 타입을 출력해보자
## ※ 결과 확인이 중요!!

print(youtuber.items())
print(youtuber.keys())
print(youtuber.values())

'''
# [클래스(class)]
## 클래스와 객체
## 클래스: 객체를 만들기 위한 "설계도"
## 객체: 설계도로부터 만들어낸 "제품"

## 클래스를 사용하는 이유
## LOL 인벤 챔피언들 정보: https://lol.inven.co.kr/dataninfo/champion/compare.php
## LOL 혹은 자신이 좋아하는 게임의 캐릭터 3가지를 선택하여 해당 캐릭터의 정보(채력, 공격력, 이동속도)를 입력하고,
## "게임 시작 인사, 캐릭터 능력을 각각 출력(함수)"등을 수행하는 프로그램을 만들어 보자

## case1: class를 활용하지 않은 경우
'''
def character_info(name, attack, health, speed):
    print(f"[{name}]")
    print(f"기본 공격력: {attack}")
    print(f"기본 체력: {health}")
    print(f"기본 속도: {speed}")

character1_name = '리신'
character1_attack = 70
character1_health = 575
character1_speed = 345
print(f"{character1_name}님 소환사의 협곡에 오신 것을 환영합니다.")
character_info(character1_name, character1_attack, character1_health, character1_speed)

character2_name = '레넥톤'
character2_attack = 69
character2_health = 575
character2_speed = 345
print(f"{character2_name}님 소환사의 협곡에 오신 것을 환영합니다.")
character_info(character2_name, character2_attack, character2_health, character2_speed)
'''
## case2: 클래스를 사용한 경우
class character:
    def __init__(self, name, attack, health, speed):
        self.name = name
        self.attack = attack
        self.health = health
        self.speed = speed
        print(f"{self.name}님 소환사의 협곡에 오신 것을 환영합니다.")

    def character_info (self):
        print(f"[{self.name}]")
        print(f"기본 공격력: {self.attack}")
        print(f"기본 체력: {self.health}")
        print(f"기본 속도: {self.speed}")

leesin = character("리신", 70, 575, 345)
renekton = character("레넥톤", 71, 600, 345)

leesin.character_info()
renekton.character_info()
