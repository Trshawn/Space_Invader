import pygame
import math

from pygame.constants import K_LEFT, K_UP
from Background.background_sound import *
from Enemy.enemies import *
from Plane.player import *
from Bullet.bullets import *
from Enemy.boss import *
from Bullet.boss_bullets import *


class Game:

    def __init__(self):
        # Initialisation interface
        pygame.init()

        # Screen
        self.SCREEN_WIDTH = pygame.image.load("./Background/bg.png").get_width()
        self.SCREEN_HEIGHT = pygame.image.load("./Background/bg.png").get_height()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Title & Icon
        pygame.display.set_caption("Space Invader")
        self.icon = pygame.image.load('icon.png')
        pygame.display.set_icon(self.icon)

        # frame
        self.clock = pygame.time.Clock()
        self.FRAME = 120

        # Play bgm
        pygame.mixer.music.load('./Background/bg.wav')
        pygame.mixer.music.play(-1)

        # Explosion sound effect
        self.explosion = pygame.mixer.Sound('./Sound Effect/exp.wav')

        # Init background
        background1 = Background()
        background2 = Background()
        background2.rect.y = -background2.rect.height
        self.bg_group = pygame.sprite.Group(background1, background2)

        # Init player
        self.player = Planeplayer()

        # Init bullets
        self.bullets = []
        self.special_bullets = 3  # 清屏子弹 数量上限

        # Init enemies
        self.number_of_enemies = 2
        self.enemies = []

        for i in range(self.number_of_enemies):
            self.Monster = Enemy()
            self.enemies.append(self.Monster)

        self.boss_flag=False
        self.boss_bullets = []
        pygame.time.set_timer(BOSS_BULLETS_EVENT, 200)

        # Others
        self.score = 0
        self.over_font = pygame.font.Font('freesansbold.ttf', 64)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.is_over = False

    def handle_events(self):
        flag_RIGHT = 0
        flag_DOWN = 0
        flag_LEFT = 0
        flag_UP = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.horizontal = 5
                    flag_RIGHT = 1
                if event.key == pygame.K_LEFT:
                    self.player.horizontal = -5
                    flag_LEFT = 1
                if event.key == pygame.K_UP:
                    self.player.vertical = -5
                    flag_UP = 1
                if event.key == pygame.K_DOWN:
                    self.player.vertical = 5
                    flag_DOWN = 1
                if event.key == pygame.K_SPACE:
                    print("发射子弹...")
                    self.bullets.append(Bullet(self.player.x, self.player.y))
                if event.key == pygame.K_r and self.special_bullets > 0:  # 清屏炸弹
                    self.score += self.number_of_enemies * 5
                    for e in self.enemies:
                        e.reset()
                    self.special_bullets -= 1

            elif event.type == pygame.KEYUP:
                if event.key != pygame.K_SPACE:
                    if event.key == pygame.K_RIGHT:
                        flag_RIGHT = 0
                        if flag_LEFT == 0:
                            self.player.horizontal = 0
                        else:
                            self.player.horizontal = -5
                    if event.key == pygame.K_LEFT:
                        flag_LEFT = 0
                        if flag_RIGHT == 0:
                            self.player.horizontal = 0
                        else:
                            self.player.horizontal = 5
                    if event.key == pygame.K_DOWN:
                        flag_DOWN = 0
                        if flag_UP == 0:
                            self.player.vertical = 0
                        else:
                            self.player.vertical = 5
                    if event.key == pygame.K_UP:
                        flag_UP = 0
                        if flag_DOWN == 0:
                            self.player.vertical = 0
                        else:
                            self.player.vertical = -5

            elif event.type == BOSS_BULLETS_EVENT and self.boss_flag:
                self.boss_bullets.append(BossBullet(self.boss.x+self.boss.image.get_width()/2-25, self.boss.y+self.boss.image.get_height()-25))

    # 游戏难度
    def game_stage(self):
        if self.score == 20 and len(self.enemies) == 2:
            self.enemies.clear()
            for i in range(self.number_of_enemies):
                self.Monster = Enemy()
                self.number_of_enemies = 4
                self.enemies.append(self.Monster)
            return
        if self.score == 40 and len(self.enemies) == 4:
            self.enemies.clear()
            for i in range(self.number_of_enemies):
                self.Monster = Enemy()
                self.number_of_enemies = 6
                self.enemies.append(self.Monster)
            return
        if self.score == 50 and len(self.enemies) == 6:
            # Init boss
            self.boss = Boss()
            self.boss_flag = True

    def show_bullets(self):
        for b in self.bullets:
            self.screen.blit(b.bulletImg, (b.x, b.y))
            self.hit(b)
            b.y -= b.step
            if b.y < 0:
                self.bullets.remove(b)

    # 子弹命中
    def hit(self, bullet):
        for e in self.enemies:
            if self.distance(bullet.x, bullet.y, e.x, e.y) < 30:
                self.explosion.play()
                self.score += 5
                self.bullets.remove(bullet)
                e.reset()
                break

    # 敌人显示
    def show_enemy(self):
        self.type_move = random.randint(1, 3)
        for e in self.enemies:
            self.screen.blit(e.enemyImg, (e.x, e.y))
            # 敌人随机路线
            ## 直线移动
            if self.type_move == 1:
                e.y += e.step
            ## 斜线移动
            if e.x <= 400:
                if self.type_move == 2:
                    e.x += e.step * random.uniform(0.5, 1)
                    e.y += e.step * random.uniform(0.8, 1)
            elif e.x > 400:
                if self.type_move == 2:
                    e.x -= e.step * random.uniform(0.5, 1)
                    e.y += e.step * random.uniform(0.8, 1)
            ## 左右移动，直到被击毁
            if self.type_move == 3:
                if e.x < 50:
                    e.x += e.step
                elif e.x > 750:
                    e.x -= e.step
            # 检测敌人与玩家距离
            if self.distance(e.x, e.y, self.player.x, self.player.y) < 25:
                self.explosion.play()
                self.is_over = True
                self.enemies.clear()
            # 如果敌人飞出游戏界面，重置敌人
            if e.y > 600:
                e.reset()

    def show_boss(self):
        if self.boss.y > 70:
            self.boss.y = 70
        self.screen.blit(self.boss.image, (self.boss.x, self.boss.y))
        self.boss.update()

    def show_boss_bullets(self):
        for b in self.boss_bullets:
            self.screen.blit(b.img, (b.x, b.y))
            b.update()

    def distance(self, bx, by, ex, ey):
        a = bx - ex
        b = by - ey
        return math.sqrt(a ** 2 + b ** 2)

    # 显示分数
    def show_score(self):
        text = f"Score:{self.score}, BB:{self.special_bullets}"
        score_render = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(score_render, (10, 10))

    # 检测游戏是否结束
    def check_is_over(self):
        if self.is_over:
            text = "Game Over"
            render = self.over_font.render(text, True, (255, 255, 0))
            self.screen.blit(render, (200, 250))

    def refresh(self):

        # refresh background
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        # refresh player
        self.screen.blit(self.player.img, (self.player.x, self.player.y))

        # refresh objects
        self.show_bullets()
        self.show_enemy()
        try:
            self.show_boss()
            self.show_boss_bullets()
        except:
            pass

        # refresh score
        self.show_score()

        # check
        self.check_is_over()

        # update screen
        pygame.display.update()

    def start_game(self):

        while True:
            # self.clock.tick(self.FRAME)
            self.handle_events()
            self.game_stage()
            self.player.move_player()
            self.refresh()


if __name__ == '__main__':
    game = Game()
    # game.main_menu
    game.start_game()
