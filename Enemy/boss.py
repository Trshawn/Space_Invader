import pygame
import random

#新加入了动画精灵用super调用精灵初始化
class Boss(pygame.sprite.Sprite):
    def __init__(self, img="./Enemy/boss.png"):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.x = -10
        self.y = 0
        self.horizon = random.randint(1, 3)
        self.vertical = random.randint(3, 9)

    def update(self):
        if self.x < 0:
            self.x = 0
        if self.x > 700:
            self.x = 700
        if self.y > 300:
            self.y = 300

        self.rect.x += self.horizon
        self.rect.y += self.vertical
        self.horizon = random.randint(1, 3)
        self.vertical = random.randint(3, 9)
