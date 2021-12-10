import pygame
import random

HEIGHT = pygame.image.load("./Background/bg.png").get_height()

imgs = ["./Enemy/enemy3.png"]


class Enemy():
    def __init__(self, stage=0):
        self.stage = stage
        self.enemyImg = pygame.image.load(imgs[self.stage])
        self.x = random.randint(50, 750)
        self.y = -self.enemyImg.get_height()
        self.speed = 0.7

    def reset(self):
        self.x = random.randint(50, 750)
        self.y = -self.enemyImg.get_height()

