# 중급반 8주차 정규수업(10:00~12:00)

# [Galaga 게임을 만들어보자]
from tkinter import *
import sys
import pygame

# class Sprite
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
        g.create_image(self.x, self.y, anchor=NW, image=self.img)

    # 스프라이트를 움직이는 메소드
    def move(self):
        self.x += self.dx
        self.y += self.dy

    # dx를 설정하는 설정자 메소드
    def setDx(self, dx):
        self.dx = dx

    # dy를 설정하는 설정자 메소드
    def setDy(self, dy):
        self.dy = dy

    # dx를 반환하는 접근자 메소드
    def getDx(self):
        return self.dx

    # dy를 반환하는 접근자 메소드
    def getDy(self):
        return self.dy

    # x를 반환하는 접근자 메소드
    def getX(self):
        return self.x

    # y를 반환하는 접근자 메소드
    def getY(self):
        return self.y

    # 다른 스프라이트와의 충돌 여부를 계산한다. 충돌이면 true를 반환한다.
    def checkCollision(self, other):
        p1x = self.x
        p1y = self.y
        p2x = self.x + self.getWidth()
        p2y = self.y + self.getHeight()

        p3x = other.x
        p3y = other.y
        p4x = other.x + other.getWidth()
        p4y = other.y + other.getHeight()

        overlapped = not( p4x < p1x or      # () 안의 조건식은 겹치지 않을 조건이다. 네모를 그리고 좌하단 꼭짓점을 (p1x,p1y)라고 하자.
            p3x > p2x or                    # p4x < p1x: self와 겹치지 않게 other이 좌측이 위치
            p2y < p3y or                    # p3x > p1x: self와 겹치지 않게 other이 우측에 위치
            p1y > p4y)
        return overlapped

    # 충돌 처리한다. Sprite class에서는 아무 기능이 없으나, 자식 클래스에 오버라이드 된다.
    def handleCollision(self,other):
        pass


# class StarShipSprite
# : 우주선(StarShip)을 나타내는 클래스
class StarShipSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dx = 0
        self.dy = 0

    # 우주선을 움직이는 메서드. (윈도우 경계를 넘으려고 할 경우, 움직이지 못하게 할 것)
    def move(self):
        if (((self.dx < 0) and (self.x <10)) or ((self.dx > 0) and (self.x > 725))):
            return
        if ((self.dy > 0) and (self.y > 525) or ((self.dy < 0) and (self.y < 10))):
            return
        super().move()
        self.dx = 0
        self.dy = 0

    # 충돌을 처리한다. 외계인 우주선과 충돌하면 게임이 종료되도록 한다.
    def handleCollision(self, other):
        if type(other) == AlienSprite:
            self.game.endGame()

# class AlienSprite
# : 외계인 우주선을 나타내 는 클래스
class AlienSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dx = -10

    # 외계인 우주선을 움직이는 메소드(윈도우의 경계에 도달하면 한 칸 아래로 이동한다.)
    def move(self):
        if (((self.dx < 0) and (self.x <10)) or ((self.dx > 0) and (self.x > 750))):
            self.dx = -self.dx
            self.y += 50
            if (self.y > 600):
                self.game.endGame()
        super().move()


# class ShotSprite
# : 포탄을 나타내는 클래스
class ShotSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dy = -20
        self.hit_sound = pygame.mixer.Sound(r'C:\python_deep\python_level_middle\Galaga_Game\sound\hit_sound.mp3')
        self.shot_sound = pygame.mixer.Sound(r'C:\python_deep\python_level_middle\Galaga_Game\sound\shot_sound.mp3')
        self.shot_sound.play()

    # 화면을 벗어나면 객체를 리스트에서 삭제한다.
    def move(self):
        super().move()
        if self.y < -50:
            self.game.removeSprite(self)

    # 충돌을 처리한다. 포탄과 외계인 우주선 객체를 모두 리스트에서 삭제한다.
    def handleCollision(self, other):
        if type(other) is AlienSprite:
            self.hit_sound.play()
            self.game.removeSprite(self)
            self.game.removeSprite(other)


