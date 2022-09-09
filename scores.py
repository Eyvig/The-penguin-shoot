import pygame.font
from penguin import Penguin
from pygame.sprite import Group

class Scores():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_penguins()

    def image_score(self):
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (153, 217, 234))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 50
        self.score_rect.top = 20

    def image_high_score(self):
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (153, 217, 234))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top + 20

    def image_penguins(self):
        self.penguins = Group()
        for penguin_number in range(self.stats.penguins_left):
            penguin = Penguin(self.screen)
            penguin.rect.x = 15 + penguin_number * penguin.rect.width
            penguin.rect.y = 20
            self.penguins.add(penguin)

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.penguins.draw(self.screen)
