import pygame


class background_sound():
    def __init__(self,img='./Background/bg.png',sound='./Background/bg.wav'):
        self.img=pygame.image.load(img)
        self.sound=pygame.mixer.music.load(sound)
        pygame.mixer.music.play(-1)

        