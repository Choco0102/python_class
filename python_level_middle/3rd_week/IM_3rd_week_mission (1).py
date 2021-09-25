# python 중급반 3주차 정규수업(10:00~12:00) mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[기초반 마지막 시간 복습]
1. 이벤트 처리란?
2. turtle모듈을 활용한 마우스, 키보드 이벤트 처리
'''


# [Tkinter]
# ※ Tkinter란? - Python에서 제공하는 GUI생성을 위한 표준 Python 인터페이스

## Tkinter 시작하기
'''
from tkinter import *

window = Tk()
window.mainloop()
'''
## Tkinter 시작하기: Window 창 설정하기
'''
from tkinter import *

window = Tk()
window.title("testing")
window.geometry("500x700+0+0")
window.resizable(True, True)

window.mainloop()
'''
## Tkinter 위젯: Label() - 연습문제1
## 참고 url: https://076923.github.io/posts/Python-tkinter-2/
## Hello World를 포함한 GUI창 띄우기
## Hello World를 포함한 GUI창 띄우기 + (koverwatch,50)으로 font 바꿔보기
'''
from tkinter import *           #  *은 all의 의미
win = Tk()
win.title("label 연습문제 1")
lb = Label(win, text="Hello World!", font=("koverwatch", 50))
lb.pack()
win.mainloop()
'''

## Tkinter 위젯 배치 관리자 연습문제: grid, pack, palce 하나씩 수행해보기
'''
from tkinter import *

win = Tk()
win.title("배치관리자 연습문제")
win.geometry("1000x600+200+120")
win.resizable(True, True)


lb1 = Label(win, text='Life is too short', font=('koverwatch', 20))
lb2 = Label(win, text='You need Python', font=('굴림', 10))
#lb1.grid(row=0, column=0)     # Grid
#lb2.grid(row=2, column=7)
#lb1.pack()      # Pack
#lb2.pack()
#lb1.place(x=100, y=200)     # Place
#lb2.place(x=200, y=330)

win.mainloop()
'''

## Tkinter 위젯: PhotoImage()
## 저장된 이미지를 GUI화면에 출력해보자.
'''
from tkinter import *

win = Tk()
win.title("안 팔아요...")

img = PhotoImage(file="C:/python_deep/python_level_middle/3rd_week/img.png")
lb = Label(win, image = img)
lb.pack()

win.mainloop(
'''
## Tkinter 위젯: Button() - 버튼 생성하기
## 참고 url: https://076923.github.io/posts/Python-tkinter-3/
'''
from tkinter import *

win = Tk()
win.title("버튼 생성하기 연습문제")

btn1 = Button(win, text="버튼 1")
btn2 = Button(win, text="버튼 2")

btn1.pack(side = "left", padx = 20)
btn2.pack(side = "left")

win.mainloop()
'''
# Tkinter 위젯: Button() - 버튼 이벤트 처리하기
## Button을 누르면 설정한 이벤트(callback 함수)가 실행되도록 만들어보자.
''''
from tkinter import *

def callback():
    if btn ['text'] == "클릭":
        btn ['text'] = "버튼이 클릭되었습니다."
    else:
        btn['text'] = "클릭"

win = Tk()
win.title("이벤트 처리 연습문제")

lb = Label(win, text="버튼을 클릭하세요")
lb.pack()
btn = Button(win, text="클릭", command = callback)
btn.pack()

win.mainloop()
'''
## Tkinter 위젯: Text() - 연습문제: Text 위젯 생성하기

from tkinter import *

win = Tk()
win.title("text 위젯 연습문제")

T = Text(win, width = 80, height = 10)
T.pack()
T.insert(1.0, "텍스트 위젯 연습문제 \n Hello world! \n 지금 생각나는 문장을 입력해봅시다 :D")

win.mainloop()

## Tkinter 위젯: Canvas() - Canvas 생성하기 & 여러가지 도형 그리기


## Tkinter 위젯: Canvas() - Canvas로 이미지 생성하기(create_image())


# Tkinter 메서드: .bind() - 마우스로 그림그리기
## 참고 url - https://076923.github.io/posts/Python-tkinter-23/


## class로 프레임 감싸기 - 예시
''''
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