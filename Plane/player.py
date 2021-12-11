import pygame

WIDTH = pygame.image.load("./Background/bg.png").get_width()
HEIGHT = pygame.image.load("./Background/bg.png").get_height()


class Planeplayer():

    def __init__(self, x=350, y=450, img="./Plane/player2.png"):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y
        self.horizontal = 0
        self.vertical = 0
        self.hp = 10

    def move_player(self):
        self.x += self.horizontal
        self.y += self.vertical

        # Edge
        if self.x > WIDTH - self.img.get_width():
            self.x = WIDTH - self.img.get_width()
        if self.y > HEIGHT - self.img.get_height():
            self.y = HEIGHT - self.img.get_height()
        if self.hp>0:
            if self.x < 0:
                self.x = 0
