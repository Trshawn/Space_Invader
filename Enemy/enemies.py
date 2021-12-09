import pygame
import random

class Enemy():
    def __init__(self,img="./Enemy/enemy.png"):
        self.enemyImg=pygame.image.load(img)
        self.x=random.randint(50,750)
        self.y=random.randint(50,150)
        self.speed=0.7

    def reset(self):
        self.x=random.randint(50,750)
        self.y=random.randint(50,150)