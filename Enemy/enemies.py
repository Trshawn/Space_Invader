import pygame
import random

HEIGHT = pygame.image.load("./Background/bg.png").get_height()


class Enemy():
    def __init__(self,img="./Enemy/enemy.png"):
        self.enemyImg=pygame.image.load(img)
        self.x=random.randint(50,750)
        self.y = -self.enemyImg.get_height()
        self.speed=2

    def reset(self):
        self.x=random.randint(50,750)
        self.y=random.randint(50,150)

    def update(self):
        if self.y < HEIGHT/3:
            self.speed = 2
        else:
            self.speed = 1
