#data.py
import pygame
size = (1280, 720) # 창 크기
screen = pygame.display.set_mode(size) # 빈 창 크기 지정 변수
class sprite: 
    def __init__(self): # 클래스 기본 함수
        self.x= 0 # x좌표 할당을 위한 변수
        self.y= 0 # y좌표 할당을 위한 변수 
        self.move= 0 # 움직임 할당을 위한 변수
    def insertImg(self, addr): # 이미지 파일 할당을 위한 함수
        if addr[-3:] == 'png': # 파일 형식이 png일 떄
            self.obj= pygame.image.load(addr).convert_alpha()
        else: # 그 외의 경우 일 떄
            self.obj= pygame.image.load(addr)
    def setSize(self, oX, oY): # 이미지 크기 할당을 위한 함수
        self.obj= pygame.transform.scale(self.obj, (oX, oY))
        self.oX, self.oY= self.obj.get_size()
    def show(self): # 오브젝트 생성 위한 함수
        screen.blit(self.obj, (self.x, self.y))
