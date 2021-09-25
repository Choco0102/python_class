# python 중급반 4주차 정규수업(10:00~12:00) mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[기초반 마지막 시간 복습]
1. Tkinter란?
2. Tkinter 시작하기
3. Tkinter의 여러가지 위젯들: Label, PhotoImage, Button, Text
'''

# [Tkinter 이어서...]
## Tkinter 위젯: Canvas() - Canvas 생성하기 & 여러가지 도형 그리기
'''
from tkinter import *
win = Tk()
win.title("캔버스 도형 그리기 연습문제")

c = Canvas(win, width=600, height=400)
c.pack()

c.create_oval(28, 18, 48, 38, width=2, outline="black", fill="yellow")
c.create_line(0, 0, 68, 48, width=9, fill="orange")
c.create_rectangle(50, 150, 150, 300, width=4, outline="red", fill="orange")

win.mainloop()
'''
## Tkinter 위젯: Canvas() - Canvas로 이미지 생성하기(create_image())
'''
from tkinter import *
win = Tk()
win.title("켄버스 이미지 생성 연습문제")

c = Canvas(win, width=600, height=400)
c.pack()
img = PhotoImage(file="C:/python_deep/python_level_middle/3rd_week/img.png")
c.create_image(0, 0, anchor=NW, image=img)
c.pack()

win.mainloop()
'''
# Tkinter 메서드: .bind() - 마우스로 그림그리기
## 참고 url - https://076923.github.io/posts/Python-tkinter-23/
'''
from tkinter import *

def drawDot(event):
    x1, y1 = (event.x-1),(event.y-1)
    x2, y2 = (event.x+1),(event.y+1)
    c.create_oval(x1, y1, x2, y2, fill="orange")

win = Tk()
win.title("드래그로 그림 그리기")

lb = Label(win, text="마우스를 드래그하면 점들이 그려집니다")
lb.pack()

c = Canvas(win, width=600, height=400)
c.bind("<B1-Motion>", drawDot)
c.pack()

win.mainloop()
'''
## class로 프레임 감싸기 - 예시
'''
from tkinter import *

class Application:
    def __init__(self, parent):
        h_btn = Button(parent, text="클릭", command=self.hello)
        h_btn.pack(side="left")
        q_btn = Button(parent, text="Quit", command=parent.quit)
        q_btn.pack(side="left")

    def hello(self):
        print("Hello world! :D")

root = Tk()
app = Application(root)
root.mainloop()
'''

# [Gallaga]
## 모듈 불러오기: tkinter, sys

# <class Sprite>
# : 게임의 스프라이트를 나타내는 클래스로 공통적으로 사용되는 변수와 메소드를 가지고 있다.
## 'sprite'의 의미
## 1) (장난을 좋아하는) 요정, 도깨비
## 2) (컴퓨터 그래픽스) 영상 속에 작은 2차원 비트맥이나 애니메이션을 합성하는 기술
class Sprite:
    def __init__(self, image, x, y):
        self.img = image    # 스프라이트가 가지고 있는 이미지
        self.x = x          # 현재 위치의 x좌표
        self.y = y          # 현재 위치의 y좌표
        self.dx = 0         # 단위시간에 움직이는 x방향 거리
        self.dy = 0         # 단위시간에 움직이는 y방향 거리

    # 스프라이트의 가로 길이 반환
    def getWidth(self):
        return self.img.width()

    # 스프라이트의 세로 길이 반환
    def getHeight(self):
        return self.img.height()

    # 스프라이트를 화면에 그리기
    def draw(self, g):
        g.create_image(self.x, self.y, anchor=NW, image=self.img())     #g는 canvas 객체

    # 스프라이트를 움직이는 메소드
    def move(self):
        # dx
        # dy

    # dx를 설정하는 설정자 메소드
    def setDx(self, dx):
        # x 좌표 설정

    # dy를 설정하는 설정자 메소드
    def setDy(self, dy):
        # y 좌표 설정

    # dx를 반환하는 접근자 메소드
    def getDx(self):
        # dx 반환

    # dy를 반환하는 접근자 메소드
    def getDy(self):
        # dy 반환

    # x를 반환하는 접근자 메소드
    def getX(self):
        # x 좌표 반환

    # y를 반환하는 접근자 메소드
    def getY(self):
        # y 좌표 반환

    # 다른 스프라이트와의 충돌 여부를 계산한다. 충돌이면 true를 반환한다.
    def checkCollision(self, other):
        ## p1(왼쪽 상단 꼭짓점), p2(오른쪽 하단 꼭짓점)
        p1x =
        p1y =
        p2x =
        p2y =

        ## p3(other의 왼쪽 상단 꼭짓점), p4(other의 오른쪽 상단 꼭짓점)
        p3x =
        p3y =
        p4x =
        p4y =

        ## overlapped: 충돌 여부 검사: 충돌시 True 반환
        overlapped = not ( <조건1> or  # () 안의 조건식은 겹치지 않을 조건이다. 네모를 그리고 좌상단 꼭짓점을 (p1x,p1y)라고 하자.
                           <조건2> or  # self와 겹치지 않게 other이 좌측이 위치
                           <조건3> or  # self와 겹치지 않게 other이 우측에 위치
                           <조건4>)
        return overlapped

    # 충돌 처리한다. Sprite class에서는 아무 기능이 없으나, 자식 클래스에 오버라이드 된다.
    def handleCollision(self, other):
        pass


'''
# <class StarShipSprite>
# : 우주선(StarShip)을 나타내는 클래스
class StarShipSprite():
    def __init__(self, , , , ):
        # 상속
        # game
        # dx 초기화
        # dy 초기화

    # 우주선을 움직이는 메서드. (윈도우 경계를 넘으려고 할 경우, 움직이지 못하게 할 것)
    def move(self):
        # 윈도우 경계를 넘지 못하도록 설정
        if (<조건1>):
            return
        if (<조건2>):
            return
        # 상속
        # dx 설정
        # dy 설정

    # 충돌을 처리한다. 외계인 우주선과 충돌하면 게임이 종료되도록 한다.
    def handleCollision(self, other):
        # 충돌 조건(if ... is ...: 를 활용할 것.)
        
'''

'''
# class AlienSprite
# : 외계인 우주선을 나타내는 클래스
class AlienSprite():
    def __init__(self, , , , ):
        # 상속
        # game
        # dx 설정

    # 외계인 우주선을 움직이는 메소드(윈도우의 경계에 도달하면 한 칸 아래로 이동한다.)
    def move(self):
        if (<조건입력>):
            # dx 변경
            # y 변경
            # y>600일 경우, GameOver
                
        # move 상속

'''
'''
# class ShotSprite
# : 포탄을 나타내는 클래스
class ShotSprite():
    def __init__(self, , , , ):
        # 상속
        # game
        # dy 초기화

    # 화면을 벗어나면 객체를 리스트에서 삭제한다.
    def move(self):
        # move 상속
        # 포탄이 화면을 벗어날 경우(y<-50) Sprite 삭제(game.removeSprite)


    # 충돌을 처리한다. 포탄과 외계인 우주선 객체를 모두 리스트에서 삭제한다.
    def handleCollision(self, other):
        # other의 자료형이 AlienSprite일 때, 둘다 삭제할 것(removeSprite())
'''
