import pygame
import random
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
blue=(0,200,255)
dis.fill(grey)
game_over=False
game_close=False
x=300
y=200
x_change=0
y_change=0
clock=pygame.time.Clock()
game_close=False
font_style=pygame.font.SysFont("freesans",25)
lost_img=font_style.render("Press P to Play Again! Or Q to Quit!",True,red)

def our_snake(snake_block,snake_list):
  for x in snake_list:
    pygame.draw.rect(dis,teal,(x[0],x[1],snake_block,snake_block))
def game_loop():
    game_over=False
    game_close=False
    x=300
    y=200
    x_change=0
    y_change=0
    foodx=10*random.randint(0,59)
    foody=10*random.randint(0,39)
    snake_list=[]
    length_of_snake=1
    while(game_over==False):
        while(game_close==True):
            dis.fill(white)
            dis.blit(lost_img,[100,100])
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
        #pygame.draw.rect(dis,teal,(x,y,10,10))
        pygame.draw.rect(dis,blue, (foodx,foody, 10, 10))
        snake_head=[]
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list)>length_of_snake:
          del snake_list[0]
        our_snake(10,snake_list)
        if x==foodx and y==foody:
          length_of_snake+=1
          foodx=10*random.randint(0,59)
          foody=10*random.randint(0,39)
        pygame.display.update()
        clock.tick(40)

    pygame.quit()
game_loop()