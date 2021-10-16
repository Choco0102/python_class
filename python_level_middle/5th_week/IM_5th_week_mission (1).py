# python 중급반 5주차 정규수업(10:00~12:00) mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[중급반 5주차 복습]
1. Tkinter의 여러가지 위젯들(2): Canvas, .bind()
2. 마우스르 활용하여 그림 그리기
3. Gallaga 만들기
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
        self.img = image  # 스프라이트가 가지고 있는 이미지
        self.x = x  # 현재 위치의 x좌표
        self.y = y  # 현재 위치의 y좌표
        self.dx = 0  # 단위시간에 움직이는 x방향 거리
        self.dy = 0  # 단위시간에 움직이는 y방향 거리

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
        overlapped = not (< 조건1 > or  # () 안의 조건식은 겹치지 않을 조건이다. 네모를 그리고 좌상단 꼭짓점을 (p1x,p1y)라고 하자.
                          < 조건2 > or  # self와 겹치지 않게 other이 좌측이 위치
                          < 조건3 > or  # self와 겹치지 않게 other이 우측에 위치
                          < 조건4 >)
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

# 갤러그 게임을 나타내는 클래스
'''
class GalagaGame():
    # "이벤트" 관련 매서드들
    ## ↑ 화살표 키 이벤트 처리
    def keyUp(self, event):
        # startship의 dy값 -10으로 설정

    ## ↓ 화살표 키 이벤트 처리
    def keyDown(self, event):
        # startship의 dy값 +10으로 설정

    ## ← 화살표 키 이벤트 처리
    def keyLeft(self, event):
        # startship의 dx값 -10으로 설정

    ## → 화살표 키 이벤트 처리
    def keyRight(self, event):
        # startship의 dx값 +10으로 설정

    ## 스페이스 키 이벤트를 처리
    def keySpace(self, event):
        # 포탄발사 메서드 (self.fire) 호출

    ## ESC 키 이벤트를 처리
    def keyESC(self, event):
        # Tk() 화면이 꺼지도록 설정(.destroy() 활용)

    # initSprites 메서드: 게임에 필요한 스프라이트를 생성
    def initSprites(self):
        # self.startship 객채 생성
        # self.sprites 리스트에 starship 추가

        # 에어리언 추가 (12x2 만큼 외계인 객체 생성)



    # __init__(): 생성자 메서드
    def __init__(self, master):
        # 객체 생성




        # 이미지 생성



        # 게임실행 여부 & sprite 초기화


        # 이벤트 처리(7가지 이벤트 처리)








    # startGame() 메서드: 게임시작 메서드(Enter키의 이벤트 핸들러)
    def startGame(self, event):
        # sprites 객체 전체 삭제
        # sprites 객체 초기화

    # endGame() 메서드: 게임 종료(Game Over의 조건을 충족했을 때 실행되는 메서드)
    def endGame(self):
        # 게임 실행여부 "False"로 설정
        # 프로그램 종료

    # removeSprite() 메서드: 스프라이트를 리스트에서 삭제
    def removeSprite(self, sprite):
        # 입력된 sprite가 self.sprites 리스트에 있다면,
            # self.sprites에서 sprite 제거
            # sprite 제거
    
    # fire() 메서드: 포탄 발사
    def fire(self):
        # 포탄 객체 shot 생성
        # sprites 객체에 추가하기

    # paint() 메서드: 화면 그리기
    def paint(self):
        # 캔버스 내용을 전체 지우기
        # 검은 화면 생성(Canvas 객체_
        # 반복문을 활용하여 sprites의 객체들 그리기
            # .draw 명령 실행

    # gameLoop() 메서드: 게임 루프
    def gameLoop(self):
        # 1. 스프라이트들이 움직이도록 설정(move)



        # 2. 스프라이트 리스트 안의 객체끼리의 충돌을 검사한다.(collision)








        # 3. 배경그리기(paint // gameloop가 실행될 때마다 그려 마치 움직이는 것처럼 보이게 함.)


        # 4. 게임 동작 여부를 확인하여 True일때, 10ms 간격으로 self.gameLoop를 실행시킨다.(gameLoop)
        # 만약, 게임 실행여부가 True라면
            # gameLoop를 10ms 후에 실행 (※ after 명령: 일정 시간이 지난 후에 특정 함수 또는 메서드를 실행시킨다.)


if __name__ == "__main__":
    # Tk() 객체 생성
    # 제목 설정
    # GalagaGame 객체 생성
    # gameLoop() 함수를 호출
    # mainloop()
'''
