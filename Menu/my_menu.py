# menu
import pygame

class Menu():
    def __init__(self):
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

        #game pause
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