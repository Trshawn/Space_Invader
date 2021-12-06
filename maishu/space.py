import pygame
import math

from pygame.constants import K_LEFT, K_UP
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
bgImg=background_sound()

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
        if distance(e.x,e.y,player.x,player.y)<30:
            bao_sound.play()
            is_over=True
            enemies.clear()


bullets=[]

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

flag_RIGHT=0
flag_DOWN=0
flag_LEFT=0
flag_UP=0

if __name__ == '__main__':

    running = True
    while running:
        screen.blit(bgImg.img,(0,0))
        show_score()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    player.horizontal=5
                    flag_RIGHT=1
                if event.key==pygame.K_LEFT:
                    player.horizontal=-5
                    flag_LEFT=1
                if event.key == pygame.K_UP:
                    player.vertical = -5
                    flag_UP=1
                if event.key == pygame.K_DOWN:
                    player.vertical = 5
                    flag_DOWN=1
                if event.key==pygame.K_SPACE:
                    print("发射子弹...")
                    bullets.append(Bullet(player.x, player.y))


            elif event.type==pygame.KEYUP:
                if event.key!=pygame.K_SPACE:
                    if event.key==pygame.K_RIGHT:
                        flag_RIGHT=0
                        if flag_LEFT==0:
                            player.horizontal = 0
                        else:
                            player.horizontal = -5
                    if event.key==pygame.K_LEFT:
                        flag_LEFT=0
                        if flag_RIGHT==0:
                            player.horizontal = 0
                        else:
                            player.horizontal = 5
                    if event.key==pygame.K_DOWN:
                        flag_DOWN=0
                        if flag_UP==0:
                            player.vertical = 0
                        else:
                            player.vertical = 5
                    if event.key==pygame.K_UP:
                        flag_UP=0
                        if flag_DOWN==0:
                            player.vertical=0
                        else:
                            player.vertical = -5
        
        show_bullets()
        screen.blit(player.img,(player.x,player.y))

        player.move_player()
        show_enemy()
        check_is_over()
        pygame.display.update()
