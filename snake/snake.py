import pygame
pygame.init()
#make variable
dis=pygame.display.set_mode((600,400))
pygame.display.set_caption("Snake by Eleah Burman")
pygame.display.update()
red=(128,0,0)
black=(0,0,0)
white=(255,255,255)
grey=(150,150,150)
orange=(255,150,20)
teal=(125,191,170)
dis.fill(grey)
game_over=False
game_close=False
x=300
y=200
x_change=0
y_change=0
clock=pygame.time.Clock()
def game_loop():
    game_over=False
    game_close=False
    x=300
    y=200
    x_change=0
    y_change=0
    while(game_over==False):
        while(game_close==True):
            dis.fill(white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over=True
                    game_close=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_p:
                        game_loop()
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

        if x>=600 or x<0 or y>=400 or y<0:
            game_close=True
        x=x+x_change
        y=y+y_change
        dis.fill(grey)
        pygame.draw.rect(dis,teal,(x,y,10,10))
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
game_loop()