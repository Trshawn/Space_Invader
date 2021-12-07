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

number_of_enemies=2
enemies=[]

score=0
for i in range(number_of_enemies):
    Monster = Enemy()
    enemies.append(Monster)  

# 游戏难度
def game_stage():
    global score
    global number_of_enemies
    if score == 20 and len(enemies) == 2:
        enemies.clear()
        for i in range(number_of_enemies):
            Monster = Enemy()
            number_of_enemies = 4
            enemies.append(Monster)
        return
    if score == 40 and len(enemies) == 4:
        enemies.clear()
        for i in range(number_of_enemies):
            Monster = Enemy()
            number_of_enemies = 6
            enemies.append(Monster)
        return


# 敌人显示
type_move = random.randint(1,3)
def show_enemy():
    global is_over
    type_move = random.randint(1,3)
    for e in enemies:
        screen.blit(e.enemyImg,(e.x,e.y))
        # 敌人随机路线
        ## 直线移动
        if type_move == 1:
            e.y += e.step
        ## 斜线移动
        if e.x <= 400:
            if type_move == 2:
                e.x += e.step * random.uniform(0.5,1)
                e.y += e.step * random.uniform(0.8,1)
        elif e.x > 400:
            if type_move == 2:
                e.x -= e.step * random.uniform(0.5,1)
                e.y += e.step * random.uniform(0.8,1)
        ## 左右移动，直到被击毁
        if type_move == 3:
            if e.x < 50:
                e.x += e.step
            elif e.x > 750:
                e.x -= e.step
        # 检测敌人与玩家距离
        if distance(e.x,e.y,player.x,player.y)<25:
            bao_sound.play()
            is_over=True
            enemies.clear()
        # 如果敌人飞出游戏界面，重置敌人
        if e.y > 600:
            e.reset()

# 子弹
bullets=[]
special_bullets = 3 # 清屏子弹 数量上限

def show_bullets():
    global screen
    for b in bullets:
        screen.blit(b.bulletImg, (b.x, b.y))
        hit(b)
        b.y -= b.step
        if b.y < 0:
            bullets.remove(b)

# 子弹命中
def hit(bullet):
    global score
    for e in enemies:
        if distance(bullet.x, bullet.y, e.x, e.y) < 30:
            bao_sound.play()
            score += 5
            bullets.remove(bullet)
            e.reset()
            break

#定义精灵组由两个图片组成来制造移动而不会断层
background1=background_sound()
background2=background_sound()
background2.rect.y = -background2.rect.height
bg_group = pygame.sprite.Group(background1, background2)

font=pygame.font.Font('freesansbold.ttf',32)
is_over=False

# 显示分数
def show_score():
    text=f"Score:{score}, BB:{special_bullets}"
    score_render=font.render(text,True,(255,255,255))
    screen.blit(score_render,(10,10))

over_font=pygame.font.Font('freesansbold.ttf',64)

# 检测游戏是否结束
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
        #update方法定义在background_sound包中
        #定义的是背景的移动
        bg_group.update()
        #draw为动画精灵的方法
        bg_group.draw(screen)
        show_score()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.horizontal=5
                    flag_RIGHT=1
                if event.key == pygame.K_LEFT:
                    player.horizontal=-5
                    flag_LEFT=1
                if event.key == pygame.K_UP:
                    player.vertical = -5
                    flag_UP=1
                if event.key == pygame.K_DOWN:
                    player.vertical = 5
                    flag_DOWN=1
                if event.key == pygame.K_SPACE:
                    print("发射子弹...")
                    bullets.append(Bullet(player.x, player.y))
                if event.key == pygame.K_r and special_bullets > 0: # 清屏炸弹
                    score += number_of_enemies * 5
                    for e in enemies:
                        e.reset()
                    special_bullets -= 1

            elif event.type == pygame.KEYUP:
                if event.key != pygame.K_SPACE:
                    if event.key == pygame.K_RIGHT:
                        flag_RIGHT = 0
                        if flag_LEFT == 0:
                            player.horizontal = 0
                        else:
                            player.horizontal = -5
                    if event.key == pygame.K_LEFT:
                        flag_LEFT = 0
                        if flag_RIGHT == 0:
                            player.horizontal = 0
                        else:
                            player.horizontal = 5
                    if event.key == pygame.K_DOWN:
                        flag_DOWN = 0
                        if flag_UP == 0:
                            player.vertical = 0
                        else:
                            player.vertical = 5
                    if event.key == pygame.K_UP:
                        flag_UP = 0
                        if flag_DOWN == 0:
                            player.vertical = 0
                        else:
                            player.vertical = -5
        
        show_bullets()
        screen.blit(player.img,(player.x,player.y))

        player.move_player()
        show_enemy()
        game_stage()
        check_is_over()
        pygame.display.update()