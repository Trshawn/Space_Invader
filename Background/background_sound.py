import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, stage=0, speed=1, img='./Background/bg.png'):
        super().__init__()
        self.stage = stage
        self.image = pygame.image.load(img)
        self.speed = speed
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= self.image.get_height():
            self.rect.y = -self.image.get_height()
