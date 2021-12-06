import pygame

WIDTH = pygame.image.load("./Background/bg.png").get_width()
HEIGHT = pygame.image.load("./Background/bg.png").get_height()

class Planeplayer():

    def __init__(self, x, y, img="./Plane/player.png"):
        self.x = x
        self.y = y
        self.img = pygame.image.load(img)
        self.horizontal = 0
        self.vertical = 0

    def move_player(self):
        self.x += self.horizontal
        self.y += self.vertical

        # Edge
        if self.x > WIDTH - self.img.get_width():
            self.x = WIDTH - self.img.get_width()
        if self.y > HEIGHT - self.img.get_height():
            self.y = HEIGHT - self.img.get_height()
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0


