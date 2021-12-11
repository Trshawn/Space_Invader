import pygame
import random

HEIGHT = pygame.image.load("./Background/bg.png").get_height()


class Enemy():
    def __init__(self, img="./Enemy/enemy3.png"):
        self.enemyImg = pygame.image.load(img)
        self.x = random.randint(50, 750)
        self.y = -self.enemyImg.get_height()
        self.speed = 0.7

    def reset(self):
        self.x = random.randint(50, 750)
        self.y = -self.enemyImg.get_height()

