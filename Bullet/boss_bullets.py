import pygame
import math

BOSS_BULLETS_EVENT = pygame.USEREVENT


class BossBullet(pygame.sprite.Sprite):

    def __init__(self, x, y, stage=0, flag=0, img="./Bullet/boss_bullet0.png"):

        super().__init__()
        self.stage = stage
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.speed = 3
        self.flag = flag
        self.switch = -3
        self.switch_speed = 3

    def update(self):
        self.switch += self.switch_speed
        if self.switch > 60 or self.switch < - 60:
            self.switch_speed = -self.switch_speed
        if self.stage == 0:
            self.switch = 0
        if self.flag == 0:
            self.x += self.speed * math.sin(math.radians(self.switch))
            self.y += self.speed * math.cos(math.radians(self.switch))
        if self.flag == 1:
            self.x += self.speed * math.sin(math.radians(40 + self.switch))
            self.y += self.speed * math.cos(math.radians(40 + self.switch))
        if self.flag == -1:
            self.x += self.speed * math.sin(math.radians(-40 + self.switch))
            self.y += self.speed * math.cos(math.radians(-40 + self.switch))
        if self.flag == 2:
            self.x += self.speed * math.sin(math.radians(80 + self.switch))
            self.y += self.speed * math.cos(math.radians(80 + self.switch))
        if self.flag == -2:
            self.x += self.speed * math.sin(math.radians(-80 + self.switch))
            self.y += self.speed * math.cos(math.radians(-80 + self.switch))


