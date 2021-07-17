# 6주차 mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[5주차 복습]
1. 연산자(2): 관계, 논리, 멤버십 연산자
2. 입력과 자료형 변환
3. 조건문 if
'''

# 5주차 잘못 업로드 되었던 주제: 논리연산자/ 멤버십 연산자
## 논리연산: and, or, not 연산, 결과는 True or False
## 논리연산 연습문제>>and, or, not 연산을 활용하여 결과를 예측(주석)하고 결과 학인하기
'''
print(4 <6 and 10 >= 10)       #TRUE
print("로아 썸머 이벤트 조아요" != "로아 썸머 이벤트 조아요" or "시공의 폭풍은 정말 최고야!" == "시공의 폭풍은 정말 최고야!")     #TRUE
print(not 5==5)     #FALSE
'''

## 멤버십 연산: 포함관계를 나타내는 연산(in, not in), 결과는 True or False
## 멤버십연산 연습문제>> 멤버십 연산자를 활용하여 "abc" 문자열 안에 b와 d가 포함되어 있는지 확인하기
'''
print("a" in "apple")       #TRUE     
print("d" in "banana")      #False       
print("L" not in "LOSTARK") #False
'''

# if 조건문 Mission(5주차 이어서)
## mission3>> 국어, 영어, 수학 점수를 입력받고 합계와 평균를 출력한 뒤.
## - 평균이 60점이 넘을 경우: "보충 대상자가 아닙니다. 즐거운 방학보내세요"
## - 퍙균이 60점이 넘지 않을 경우: "보충 대상자입니다. 당신의 방학은 이제 제껍니다 ㅎㅎ"
## 를 출력하는 프로그램을 만들어 보자
'''
#국,영,수 점수 입력받기
korean = int(input("국어 점수를 입력하시오>>"))
math = int(input("수학 점수를 입력하시오>>"))
english = int(input("영어 점수를 입력하시오>>"))
#총점,평균 계산
total = korean + english + math
average = total/3
#합계, 평균 출력
print("합계: %f" %total)
print("평균: %f" %average)

if average >= 60:
    print("보충대상자가 아닙니다.")
else:
    print("보충대상자입니다.")
'''
## mission4>> Up-down 게임 만들기
## random 함수를 활용하여 1~100까지의 숫자를 생성하고 up-down 게임 만들어보기

#수정 전
'''
import random

random_n = random.randint(1,100)

ans = int(input("맞춰봐>>"))

while ans != random_n:
    if ans == random_n:
       print("정답")
    elif ans > random_n:
        print("Down")
        ans = 0
    else:
        print("Up")
        ans = 0
    ans = int(input("맞춰봐>>"))
'''
#수정 후
'''
import random

random_n = random.randint(1,100)

while True:
    ans = int(input("맞춰봐>>"))
    if ans == random_n:
        print("정답")
        break
    elif ans > random_n:
        print("Down")
    else:
        print("Up")
'''
# [리스트 자료형]
## 리스트를 사용하는 이유?: 여러개의 데이터를 한 번에 저장하기 위해서
## 문법: 리스트이름 = [데이터, 데이터, ... ,데이터]
## 연습문제>> 내가 자주보는 유투버 이름 각자 1개씩 카톡방(혹은 채팅방)에 올리고
## 이 이름들을 list로 만들기
youtuber = ["10월 악토", "로빈하르트", "우왁굳", "T1 Faker", "논리왕전기", "나무늘보"]
print(youtuber)
## 리스트 제어하기1: 데이터 추가
## 방법: 리스트이름.append('추가할문자열')
## 연습문제>> 문자열에 수진썜이 좋아하는 유튜버 "승우아빠"를 추가해보자.
youtuber.append("승우아빠")
print(youtuber)
## 리스트 제어하기2: 인덱싱
## 방법: 리스트이름[인덱스 번호], 여기서 인덱스 번호는 0부터 시작에 주의!
## python의 순서를 가진 것들은 기본 0부터 시작!!
## 연습문제>> 만들어진 유투버 리스트에서 내가 가장 좋아하는 유튜버만 출력해보자
print(youtuber[3])

## 리스트 제어하기3: 데이터 수정하기
## 방법: 리스트이름[인덱스 번호] = '새로넣을 문자열'
## 연습문제>> 내가 가장 좋아하는 유투버의 이름을 2번째로 좋아하는 유튜버의 이름으로 바꿔보자
youtuber[3] = "T1"
print(youtuber)

## 리스트 제어하기4: 데이터 삭제하기
## 방법: del 리스트이름[삭제할인덱스번호]
## 연습문제>> 아쉽지만(ㅎㅎ) 선생님이 추가한 유투버를 리스트에서 삭제해보자.
del youtuber[6]
print(youtuber)

## 리스트 제어하기5: 리스트 슬라이싱
## 방법: 리스트이름[처음:끝+1]
## 연습문제>> 처음~3번쨰, 2번째~끝, 3번째~4번째에 위치한 유투버들만, 그리고(':'를 활용하여) 리스트 전체을 출력해보자.


## 리스트 제어하기6: 리스트 길이 구하기
## 방법: len(리스트이름)
## 연습문제>> 현재 리스트에 포함된 데이터의 개수를 구해보자


## 리스트 제어하기7: 리스트 정렬하기
## 방법1: 리스트이름.sort()  <- 오름차순 정렬
## 방법2: 리스트이름.sort(reverse=True)  <- 내림차순 정렬
## 연습문제>> 유투버들을 오름차순과 내림차순으로 정렬한 결과를 각각 출력해보자