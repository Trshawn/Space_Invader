import pygame
import math
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION

from pygame.mixer import pause
from Background.background_sound import *
from Enemy.enemies import *
from Plane.player import *
from Bullet.bullets import *


#初始化界面
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("space invader")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)


#导入包中的background and music
bgImg =pygame.image.load('./Background/bg.png')
#bgImg=background_sound()

# bgm
sound=pygame.mixer.music.load('./Background/bg.wav')
pygame.mixer.music.play(-1)
#添加射中音效
bao_sound=pygame.mixer.Sound('./Sound Effect/exp.wav')

#导入包中的player并且设置位置
player=Planeplayer(400,500)

number_of_enemies=6
enemies=[]

#添加敌人
for i in range(number_of_enemies):
    #导入Enemy包命名为Monster并apped到list中
    Monster=Enemy()
    enemies.append(Monster)


def show_enemy():
    global is_over
    for e in enemies:
        screen.blit(e.enemyImg,(e.x,e.y))
        e.x+=e.step
        if(e.x>736 or e.x<0):
            e.step*=-1
            e.y+=40
        if e.y>450:
            is_over=True
            enemies.clear()

        


bullets=[]

#pause game
pause = False
pause_nor_image = pygame.image.load("pause_nor.png").convert_alpha()
pause_pressed_image = pygame.image.load("pause_pressed.png").convert_alpha()
resume_nor_image = pygame.image.load("resume_nor.png").convert_alpha()
resume_pressed_image = pygame.image.load("resume_pressed.png").convert_alpha()

pause_rect = pause_pressed_image.get_rect()
pause_rect.left, pause_rect.top = 700,10
pause_image = pause_pressed_image

# pause music
pause2 = False

pause2_rect = pause_nor_image.get_rect()
pause2_rect.left, pause2_rect.top = 700,550
pause2_image = pause_pressed_image

def show_bullets():
    global screen
    for b in bullets:
        screen.blit(b.bulletImg, (b.x, b.y))
        hit(b)
        b.y -= b.step
        if b.y < 0:
            bullets.remove(b)

def hit(bullet):
    global score
    for e in enemies:
        if distance(bullet.x, bullet.y, e.x, e.y) < 30:
            bao_sound.play()
            score += 1
            bullets.remove(bullet)
            e.reset()
            break


font=pygame.font.Font('freesansbold.ttf',32)
is_over=False
score=0


def show_score():
    text=f"Score:{score}"
    score_render=font.render(text,True,(255,255,255))
    screen.blit(score_render,(10,10))


over_font=pygame.font.Font('freesansbold.ttf',64)


def check_is_over():
    if is_over:
        text="Game Over"
        render=over_font.render(text,True,(255,255,0))
        screen.blit(render,(200,250))


def distance(bx,by,ex,ey):
    a=bx-ex
    b=by-ey
    return math.sqrt(a**2+b**2)


if __name__ == '__main__':

    running = True
    while running:
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False

            elif event.type == MOUSEBUTTONDOWN:
                # button==1 represents press mouse_left_button
                # collidepoint method of rect: detect if mouse cursor is in the rect
                if event.button==1 and pause_rect.collidepoint(event.pos):
                    pause = not pause
                if pause:
                    pause_image = resume_pressed_image
                else:
                    pause_image = pause_pressed_image

                if event.button==1 and pause2_rect.collidepoint(event.pos):
                    pause2 = not pause2
                if pause2:
                    pause2_image = resume_pressed_image
                    pygame.mixer.music.stop()
                else:
                    pause2_image = pause_pressed_image
                    pygame.mixer.music.play(-1)
                    

        if not pause:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    player.horizontal=5
                elif event.key==pygame.K_LEFT:
                    player.horizontal=-5
                elif event.key == pygame.K_UP:
                    player.vertical = -5
                elif event.key == pygame.K_DOWN:
                    player.vertical = 5
                #无法发射子弹 且暂停时只有player不动
                if event.key==pygame.K_SPACE:
                    print("发射子弹...")
                    bullets.append(Bullet(player.x, player.y))


            elif event.type==pygame.KEYUP:
                player.horizontal = 0
                player.vertical = 0



        screen.blit(bgImg,(0,0))
        show_score()
        screen.blit(pause_image, pause_rect)
        screen.blit(pause2_image,pause2_rect)
        show_bullets()
        screen.blit(player.img,(player.x,player.y))
        player.move_player()
        show_enemy()
        check_is_over()
        pygame.display.update()
