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
x=300
y=200
x_change=0
y_change=0
while(game_over==False):
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
            
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                x_change=0
                y_change=-10
            elif event.key==pygame.K_DOWN:
                x_change=0
                y_change=10
            elif event.key==pygame.K_RIGHT:
                x_change=10
                y_change=0
            elif event.key==pygame.K_LEFT:
                x_change=-10
                y_change=0
                
    x=x+x_change
    y=y+y_change
    pygame.draw.rect(dis,teal,(x,y,10,10))
    pygame.display.update()
pygame.quit()