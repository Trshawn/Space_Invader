import pygame

WIDTH = pygame.image.load("./Background/bg.png").get_width()

class Boss():
    def __init__(self,speed=1, img="./Enemy/boss.png"):
        self.image = pygame.image.load(img)
        self.x = (WIDTH-self.image.get_width())/2
        self.y = -20
        self.speed=speed
        

    def update(self):
        self.y+=self.speed
        