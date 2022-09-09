import pygame
from pygame.sprite import Sprite

class Penguin(Sprite):

    def __init__(self, screen):
        super(Penguin, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/PING.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_penguin(self):

        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 4.5
        elif self.mleft and self.rect.left > 0:
            self.center -= 4.5

        self.rect.centerx = self.center

    def create_penguin(self):
        self.center = self.screen_rect.centerx