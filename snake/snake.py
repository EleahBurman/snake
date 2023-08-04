import pygame
pygame.init()
#make variable
dis=pygame.display.set_mode((600,400))
pygame.display.update()
red=(128,0,0)
black=(0,0,0)
white=(255,255,255)
pygame.display.set_caption("Snake by Eleah Burman")
game_over=False
while(game_over==False):
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis,red,(300,200,10,10))
    pygame.display.update()
pygame.quit()