import pygame

imgs = ["./Background/bg.png",
        "./Background/bg.png"]


class Background(pygame.sprite.Sprite):
    def __init__(self, stage=0, speed=1):
        super().__init__()
        self.stage = stage
        self.image = pygame.image.load(imgs[self.stage])
        self.speed = speed
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= self.image.get_height():
            self.rect.y = -self.image.get_height()
