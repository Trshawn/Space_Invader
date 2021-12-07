import pygame

#新加入了动画精灵用super调用精灵初始化
class background_sound(pygame.sprite.Sprite):
    def __init__(self,speed=1,img='./Background/bg.png'):
        super().__init__()
        self.image=pygame.image.load(img)
        self.speed=speed
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y+=self.speed
        if self.rect.y>=self.image.get_height():
            self.rect.y=-self.image.get_height()
        

        