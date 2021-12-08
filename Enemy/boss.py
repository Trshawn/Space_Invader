import random

import pygame

WIDTH = pygame.image.load("./Background/bg.png").get_width()


class Boss():
    def __init__(self,speed=1, img="./Enemy/boss.png"):
        self.image = pygame.image.load(img)
        self.x = (WIDTH-self.image.get_width())/2
        self.y = -self.image.get_height()
        self.vertical = speed
        direction = [1, -1]
        self.horizontal = speed * direction[random.randint(0, 1)]
        self.health = 10

    def update(self):
        self.y += self.vertical

        if self.y > 70:
            self.y = 70
            self.x += self.horizontal
            if self.x > 600 or self.x < 0:
                self.horizontal = -self.horizontal

        if self.health == 0:
            self.image = pygame.image.load("./Enemy/null.png")

        