import pygame

WIDTH = pygame.image.load("./Background/bg.png").get_width()
HEIGHT = pygame.image.load("./Background/bg.png").get_height()


class Planeplayer():

    def __init__(self, img="./Plane/player.png"):
        self.img = pygame.image.load(img)
        self.x = (WIDTH - self.img.get_width()) /2
        self.y = HEIGHT - self.img.get_height() - 50
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
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0


