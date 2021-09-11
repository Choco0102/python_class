# 11주차 정규수업(10:00~12:00) mission <python 기초반 마지막 수업>
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[10주차 복습]
1. class 생성 및 호출방법
2. 상속
3. 메서드 오버라이딩
'''

# [class]
## <super()와 클래스변수>
## super(): 부모클래스의 메서드들의 내용들을 그대로 가져와  자식 클래스 추가하고 싶은 경우에 사용하는 명령
## 클래스변수: 해당 클래스로 만든 모든 객체들이 공유하는 변수

## super()와 클래스 변수 연습문제: RPG게임 업데이트
## : ‘상속 및 메서드 오버라이딩 연습문제’에서 만들었던 내용들을 업데이트해보자
## - 드래곤 클래스에 ‘인스턴스 속성’으로 ‘3개의 스킬(불뿜기, 꼬리치기, 날개치기)’을 추가
## - 드래곤이 스킬을 쓰면 속성 중 하나가 무작위로 사용되도록 설정(random 모듈 이용)
'''
import random
class Monster:
    number = 1000                               #클래스 변수
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.number -= 1

    def move(self):
        print(f"{self.name} 지상에서 이동하기")

class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"{self.name} 헤엄치기")

class Dragon(Monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)        #29번부터 32번줄 내용을 super()로 대체한다.
        self.skills = ['불뿜기', '꼬리치기', '날개치기']
    def move(self):
        print(f"{self.name} 날기")
    def skill(self):
        print(f'스킬 {self.skills[random.randint(0,2)]}을 사용했다.')

wolf = Wolf('늑대', 100, 50)
wolf.move()
print(wolf.number)

shark = Shark('상어', 200, 100)
shark.move()
print(shark.number)

dragon = Dragon('드래곤', 1000, 350)
dragon.move()
dragon.skill()
dragon.skill()
dragon.skill()
print(dragon.number)
'''
## class Mission: 아이템 구성안과 설계도를 활용하여, class와 객체를 생성해 보자
## 이때, 부모 클래스: Item // 자식 클래스: WearableItem, UsableItem 이다.


# [예외처리]
# : 프로그램 실행 중에 발생하는 예외를 미연에 방지하는 것.

## 예외처리가 필요한 이유 예시:  계산기 프로그램
'''
num1 = input("첫번짼 숫자를 입력해주세요.(숫자로 입력해주세요)>>")
num2 = input("두번째 숫자를 입력해주세요.(숫자로 입력해주세요)>>")
try:
    result = float(num1) + float(num2)
    print('결과: ', result)
except:
    print("오류가 발생하였습니다.")
'''
## 예외처리 연습문제: 환율 계산 문제
won = input("원화금액 입력해>>")
dollar = input(" 달러>>")
try:
    ratio = float(won)/float(dollar)
    print('환율: ', ratio)
except ValueError:
    print("문자열 예외가 발생했습니다. 숫자를 입력해주세요.")
except ZeroDivisionError:
    print("원은 0일 수 없습니다.")
finally:
    print("프로그램을 종료합니다.")
## 에러 발생시키기 연습문제


## 예외처리 Mission: 영어단어 공부하기 문제를 'while문 + 예외 처리'로 풀어보자


# [파일 입출력]
## 파일 입출력 연습문제1: 파일 쓰기(w: 새로쓰기 혹은 덮어쓰기)


## 파일 입출력 연습문제2: 파일 추가하기(a: 추가하기)


## 파일 입출력 연습문제3: 파일 읽기(r: 읽기)
## way1) readline 함수 사용(한 줄 씩 읽어오기)


## way2) readlines 함수 사용(모든 줄을 읽어와, 각 줄을 리스트의 요소로 반환)


## way3) read 함수 사용(문서 전체를 하나의 문자열로 가져오기)


# [이번 주 추가문제] - OX 퀴즈
## url: https://www.acmicpc.net/problem/8958
'''
import sys

T = int(sys.stdin.readline())

# 정오표 읽어오기 
errata = []
for i in range(T):
    temp = sys.stdin.readline()
    temp = temp[:-1]
    errata.append(temp)

# X를 기준으로 분할 후, 점수 계산
scores = []
for i in range(len(errata)):
    
    # <채울 code 내용>
    
    print(scores[i])
'''