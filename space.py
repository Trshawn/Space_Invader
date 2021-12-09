import pygame
import math

from pygame.constants import K_LEFT, K_UP
from Background.background_sound import *
from Enemy.enemies import *
from Plane.player import *
from Bullet.bullets import *
from Enemy.boss import *
from Bullet.boss_bullets import *
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION
from Menu.my_menu import *

class Game:

    def __init__(self):
        # Initialisation interface
        pygame.init()


        self.number=0
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
        self.special_bullets = 3  # Max number of Ultimate shot

        # Init enemies
        self.number_of_enemies = 2
        self.enemies = []

        for i in range(self.number_of_enemies):
            self.Monster = Enemy()
            self.enemies.append(self.Monster)

        self.boss_flag=False
        self.boss_bullets = []
        pygame.time.set_timer(BOSS_BULLETS_EVENT, 1000) # Boss bullet shot interval

        # Others
        self.score = 0
        self.over_font = pygame.font.Font('freesansbold.ttf', 64)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        # self.is_over = False
        self.success = False

        self.flag_RIGHT = 0
        self.flag_DOWN = 0
        self.flag_LEFT = 0
        self.flag_UP = 0

        # menu
        self.bgImg_menu = pygame.image.load('./Background/bg.png')

        self.start_image = pygame.image.load("./Menu/resume_nor.png").convert_alpha()
        self.intro_image = pygame.image.load("./Menu/resume_nor.png").convert_alpha()
        self.ex_image = pygame.image.load("./Menu/resume_nor.png").convert_alpha()
        self.back_image = pygame.image.load("./Menu/resume_nor.png").convert_alpha()

        self.menu_image = pygame.image.load("./Menu/menu.png").convert_alpha()
        self.menu_rect = self.menu_image.get_rect()
        self.menu_rect.left,self.menu_rect.top = 300,100

        self.menu_resume_image = pygame.image.load("./Menu/menu_resume.png").convert_alpha()
        self.menu_resume_rect = self.menu_resume_image.get_rect()
        self.menu_resume_rect.left,self.menu_resume_rect.top = 400,200

        self.menu_quit_image = pygame.image.load("./Menu/quitgame_nor.png").convert_alpha()
        self.menu_quit_rect = self.menu_quit_image.get_rect()
        self.menu_quit_rect.left,self.menu_quit_rect.top = 400,300

        self.back_home_image = pygame.image.load("./Menu/home.png").convert_alpha()
        self.back_home_rect = self.back_home_image.get_rect()
        self.back_home_rect.left,self.back_home_rect.top = 400,400

        # restart
        self.restart_image = pygame.image.load("./Menu/restart.png").convert_alpha()
        self.restart_rect = self.restart_image.get_rect()
        self.restart_rect.left,self.restart_rect.top = 400,200

        # game pause
        self.pause = False
        self.game_play_image = pygame.image.load("./Menu/game_play.png").convert_alpha()
        self.game_pause_image = pygame.image.load("./Menu/game_pause.png").convert_alpha()
        self.audio_on_image = pygame.image.load("./Menu/audio_on.png").convert_alpha()
        self.audio_off_image = pygame.image.load("./Menu/audio_off.png").convert_alpha()

        self.pause_rect = self.game_pause_image.get_rect()
        self.pause_rect.left, self.pause_rect.top = 700,10
        self.pause_image = self.game_pause_image

         # pause music
        self.pause2 = False

        self.pause2_rect = self.audio_off_image.get_rect()
        self.pause2_rect.left, self.pause2_rect.top = 700,550
        self.pause2_image = self.audio_off_image

    # Menu display
    def menu(self):
        
        self.screen.blit(self.bgImg_menu,(0,0))
        start_button_rect = self.start_image.get_rect()
        start_button_rect.left, start_button_rect.top = 350,300
        self.screen.blit(self.start_image,start_button_rect)

        ex_button_rect = self.ex_image.get_rect()
        ex_button_rect.left, ex_button_rect.top = 350,500
        self.screen.blit(self.ex_image,ex_button_rect)

        pygame.display.update()
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button==1 and start_button_rect.collidepoint(event.pos):
                        flag = False
                    if event.button==1 and ex_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()

    # Event                    
    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button==1 and self.pause_rect.collidepoint(event.pos):
                        self.pause = not self.pause
                        if self.pause:
                            self.pause_image = self.game_play_image

                            self.temp_speed = []
                            #temp_y = []
                            for e in self.enemies:
                                self.temp_speed.append(e.speed)
                                e.speed = 0
                                #e.move_down = 0
                            try:
                                self.temp_ver = self.boss.vertical
                                self.tmep_hor = self.boss.horizontal
                                self.boss.vertical = 0
                                self.boss.horizontal = 0
                            except:
                                pass
                            

                        else:
                            self.pause_image = self.game_pause_image
                            for e in self.enemies:
                                e.speed = self.temp_speed[0]
                                del self.temp_speed[0]
                                #e.move_down = 40
                            try:
                                self.boss.vertical = self.temp_ver
                                self.boss.horizontal = self.tmep_hor
                            except:
                                pass

                if event.button==1 and self.menu_quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
                if event.button==1 and self.menu_resume_rect.collidepoint(event.pos):
                    self.pause = False
                    self.pause_image = self.game_pause_image
                    for e in self.enemies:
                        e.speed = self.temp_speed[0]
                        del self.temp_speed[0]
                    try:
                        self.boss.vertical = self.temp_ver
                        self.boss.horizontal = self.tmep_hor
                    except:
                        pass

                if event.button==1 and self.back_home_rect.collidepoint(event.pos):
                    #running = False
                    self.enemies.clear()
                    del self.boss
                    self.boss_bullets.clear()
                    self.number_of_enemies = 2
                    for i in range(self.number_of_enemies):
                        Monster = Enemy()
                        self.enemies.append(Monster) 
                    self.player=Planeplayer()
                    self.score = 0
                    self.special_bullets = 3
                    self.start_game()
                    
                
                if event.button==1 and self.restart_rect.collidepoint(event.pos):
                    self.enemies.clear()
                    del self.boss
                    self.boss_bullets.clear()
                    self.number_of_enemies = 2
                    for i in range(self.number_of_enemies):
                        Monster = Enemy()
                        self.enemies.append(Monster)     
                    self.player=Planeplayer()
                    #for e in enemies:
                    #    e.reset()
                    #    e.speed = 0.7
                    self.score = 0
                    self.special_bullets = 3
                    self.player.hp = 10
                    # self.is_over = False
                    self.start_game()
                
                if event.button==1 and self.pause2_rect.collidepoint(event.pos):
                    self.pause2 = not self.pause2
                    if self.pause2:
                        self.pause2_image = self.audio_on_image
                        pygame.mixer.music.stop()
                        
                    else:
                        self.pause2_image = self.audio_off_image
                        pygame.mixer.music.play(-1)
                        self.explosion = pygame.mixer.Sound('./Sound Effect/exp.wav')
            # Button click
            if not self.pause:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.player.horizontal = 5
                        self.flag_RIGHT = 1
                    if event.key == pygame.K_LEFT:
                        self.player.horizontal = -5
                        self.flag_LEFT = 1
                    if event.key == pygame.K_UP:
                        self.player.vertical = -5
                        self.flag_UP = 1
                    if event.key == pygame.K_DOWN:
                        self.player.vertical = 5
                        self.flag_DOWN = 1
                    if event.key == pygame.K_SPACE and self.player.hp != 0 and not self.success:
                        print("发射子弹...")
                        if self.score >= 70:  # double bullets
                            self.bullets.append(Bullet(self.player.x - self.player.img.get_width()/3, self.player.y))
                            self.bullets.append(Bullet(self.player.x + self.player.img.get_width()/3, self.player.y))
                            if self.score >= 100:  # triple bullets
                                self.bullets.append(Bullet(self.player.x, self.player.y)) 
                        else:
                            self.bullets.append(Bullet(self.player.x, self.player.y))
                    if event.key == pygame.K_r and self.special_bullets > 0:  # 清屏炸弹
                        self.score += self.number_of_enemies * 5
                        for e in self.enemies:
                            e.reset()
                        self.special_bullets -= 1

                # Avoid keyboard conflict
                elif event.type == pygame.KEYUP:
                    if event.key != pygame.K_SPACE:
                        if event.key == pygame.K_RIGHT:
                            self.flag_RIGHT = 0
                            if self.flag_LEFT == 0:
                                self.player.horizontal = 0
                            else:
                                self.player.horizontal = -5
                        if event.key == pygame.K_LEFT:
                            self.flag_LEFT = 0
                            if self.flag_RIGHT == 0:
                                self.player.horizontal = 0
                            else:
                                self.player.horizontal = 5
                        if event.key == pygame.K_DOWN:
                            self.flag_DOWN = 0
                            if self.flag_UP == 0:
                                self.player.vertical = 0
                            else:
                                self.player.vertical = 5
                        if event.key == pygame.K_UP:
                            self.flag_UP = 0
                            if self.flag_DOWN == 0:
                                self.player.vertical = 0
                            else:
                                self.player.vertical = -5
                try:
                    if event.type == BOSS_BULLETS_EVENT and self.boss_flag and self.boss.y > -50 and self.boss.health > 0:
                        if self.number%10 in [0,1,2,3,4]:
                            self.boss_bullets.append(BossBullet(self.boss.x+self.boss.image.get_width()/2-25,
                                                                self.boss.y+self.boss.image.get_height()-25, 0))
                            self.boss_bullets.append(BossBullet(self.boss.x + self.boss.image.get_width() / 2 - 25,
                                                                self.boss.y + self.boss.image.get_height() - 25, 1))
                            self.boss_bullets.append(BossBullet(self.boss.x + self.boss.image.get_width() / 2 - 25,
                                                                self.boss.y + self.boss.image.get_height() - 25, -1))
                        else:
                            self.boss_bullets.append(BossBullet(self.boss.x+self.boss.image.get_width()/2-25,
                                                                self.boss.y+self.boss.image.get_height()-25, 0))
                        self.number+=1
                except:
                    pass

    # Game difficulty
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
        if self.score == 45 and len(self.enemies) == 6:
            # Init boss
            self.boss = Boss()
            self.boss_flag = True

    # Bullet display
    def show_bullets(self):
        for b in self.bullets:
            self.screen.blit(b.bulletImg, (b.x, b.y))
            self.hit(b)
            b.y -= b.speed
            try:
                if self.distance(b.x, b.y, self.boss.x + 98, self.boss.y + 67) < 50:
                    self.boss.health -= 1
                    self.bullets.remove(b)
                    print(f"health -= 1\nhealth:{self.boss.health}")
            except: 
                pass
            if b.y < 0:
                self.bullets.remove(b)

    # Bullet hit
    def hit(self, bullet):
        for e in self.enemies:
            if self.distance(bullet.x, bullet.y, e.x, e.y) < 30:
                if self.pause2==False:
                    self.explosion.play()
                self.score += 5
                self.bullets.remove(bullet)
                e.reset()
                break

    # Enemy display
    def show_enemy(self):
        self.type_move = random.randint(1, 3)
        for e in self.enemies:
            self.screen.blit(e.enemyImg, (e.x, e.y))
            # Random action
            ## Vertical move
            if self.type_move == 1:
                e.y += e.speed
            ## Different angle
            if e.x <= 400:
                if self.type_move == 2:
                    e.x += e.speed * random.uniform(0.5, 1)
                    e.y += e.speed * random.uniform(0.8, 1)
            elif e.x > 400:
                if self.type_move == 2:
                    e.x -= e.speed * random.uniform(0.5, 1)
                    e.y += e.speed * random.uniform(0.8, 1)
            ## Horizontal move
            if self.type_move == 3:
                if e.x < 50:
                    e.x += e.speed
                elif e.x > 750:
                    e.x -= e.speed
            # Detect distance between enemy and player
            if self.distance(e.x, e.y, self.player.x, self.player.y) < 25:
                if self.pause2 == False:
                    self.explosion.play()
                self.player.hp -= 1
                # Hit by enemies and reset this enemy
                self.enemies.remove(e)
                self.enemies.append(e)
                e.reset()           
                # self.is_over = True
                if self.player.hp <= 0:
                    self.enemies.clear()
            # Outside the screen = reset
            if e.y > 600:
                e.reset()

    # Boss display
    def show_boss(self):
        if self.boss.health == 0:
            self.success = True
            self.enemies.clear()
        self.screen.blit(self.boss.image, (self.boss.x, self.boss.y))
        self.boss.update()

    # Boss bullet display
    def show_boss_bullets(self):
        for b in self.boss_bullets:
            self.screen.blit(b.img, (b.x, b.y))
            b.update()
            if b.y > self.SCREEN_HEIGHT:
                self.boss_bullets.remove(b)
            if self.distance(b.x, b.y, self.player.x, self.player.y) < 50:
                self.player.hp -= 1
                self.explosion.play()
                self.boss_bullets.remove(b)
                # self.is_over = True
                if self.player.hp <= 0:
                    if self.pause2 == True:
                        self.explosion.stop()
                    else:
                        self.explosion.play()
                    self.enemies.clear()

    # Distance formula
    def distance(self, bx, by, ex, ey):
        a = bx - ex
        b = by - ey
        return math.sqrt(a ** 2 + b ** 2)

    # Display score
    def show_score(self):
        text = f"Score:{self.score}, BB:{self.special_bullets}, HP:{self.player.hp}"
        score_render = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(score_render, (10, 10))

    # Player and Boss HP display
    def show_health(self, hp):
        # Player
        hp = self.player.hp
        red_x, red_y = 550, 20
        red_width, red_height = 130, 10
        green_x, green_y = 550, 20
        green_width, green_height = 130 - 13 * (10 - hp), 10
        # Draw Max HP bar and Current HP bar
        pygame.draw.rect(self.screen, (255, 0, 0), (red_x, red_y, red_width, red_height))        
        pygame.draw.rect(self.screen, (0, 255, 0), (green_x, green_y, green_width, green_height))
        # Boss
        try:
            bossHP = self.boss.health
            red_x, red_y = 350, 20
            red_width, red_height = 130, 10
            green_x, green_y = 350, 20
            green_width, green_height = 130 * (self.boss.health / 50), 10
            # Draw Max HP bar and Current HP bar
            pygame.draw.rect(self.screen, (255, 0, 0), (red_x, red_y, red_width, red_height))        
            pygame.draw.rect(self.screen, (0, 255, 0), (green_x, green_y, green_width, green_height))
        except:
            pass

        pygame.display.update()

    # Game complete
    def check(self):
        if self.player.hp <= 0:
            self.player.hp = 0
            text = "Game Over"
            render = self.over_font.render(text, True, (255, 255, 0))
            self.screen.blit(render, (200, 250))
        if self.success:
            text = "You Win"
            render = self.over_font.render(text, True, (255, 255, 0))
            self.screen.blit(render, (self.SCREEN_WIDTH/2 - 100, self.SCREEN_HEIGHT/2 - 50))

    # Game refresh
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

        # refresh menu button
        self.screen.blit(self.pause_image, self.pause_rect)
        self.screen.blit(self.pause2_image,self.pause2_rect)

        # refresh score
        self.show_score()

        # pause menu
        if self.pause:
            self.screen.blit(self.menu_image, self.menu_rect)     
            self.screen.blit(self.menu_resume_image, self.menu_resume_rect)
            self.screen.blit(self.menu_quit_image, self.menu_quit_rect)
            self.screen.blit(self.back_home_image,self.back_home_rect)

        # check
        self.check()
        if self.player.hp <= 0:
            self.player.hp = 0
            self.screen.blit(self.restart_image, self.restart_rect)

        # update screen
        pygame.display.update()

    def start_game(self):
        self.pause = False
        self.pause2 = False
        self.menu()
        while True:
            # self.clock.tick(self.FRAME)
            self.handle_events()
            self.game_stage()
            self.show_health(self.player.hp)
            self.player.move_player()
            self.refresh()


if __name__ == '__main__':
    game = Game()
    game.start_game()
