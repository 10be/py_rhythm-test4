#main.py
import pygame, sys #외장함수 불러오기
from pygame.locals import *
from data import *

pygame.init()

size= (1280, 720) # 화면 크기 설정
FPS= 60 #프레임 수 변수

screen= pygame.display.set_mode(size) # size변수만큼의 크기의 창 생성 
pygame.display.set_caption('PY RHYTHM') # 게임 창의 이름 설정
fpsclock= pygame.time.Clock() # 프레임 조절을 위한 변수

n_line= sprite() # 클래스 불러오기(while문 밖에 할당)
n_line.insertImg('images/line.png') # 이미지 위치/이미지 파일명
n_line.setSize(512, 32) # 오브젝트 크기할당
n_line.x= 400 # 오브젝트 x좌표할당
n_line.y= 550 # 오브젝트 y좌표할당

n1_list=[] # 복제 된 오브젝트가 들어갈 리스트
n2_list=[] # 복제 된 오브젝트가 들어갈 리스트
n3_list=[] # 복제 된 오브젝트가 들어갈 리스트
n4_list=[] # 복제 된 오브젝트가 들어갈 리스트

music = pygame.mixer.Sound('music/Kitsune^2 - Rainbow Tylenol.mp3') # 음악파일
music.set_volume(0.3) # 음량조절

k1 = 0 # 타이밍을 위한 시간을 구할 변수
k2 = 0 
k3 = 0 
k4 = 0 
speed = 17 # 움직일 노트의 속도를 할당할 변수
tmpo = 28 # 템포를 정해줄 변수
ks = 0 # 음악이 나올 타이밍을 전해줄 변수

p1 = 0 # 키 홀드를 막기위한 변수
p2 = 0
p3 = 0
p4 = 0

line1 = sprite() # 왼쪽 사이트 바
line1.insertImg('images/line2.png')
line1.setSize(16, 800)
line1.x = 384
line1.y = 0

line2 = sprite() # 오른쪽 사이트 바
line2.insertImg('images/line2.png')
line2.setSize(16, 800)
line2.x = 912
line2.y = 0

f = open("txt/rainbow_tylenol.txt") # txt파일 열기
notes = f.read().splitlines() #해당 txt 파일을 리스트로 만들기
list_n = 0
notes[list_n] #list_n번째 칸의 
kn = -1 #노트가 내려올 타이밍

