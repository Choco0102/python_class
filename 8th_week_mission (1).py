# 8주차 정규수업(10:00~12:00) mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[7주차-2 복습]
1. 리스트 mission
2. 반복문 mission1,2: 구구단 출력하기
3. 반복문 mission3: 영단어 타자연습
'''

# 저번 시간에 못 다한 반복문 마지막 Mission
## 반복문 mission4: turtle을 활용하여 무지개 그리기 (이후 함수에도 연개할 예정이므로 반드시 수행)
### for 반복문 Mission2: turtle 모듈을 활용하여 무지개 만들기
'''
import turtle

# 변수 및 객체 선언
win = turtle.Screen()
t = turtle.Turtle('turtle')
t.shapesize(2)
rainbow_size = 500         # 무지개 크기(너비)
pen_size = 30              # 펜 굵기
rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']      # 활용할 색상 지정
t.speed(10)                # 거북이 속도 설정 

# 펜 초기 설정
t.pensize(pen_size)

# for 반복문 실행(무지개 그리기)
for i in range(0, 7):
    t.setheading(90)
    t.penup()
    t.setpos(0+30*i,0)
    t.pencolor(rainbow_color[i])
    t.pendown()
    t.circle(rainbow_size+30*i,180)
    i +=1

"""
# <Mission: 이 부분을 작성해 주세요>
"""
'''

# [함수]
##: 여러개의 명령어들을 묶어서 한꺼번에 처리할 수 있도록 만든 하나의 명령어 묶음에 이름을 붙인 것.
## 문법: def 함수이름(매개변수1, 매개변수2, ...):
##         명령어 블럭
##         return 반환값

## docstring: 함수에 대한 설명을 나타내는 문장

## 연습문제1: 입력X, 출력X인 함수
## >> 함수를 호출하면 별모양을 그리는 DrawStar_100()
'''
import turtle
# DrawStar_100 함수 정의해주기

win = turtle.Screen()
DrawStar_100()
win.mainloop()
'''
## 연습문제2: 입력O, 출력X인 함수
## >> 한 변의 길이를 입력하면, 그 한변의 길이를 가지는 별을 그리는 DrawStar()
'''
import turtle
# DrawStar() 함수 정의해주기 

win = turtle.Screen()
DrawStar(200)
win.mainloop()
'''
## 연습문제3: 입력X, 출력O인 함수
## >> 1~100까지 랜덤한 정수 1개를 반환하는 getRandomNum()
'''
import random
# getRandomNum() 함수 정의해주기

num = getRandomNum()
print(num)
'''
## 연습문제4: 입력O, 출력O인 함수
## >> a,b를 입력하면 두 수의 합을 반환하는 add()
'''
# add 함수 정의해주기 

X = add(100, 55)
print(X)
'''

## 함수 Mission: 앞서 반복문 Mission4에서 그린 무지개를 "함수"로 만들어보자
## 조건은 ppt 16p참고

# Mission: draw_rainbow() 함수 정의하기
def draw_rainbow(t, rainbow_size, pen_size, x, y):
    """
    입력한 t가 rainbow_size크기의 지름과 pen_size 두께의 색상띠를 가지는 무지개를 (x,y)에 그리는 함수
    :param t: 그림을 그릴 turtle 객체
    :param rainbow_size: 무지개의 지름
    :param pen_size: 무지개를 그릴 펜의 두께
    :param x: 무지개가 그려질 x좌표
    :param y: 무지개가 그려질 y좌표
    """
    # 설정(작성할 부분1)
    t.pensize(pen_size)
    rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']

    # 그리기(작성할 부분2)
    for i in range(0,7):
        t.setheading(90)
        t.penup()
        t.setpos(x + 30 * i, y)
        t.pencolor(rainbow_color[i])
        t.pendown()
        t.circle(rainbow_size + 30 * i, 180)
        i += 1

    return

import turtle

win = turtle.Screen()
win.screensize(1000,1000)
t = turtle.Turtle('turtle')
t.speed(0)

# 이제 draw_rainbow를 활용하여 무지개를 마음껏 그려보자(작성할 부분3)
draw_rainbow(t,50,30,0,0)
draw_rainbow(t,50,30,50,0)

turtle.mainloop()