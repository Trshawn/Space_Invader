import pygame
import random

class Enemy():
    
    def __init__(self,img="./Enemy/enemy.png"):
        self.enemyImg=pygame.image.load(img)
        self.x=random.randint(200,600)
        self.y=random.randint(50,250)
        self.step=random.randint(2,6)

    def reset(self):
        self.x=random.randint(200,600)
        self.y=random.randint(50,250)
    # !
    def move(self):       
        self.x+=self.step