while True: # 무한히 반복
    screen.fill((0, 0, 0)) # 배경 색 지정

    keys = pygame.key.get_pressed() # 키 입력을 감지할 변수

    if kn % (tmpo/ 4) == 0:
        list_n += 1 # list_n을 kn % (tmpo/4)가 0일 때 마다 1을 더하기
    if list_n >= len(notes): # list_n이 notes리스트의 마지막 변수까지 왔다면
        list_n = 49 # 마지막 리스트 번호로고정
    if ks == 50: # ks가 50일 때
        music.play() # 음악 재생
    kn += 1
    ks += 1


    if k1 % (tmpo/ 4) == 0 and notes[list_n] == '1': # k와 tmpo ÷ 4를 나눌 때 나머지가 0인 경우, 그리고 notes[list_n] == 1인 경우에 실행
        n1 = sprite() # 클래스 불러오기 
        n1.insertImg('images/note.png') # 이미지 할당
        n1.setSize(128, 32) # 크기 할당
        n1.x = 400 # x값할당
        n1.y = -950 # y값할당
        n1.move = speed # 움직이는 속도값 할당
        n1_list.append(n1) # 리스트에 생성된 오브젝트 할당
    k1 += 1 # 1/60 초 마다 k에 1 추가
    d_list= [] # 지워질 오브젝트를 할당할 리스트    
    for i1 in range(len(n1_list)):
        m1= n1_list[i1] # m1을 n1_list에 있는 i1 번쨰 오브젝트로 정의
        m1.y += n1.move # m1을 아래로 움직이기
        if m1.y > 720: # m1의 y좌표가 720 일떄 
            d_list.append(i1)
        if keys[pygame.K_d] and p1 == 0: # d키를 눌렀을떄 p1이 0인 경우
            if m1.y >= 400 and m1.y < 450:
                d_list.append(i1)
            elif m1.y >= 450 and m1.y < 470:
                d_list.append(i1)
            elif m1.y >= 470 and m1.y < 580:
                d_list.append(i1)
            elif m1.y >= 580 and m1.y < 600:
                d_list.append(i1)
            elif m1.y >= 600:
                d_list.append(i1)
    d_list.reverse()
    for d in d_list:
        del n1_list[d] # n1_list에 있는 d번째 리스트에 있는 오브젝트 삭제

    if k2 % (tmpo/ 4) == 0 and notes[list_n] == '2': # k와 tmpo ÷ 4를 나눌 때 나머지가 0인 경우, 그리고 notes[list_n] == 2인 경우에 실행
        n2 = sprite() # 클래스 불러오기 
        n2.insertImg('images/note.png') # 이미지 할당
        n2.setSize(128, 32) # 크기 할당
        n2.x = 528 # x값할당
        n2.y = -950 # y값할당
        n2.move = speed # 움직이는 속도값 할당
        n2_list.append(n2) # 리스트에 생성된 오브젝트 할당
    k2 += 1 # 1/60 초 마다 k에 1 추가
    d_list= [] # 지워질 오브젝트를 할당할 리스트    
    for i2 in range(len(n2_list)):
        m2 = n2_list[i2] # m1을 n1_list에 있는 i1 번쨰 오브젝트로 정의
        m2.y += n2.move # m1을 아래로 움직이기
        if m2.y > 720: # m1의 y좌표가 720 일떄 
            d_list.append(i2)
        if keys[pygame.K_f] and p2 == 0: # f키를 눌렀을떄 p2이 0인 경우
            if m2.y >= 400 and m2.y < 450:
                d_list.append(i2)
            elif m2.y >= 450 and m2.y < 470:
                d_list.append(i2)
            elif m2.y >= 470 and m2.y < 580:
                d_list.append(i2)
            elif m2.y >= 580 and m2.y < 600:
                d_list.append(i2)
            elif m2.y >= 600:
                d_list.append(i2)
    d_list.reverse()
    for d in d_list:
        del n2_list[d] # n1_list에 있는 d번째 리스트에 있는 오브젝트 삭제

    if k3 % (tmpo/ 4) == 0 and notes[list_n] == '3': # k와 tmpo ÷ 4를 나눌 때 나머지가 0인 경우, 그리고 notes[list_n] == 3인 경우에 실행
        n3 = sprite() # 클래스 불러오기 
        n3.insertImg('images/note.png') # 이미지 할당
        n3.setSize(128, 32) # 크기 할당
        n3.x = 656 # x값할당
        n3.y = -950 # y값할당
        n3.move = speed # 움직이는 속도값 할당
        n3_list.append(n3) # 리스트에 생성된 오브젝트 할당
    k3 += 1 # 1/60 초 마다 k에 1 추가
    d_list= [] # 지워질 오브젝트를 할당할 리스트    
    for i3 in range(len(n3_list)):
        m3 = n3_list[i3] # m1을 n1_list에 있는 i1 번쨰 오브젝트로 정의
        m3.y += n3.move # m1을 아래로 움직이기
        if m3.y > 720: # m1의 y좌표가 720 일떄 
            d_list.append(i3)
        if keys[pygame.K_j] and p3 == 0: # j키를 눌렀을떄 p3이 0인 경우
            if m3.y >= 400 and m3.y < 450:
                d_list.append(i3)
            elif m3.y >= 450 and m3.y < 470:
                d_list.append(i3)
            elif m3.y >= 470 and m3.y < 580:
                d_list.append(i3)
            elif m3.y >= 580 and m3.y < 600:
                d_list.append(i3)
            elif m3.y >= 600:
                d_list.append(i3)
    d_list.reverse()
    for d in d_list:
        del n3_list[d] # n1_list에 있는 d번째 리스트에 있는 오브젝트 삭제

    if k4 % (tmpo/ 4) == 0 and notes[list_n] == '4': # k와 tmpo ÷ 4를 나눌 때 나머지가 0인 경우, 그리고 notes[list_n] == 4인 경우에 실행
        n4 = sprite() # 클래스 불러오기 
        n4.insertImg('images/note.png') # 이미지 할당
        n4.setSize(128, 32) # 크기 할당
        n4.x = 784 # x값할당
        n4.y = -950 # y값할당
        n4.move = speed # 움직이는 속도값 할당
        n4_list.append(n4) # 리스트에 생성된 오브젝트 할당
    k4 += 1 # 1/60 초 마다 k에 1 추가
    d_list= [] # 지워질 오브젝트를 할당할 리스트    
    for i4 in range(len(n4_list)):
        m4 = n4_list[i4] # m1을 n1_list에 있는 i1 번쨰 오브젝트로 정의
        m4.y += n4.move # m1을 아래로 움직이기
        if m4.y > 720: # m1의 y좌표가 720 일떄 
            d_list.append(i4)
        if keys[pygame.K_k] and p4 == 0: # k키를 눌렀을떄 p4이 0인 경우
            if m4.y >= 400 and m4.y < 450:
                d_list.append(i4)
            elif m4.y >= 450 and m4.y < 470:
                d_list.append(i4)
            elif m4.y >= 470 and m4.y < 580:
                d_list.append(i4)
            elif m4.y >= 580 and m4.y < 600:
                d_list.append(i4)
            elif m4.y >= 600:
                d_list.append(i4)
    d_list.reverse()
    for d in d_list:
        del n4_list[d] # n1_list에 있는 d번째 리스트에 있는 오브젝트 삭제

    if keys[pygame.K_d]: # 해당 키를 눌렀는지 감지
        p1 = 1
    else:
        p1 = 0

    if keys[pygame.K_f]: # 해당 키를 눌렀는지 감지
        p2 = 1
    else:
        p2 = 0

    if keys[pygame.K_j]: # 해당 키를 눌렀는지 감지
        p3 = 1
    else:
        p3 = 0

    if keys[pygame.K_k]: # 해당 키를 눌렀는지 감지
        p4 = 1
    else:
        p4 = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for m1 in n1_list:
        m1.show()

    for m2 in n2_list:
        m2.show()

    for m3 in n3_list:
        m3.show()

    for m4 in n4_list:
        m4.show()
    
    n_line.show()
    line1.show()
    line2.show()

    pygame.display.update() # 게임 창 유지
    fpsclock.tick(FPS) # FPS 변수 만큼의 프레임으로 지정