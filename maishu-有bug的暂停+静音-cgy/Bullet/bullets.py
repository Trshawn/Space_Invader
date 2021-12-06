import pygame


class Bullet():
    def __init__(self, x, y):
        self.bulletImg = pygame.image.load('./Bullet/bullet.png')
        self.x = x + 16
        self.y = y + 10
        self.step = 5


