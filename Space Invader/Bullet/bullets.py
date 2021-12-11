import pygame


class Bullet():
    def __init__(self, x, y):
        self.bulletImg = pygame.image.load('./Bullet/bullet2.png')
        self.x = x + 1
        self.y = y - 50
        self.speed = 5