# 갤러그 게임을 나타내는 클래스
class GalagaGame():
    # "이벤트" 관련 매서드들
    ## ↑ 화살표 키 이벤트 처리
    def keyUp(self, event):
        self.starship.setDy(-10)

    ## ↓ 화살표 키 이벤트 처리
    def keyDown(self, event):
        self.starship.setDy(+10)

    ## → 화살표 키 이벤트 처리
    def keyLeft(self, event):
        self.starship.setDx(-10)

    ## ← 화살표 키 이벤트 처리
    def keyRight(self, event):
        self.starship.setDx(+10)

    ## 스페이스 키 이벤트를 처리
    def keySpace(self, event):
        self.fire()

    ## ESC 키 이벤트를 처리
    def keyESC(self, event):
        self.master.destroy()

    # initSprites 메서드: 게임에 필요한 스프라이트를 생성
    def initSprites(self):
        self.starship = StarShipSprite(self, self.shipImage, 370, 520)
        self.sprites.append(self.starship)
        for y in range(0, 2):
            for x in range(0, 12):
                alien = AlienSprite(self, self.alienImage, 100+x*50, 50+y*30)
                self.sprites.append(alien)

    # __init__(): 생성자 메서드
    def __init__(self, master):
        self.master = master
        self.sprites = []
        self.canvas = Canvas(master, width=800, height=600)
        self.canvas.pack()
        # self.shotImage = PhotoImage(file=r"D:\My_file\Github_asdfrv20\Python_deep\python_1st_term\python_intermediate_1st term\Gallaga\image\fire.png")
        # self.shipImage = PhotoImage(file=r"D:\My_file\Github_asdfrv20\Python_deep\python_1st_term\python_intermediate_1st term\Gallaga\image\starship.png")
        # self.alienImage = PhotoImage(file=r"D:\My_file\Github_asdfrv20\Python_deep\python_1st_term\python_intermediate_1st term\Gallaga\image\alien.png")
        self.shotImage = PhotoImage(file="C:/python_deep/python_level_middle/Galaga_Game/image/fire.png")
        self.shipImage = PhotoImage(file="C:/python_deep/python_level_middle/Galaga_Game/image/starship.png")
        self.alienImage = PhotoImage(file="C:/python_deep/python_level_middle/Galaga_Game/image/alien.png")
        self.running = True
        self.initSprites()
        print(self.sprites)
        master.bind("<Up>", self.keyUp)
        master.bind("<Down>", self.keyDown)
        master.bind("<Left>", self.keyLeft)
        master.bind("<Right>", self.keyRight)
        master.bind("<space>", self.keySpace)
        master.bind("<Escape>", self.keyESC)
        master.bind("<Return>", self.startGame)
        self.shot_sound = pygame.mixer.Sound(r'C:\python_deep\python_level_middle\Galaga_Game\sound\shot_sound.mp3')
        self.start_sound = pygame.mixer.Sound(r'C:\python_deep\python_level_middle\Galaga_Game\sound\shot_sound.mp3')

    # startGame() 메서드: 게임시작 메서드(Enter키의 이벤트 핸들러)
    def startGame(self, event):
        self.sprites.clear()
        self.initSprites()
        self.start_sound.play()
        self.start_sound.play()

    # endGame() 메서드: 게임 종료(Game Over의 조건을 충족했을 때 실행되는 메서드)
    def endGame(self):
        self.running = False
        sys.exit()

    # removeSprite() 메서드: 스프라이트를 리스트에서 삭제
    def removeSprite(self, sprite):
        if(sprite in self.sprites):
            self.sprites.remove(sprite)
            del sprite

    # fire() 메서드: 포탄 발사
    def fire(self):
        shot = ShotSprite(self, self.shotImage, self.starship.getX()+28, self.starship.getY()-30)
        self.sprites.append(shot)

    # paint() 메서드: 화면 그리기
    def paint(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0, 0, 800, 600, fill="black")
        for sprite in self.sprites:
            sprite.draw(self.canvas)

    # gameLoop() 메서드: 게임 루프
    def gameLoop(self):
        # 1. 스프라이트들이 움직이도록 설정(move)
        for sprite in self.sprites:
            sprite.move()

        # 2. 스프라이트 리스트 안의 객체끼리의 충돌을 검사한다.(collision)
        for me in self.sprites:
            for other in self.sprites:
                if me != other:
                    if me.checkCollision(other):
                        me.handleCollision(other)
                        other.handleCollision(me)

        # 3. 배경그리기(paint // gameloop가 실행될 때마다 그려 마치 움직이는 것처럼 보이게 함.)
        self.paint()

        # 4. 게임 동작 여부를 확인하여 True일때, 10ms 간격으로 self.gameLoop를 실행시킨다.(gameLoop)
        if self.running:
            self.master.after(10, self.gameLoop)        # after 명령: 일정 시간이 지난 후에 특정 함수 또는 메서드를 실행시킨다.

# main문
if __name__ == "__main__":
    root = Tk()             # Tk() 객체 생성
    root.title("Galaga")
    pygame.init()

    g = GalagaGame(root)    # GalagaGame 객체 생성
    g.start_sound.play()
    g.gameLoop()            # gameLoop() 함수를 호출
    root.mainloop()