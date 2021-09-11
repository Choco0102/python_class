# 10주차 정규수업(10:00~12:00) mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[8주차 복습]
1. 튜플 자료형
2. 딕셔너리 자료형 
3. class의 개념과 필요성
'''

# [class]
## <class 생성 및 호출>
## <class 생성 문법>
## class 클래스 이름:
##     def 메서드 이름1(self, 입력변수1, 입력변수2, ...):
##         실행명령
##     def 메서드 이름2(self, 입력변수1, 입력변수2. ...):
##         실행명령

## <class 호출 문법>
## 클래스 선언하기: 인스턴스 = 클래스이름()
## 매서드 호출하기: 인스턴스.메서드()

## 연습문제2: 모든 자료형은 class이다.
## 정수형, 실수형, 문자열, 불린형 등의 다양한 자료형을 가진 변수를 선언 후
## type() 명령을 통해 자료형을 출력하여 보자(class 확인 할 것)
## + 추가적으로 .__dir__() 역시 출력해보자
'''
a = 12
b = 0.125
c = '안녕하세요'
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(a.__dir__())
print(b.__dir__())
print(c.__dir__())
print(d.__dir__())

'''
## class Mission1
## : Mission에 언급된 내용대로 Cat class를 만들어 보자
'''
class Cat:
    def cry(self):
        print("야옹")
    def tail_wag(self):
        print("야옹!야옹!")
    def translate_cry(self):
        print("하찮은 닝겐 나에게 밥을 대령해라!!")
    def translate_tailwag(self):
        print("놀아줘라 닝겐")

cat = Cat()
cat.cry()
cat.tail_wag()
cat.translate_cry()
cat.translate_tailwag()
'''
## <생성자>
## : 객체가 생성될 때 자동으로 호출되는 메서드.
## [문법] class 클래스이름:
##           def __init__(self, 입력변수들):
##               초기화 실행 문장

## 생성자 연습문제
## : Monster 클래스를 만들고 step에 따라 생성자와 메서드가 추가된 Monster 클래스를 만들어보자.
## step1) 가장 기본적인 Monster 클래스를 만들어 보자
##        : say 메서드만을 가지는 Monster 클래스
'''
class Monster:
    def say(self):
        print("나는 아주아주 무서운 몬스터다")

goblin = Monster()
goblin.say()
'''
## step2) Monster 클래스에 속성(name, health, attack, speed)을 추가하여 초기화해보자.
##        또한, 인스턴스 생성 시에 say의 내용이 출력되도록 만들어보자.
'''
class Monster:
    def __init__(self, name, health, attack, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
        print(f"나는 아주아주 무서운 {self.name}이다!")


goblin = Monster('고블린', 50, 4, 6)
wolf = Monster('늑대', 30, 5, 10)
'''
## step3) Monster 클래스에 메서드(decrease_health, get_health, info)를 추가한 후,
##        goblin과 wolf 객체를 생성하여 각 메서드들을 호출해보자.
'''
class Monster:
    def __init__(self, name, health, attack, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
        print(f"나는 아주아주 무서운 {self.name}이다!")

    def decrease_health(self, num):
        self.health -= num
    def get_health(self):
        return self.health
    def info(self):
        print(f"이름: {self.name}")
        print(f"체력: {self.health}")
        print(f"공격력: {self.attack}")
        print(f"속도: {self.speed}")


goblin = Monster('고블린', 50, 4, 6)
a = int(input("고블린에게 입힐 데미지를 입력하시오>> "))
goblin.decrease_health(a)
print(goblin.get_health())
goblin.info()

wolf = Monster('늑대', 30, 5, 10)
b = int(input("늑대에게 입힐 데미지를 입력하시오>> "))
wolf.decrease_health(b)
print(wolf.get_health())
wolf.info()
'''

## <상속>
## : 부모 클래스의 속성과 메서드를 자식클래스가 물려받을 수 있도록 만든 기능
## 상속을 사용하는 이유: 클래스들에 중복된 코드를 제거하고 유지보수를 하기 위해 사용하기 위해서 사용.

## <메서드 오버라이딩(덮어쓰기)>
## : 부모 클래스에 있는 메서드를 자식클래스에서 동일한 이름으로 다시 만드는 것

## 상속 연습문제
## :Monster 클래스를 만들고, 상속을 활용하여 Wolf, Shark, Dragon 클래스를 만들어,각각의 객체를 생성해보자.
##
## step1) 부모 클래스: Monster 클래스 정의하기
## - 속성: name, health, attack
## - 메서드: move("self.name 지상에서 이동하기"를 출력하는 메서드, 이후 해당 몬스터의 이동방법이 출력되도록 할 것임.)

class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def move(self):
        print(f"{self.name} 지상에서 이동하기")

## step2) 자식 클래스: Wolf, Shark, Dragon
## - Monster 클래스를 상속 받을 것.
## - 몬스터의 속성에 맞게 move를 메서드 오버라이딩할 것.
'''
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"{self.name} 헤엄치기")

class Dragon(Monster):
    def move(self):
        print(f"{self.name} 날기")

wolf = Wolf('늑대', 100, 20)
wolf.move()

shark = Shark('상어', 100, 50)
shark.move()

dragon = Dragon('용', 500000, 3000)
dragon.move()
'''
## <super()와 클래스변수>
## super(): 부모클래스의 메서드들의 내용들을 그대로 가져와  자식 클래스 추가하고 싶은 경우에 사용하는 명령
## 클래스변수: 해당 클래스로 만든 모든 객체들이 공유하는 변수

## super()와 클래스 변수 연습문제: RPG게임 업데이트
## : ‘상속 및 메서드 오버라이딩 연습문제’에서 만들었던 내용들을 업데이트해보자
## - 드래곤 클래스에 ‘인스턴스 속성’으로 ‘3개의 스킬(불뿜기, 꼬리치기, 날개치기)’을 추가
## - 드래곤이 스킬을 쓰면 속성 중 하나가 무작위로 사용되도록 설정(random 모듈 이용)


# [이번주 추가 문제: 한수]
## url: https://www.acmicpc.net/problem/1065
'''
import sys
import copy

N = int(sys.stdin.readline())

# <N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성해보자>

'''