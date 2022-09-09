import pygame, Controls
from penguin import Penguin
from pygame.sprite import Group
from stats import Stats
from scores import Scores



def run():
    pygame.init()
    screen = pygame.display.set_mode((1280, 1024))
    pygame.display.set_caption("Cold Ice")
    bg_color = (153, 217, 234)
    penguin = Penguin(screen)
    bullets = Group()
    inos = Group()
    Controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)



    while True:
        Controls.events(screen, penguin, bullets)
        if stats.run_game:
          penguin.update_penguin()
          Controls.update(bg_color, screen, stats, sc, penguin, inos, bullets)
          Controls.update_bullets(screen, stats, sc, inos, bullets)
          Controls.update_inos(stats, screen, sc, penguin, inos, bullets)



run()
