import pygame
pygame.init()
#make variable
dis=pygame.display.set_mode((600,400))
pygame.display.update()
game_over=False
while(game_over==False):
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
pygame.quit()