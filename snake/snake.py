#importing library
import pygame

#initializing pygame
pygame.init()

#make variable
dis=pygame.display.set_mode((600,400))
pygame.display.set_caption("Snake by Eleah Burman")
pygame.display.update()
#initializing color
red=(128,0,0)
black=(0,0,0)
white=(255,255,255)
grey=(150,150,150)
orange=(255,150,20)
teal=(135,191,170)
dis.fill(grey)
game_over=False
while(game_over==False):
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis,teal,(580,380,10,10))
    pygame.display.update()
pygame.quit()