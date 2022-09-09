import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, penguin):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 50)
        self.color = 255, 245, 0
        self.speed = 10.5
        self.rect.centerx = penguin.rect.centerx
        self.rect.top = penguin.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)