# 7주차 보강1차 mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!
'''

# Problem1: turtle과 반복문을 활용하여 별모양 그리기
# 이제는 for문으로 그릴 수 있다!
## [Hint에 없는 필요 명령어]
## t.forward(): ()안의 거리만큼 전진
## t.right(): ()안의 각도만큼 현재 각도에서 오른쪽으로 회전
## t.left(): ()안의 각도만큼 현재 각도에서 왼쪽으로 회전
'''
import turtle

win = turtle.Screen()
win.setup(500,500)

for i in range(5):
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.left(72)

turtle.mainloop()
'''
# Problem2: factorial 계산하기
# ※ factorial이란?: 1에서 시작하여 "어떤 범위에 있는 모든 정수를 곱하는 것"
'''
##수정 전
answer = 1
n = int(input("숫자를 입력하시오>> "))
for i in range(n):
    answer = answer * n
    n = n-1

print(answer)


##수정 후
num = 1
num = int(input("숫자를 입력하시오>> "))
for i in range(1, num):
    num = num + i

print(num)
'''

# Problem3: 유클리드 알고리즘으로 최대공약수 구하기(GCD: Greatest Common Divisor)
## [유클리드의 GCD 알고리즘] - while문 사용하기
## 1. 두 수 가운데 큰 수를 x, 작은 수를 y라고 한다.
## 2. y가 0이면 최대 공약수는 x와 같고 알고리즘을 종료한다.
## 3. r <- x % y
## 4. x <- y
## 5. y <- r
'''
x = int(input("숫자를 입력하시오>> "))
y = int(input("숫자를 입력하시오>> "))
if x<y:
    x,y = y,x

while y != 0:
    if y == 0:
        break
    r = x % y
    x = y
    y = r
print("최대공약수는 %d입니다." %x)
'''
'''
# Problem4: 아스키코드를 활용한 슬롯머신 문제
# ASCII 코드의 33~39번(총 7개)의 특수문자를 활용하여 슬롯머신 만들기
# 문제내용은 ppt 참고

import random

a = int(input("코인을 넣어주세요!(1.코인넣기//2.그만하기)>> "))
if a == 1:
    random_n = random.randint(33, 39)


elif a == 2:
    print("게임을 종료합니다")

else:
    print("잘못 입력하셨습니다.")

'''
# Problem5: 달팽이 문제(for문으로 풀면 안풀리는 문제)
# (참고사이트: https://www.acmicpc.net/problem/2869)
# 시간측정 방법: import time // start = time.time() // print("time: ", time.time()-start)
# [조건]
# 조건1: 입력1>> 2 1 5 [결과: 4] // 입력2>> 5 1 6 [결과: 2] // 입력3>> 2 1 10000000 [결과: 9999901]
# 조건2: 위 조건1의 모든 입력에 대한 수행시간이 1초 이내에 완료
# Hint1: .split(' ')
# Hint2: 필요 하다면, import math // .ceil() 사용하기
import time
import math

temp = input('')

start = time.time()
temp = temp.split(' ')

for i in range(3):
    temp[i] = int(temp[i])
A = temp[0]
B = temp[1]
V = temp[2]


# 달팽이 문제 알고리즘 작성하기
##수정 전 ---> 틀린 이유: '4 1 14'로 생각하셈
t = math.floor((V - A) /(A - B)) + 1
print("달팽이는 %d만큼 걸립니다." %t)

##수정 후
t = math.ceil((V - A) /(A - B)) + 1
print("달팽이는 %d만큼 걸립니다." %t)

print('time: ', time.time()-start)



