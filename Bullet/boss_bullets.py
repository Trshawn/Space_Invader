import pygame
import math

BOSS_BULLETS_EVENT = pygame.USEREVENT


class BossBullet(pygame.sprite.Sprite):

    def __init__(self, x, y, flag=0, img="./Bullet/boss_bullet0.png"):

        super().__init__()
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.speed = 3
        self.flag = flag

    def update(self):
        if self.flag == 0:
            self.y += self.speed
        if self.flag == 1:
            self.x += self.speed * math.sin(math.radians(40))
            self.y += self.speed * math.cos(math.radians(40))
        if self.flag == -1:
            self.x += self.speed * math.sin(math.radians(-40))
            self.y += self.speed * math.cos(math.radians(-40))



