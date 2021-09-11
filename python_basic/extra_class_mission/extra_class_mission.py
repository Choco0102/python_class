# 기말고사 보강수업 3차
# 보강수업 주제: Today is "CASINO DAY!!!"
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!
'''

# Problem1: 아스키코드를 활용한 슬롯머신 문제
# ASCII 코드의 33~39번(총 7개)의 특수문자를 활용하여 슬롯머신 만들기
# 자세한 내용은 ppt 내용 참고
'''
##수정 전
import random
a= 0
a = int(input("코인을 넣어주세요!(1.코인넣기//2.그만하기)>> "))
while True:
    #랜덤 숫자 발생
    if a == 1:
        random_n_1 = random.randint(33, 39)
        random_n_2 = random.randint(33, 39)
        random_n_3 = random.randint(33, 39)
        print("%c" %chr(random_n_1) | "%c" %chr(random_n_2) | "%c" %chr(random_n_3))
        #잭팟인 경우
        if random_n_1 == random_n_2 == random_n_3:
            print("Jackpot")
            break
        #잭팟이 아닌 경우
        else:
            a = int(input("코인을 넣어주세요!(1.코인넣기//2.그만하기)>> "))

    elif a == 2:
        print("게임을 종료합니다")
        break

    else:
        print("잘못 입력하셨습니다.")

##수정 후
import random

slot = [0, 0, 0]
print("[SLOT MACHINE GAME]")
while True:
    select = int(input("1.게임시작//2.나가기>> "))
    if select == 1:
        print("[GAME START]")
        while True:
            coin = int(input("1.코인넣기//2.메인화면>> "))
            if coin == 1:
                # slot에 랜덤 숫자 3개 발생 시키기
                for i in range(len(slot)):
                    slot[i] = random.randint(33, 39)
                # 화면 출력
                print("---------------------")
                print("| %c | %c | %c |" %(slot[0], slot[1], slot[2]))
                print("---------------------")
                # 결과 비교 및 출력
                if slot[0] == slot[1] == slot[2]:
                    print("JACKPOT!!!!")
                else:
                    print("아쉽습니다. 다음 기회에..!")
            elif coin == 2:
                print("게임을 종료합니다.\n")
                break
            else:
                print("잘못된 입력입니다. 다시 입력해주세요\n")

    elif select == 2:
        print("언제나 당신을 기다리겠습니다. 안녕~\n")
        break
    else:
        print("잘못된 입력입니다. 다시 입력하세요.\n")
'''
# Problem2: 동물레이싱
## case1: 우리가 배운 내용만을 사용한 코딩

'''
import turtle
import random

# 화면창 설정
win = turtle.Screen()
win.title('여기는 동물레이싱 경기장')
win.bgpic('별무리경기장.gif')

width = 1200
height = 800
offset = 50
win.setup(width, height)

# Turtle 객체의 이미지 추가
win.addshape('거북이.gif')
win.addshape('강아지.gif')
win.addshape('고양이.gif')

# 선수등록
Turtle = turtle.Turtle('거북이.gif')
puppy = turtle.Turtle('강아지.gif')
cat = turtle.Turtle('고양이.gif')

# 선수 출발선 이동
Turtle.penup()
Turtle.goto(-width/2+offset, -8/32*height)
puppy.penup()
puppy.goto(-width/2+offset, -10/32*height)
cat.penup()
cat.goto(-width/2+offset, -12/32*height)

# 달리기 시작!: 이 부분을 작성해 보자
# Hint1 - Turtle, puppy, cat은 결승선에 도착하기까지 달리도록 한다.
#         (결승선 x좌표:width/2-2*offset)
# Hint2 - x의 현재 좌표를 확인하는 방법: 변수(객체).xcor()
# Hint3 - 거북이는 랜덤하게 5~7의 거리를, 강아지는 3~9의 거리를, 고양이는 1~11의 거리를 이동한다.
#         (.forward()와 random.randint()를 활용하도록 하자)
# <code를 작성할 부분>
while(Turtle.xcor() < width/2 -2*offset):
    Turtle.forward(random.randint(5,7))
while(puppy.xcor() < width/2-2*offset):
    puppy.forward(random.randint(3,9))
while(cat.xcor() < width/2 - 2*offset):
    cat.forward(random.randint(1,11))

win.mainloop()
'''


'''
## case2: (위의 문제점을 해결해 보도록 하자) thread를 사용한 경우


##중요2
def turtleRun():
    while(Turtle.xcor() < width/2 - 2*offset):
        Turtle.forward(random.randint(5, 7))

def puppyRun():
    while (puppy.xcor() < width / 2 - 2 * offset):
        puppy.forward(random.randint(3, 9))

def catRun():
    while (cat.xcor() < width / 2 - 2 * offset):
        cat.forward(random.randint(1, 12))

import random
import turtle
import threading

# 화면창 설정
win = turtle.Screen()
win.title('여기는 동물레이싱 경기장')
win.bgpic('별무리경기장.gif')

width = 1200
height = 800
offset = 50
win.setup(width, height)

# Turtle 객체의 이미지 추가
win.addshape('거북이.gif')
win.addshape('강아지.gif')
win.addshape('고양이.gif')

# 선수등록
Turtle = turtle.Turtle('거북이.gif')
puppy = turtle.Turtle('강아지.gif')
cat = turtle.Turtle('고양이.gif')

# 선수 출발선 이동
Turtle.penup()
Turtle.goto(-width/2+offset, -8/32*height)
puppy.penup()
puppy.goto(-width/2+offset, -10/32*height)
cat.penup()
cat.goto(-width/2+offset, -12/32*height)

# 경기 시작!
# 1. thread 생성
# <code를 작성할 부분1>
t1 = threading.Thread(target = turtleRun)
t2 = threading.Thread(target = puppyRun)
t3 = threading.Thread(target = catRun)
# 2. 출발!!
# <code를 작성할 부분2>
t1.start(), t2.start(), t3.start()
win.mainloop()
'''

#####MISSION######

# Problem3: 이상한 블랙잭 문제
# url: https://www.acmicpc.net/problem/2798
'''
import sys
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split(' ')))

# 이 부분을 작성하는 것이 mission
# [조건1]: 3중 for문을 활용할 것.
# [조건2]: 리스트 슬라이싱 or range함수를 활용하면 좋음.
# >> 코딩 결과는 위 사이트로 이동하여 직접 넣어보도록 하자 
# <code를 작성할 부분>


print(sum_number)
'''