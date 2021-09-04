# python 중급반 1주차 정규수업(10:00~12:00) mission
'''
[수업을 시작하기 전에!]
1. 카카오톡 질문 단체톡방 ON!
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기
5. 수업시간 집중!!

[기초반 마지막 시간 복습]
1. .super() 명령과 클래스 변수
2. 예외처리
'''

# [예외처리 이어서...]
## 에러 발생시키기 연습문제
'''
string = input("문자열 입력>> ")
if string == "까마귀 날자":
    raise ValueError
else:
    print("배 떨어진다.")
'''
## 예외처리 Mission: 영어단어 공부하기 문제를 'while문 + 예외 처리'로 풀어보자
'''
word_list = ['hello', 'chicken', 'python']
i = 0
count =0
while True:
    try:
        word = input(word_list[i]+'\n')
    except:
        break
    if word == word_list[i]:
        count += 1
    i += 1

print("현재 문제개수: ", len(word_list))
print("맞힌 문제 개수: ", count)
print("틀린 문제 개수: ", len(word_list) - count)
'''
# [파일 입출력]
## 파일 입출력 연습문제1: 파일 쓰기(w: 새로쓰기 혹은 덮어쓰기)
'''
file = open('C:\python_deep\python_level_middle/text.txt' , 'w', encoding = 'utf-8')
for i in range (1,10):
    data = f'{i}번째 줄입니다\n'
    file.write(data)
file.close()
'''
## 파일 입출력 연습문제2: 파일 추가하기(a: 추가하기)
'''
file = open('C:\python_deep\python_level_middle/text.txt' , 'a', encoding = 'utf-8')
for i in range (11,21):
    data = f'{i}번째 줄입니다\n'
    file.write(data)
file.close()
'''
## 파일 입출력 연습문제3: 파일 읽기(r: 읽기)
## way1) readline 함수 사용(한 줄 씩 읽어오기)
'''
file = open('C:\python_deep\python_level_middle/text.txt' , 'r', encoding = 'utf-8')
while True:
    data = file.readline()
    print(data, end='')
    if data == '':
        break
file.close()
'''
## way2) readlines 함수 사용(모든 줄을 읽어와, 각 줄을 리스트의 요소로 반환)
'''
file = open('C:\python_deep\python_level_middle/text.txt' , 'r', encoding = 'utf-8')
datas = file.readlines()
for data in datas:
    print(data, end='')
    file.close()
'''
## way3) read 함수 사용(문서 전체를 하나의 문자열로 가져오기)
'''
file = open('C:\python_deep\python_level_middle/text.txt' , 'r', encoding = 'utf-8')
data = file.read()
print(data)
file.close
'''