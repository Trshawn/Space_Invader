import pygame
import math

BOSS_BULLETS_EVENT = pygame.USEREVENT


class BossBullet(pygame.sprite.Sprite):

    def __init__(self, x, y, img="./Bullet/boss_bullet0.png"):

        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.speed = 3

    def update(self):
        self.y += self.speed



