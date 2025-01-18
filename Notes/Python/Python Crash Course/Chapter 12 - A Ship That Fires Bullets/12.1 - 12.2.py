import sys
import pygame
from settings import Settings
from cat import Cat

# 12-1. Blue Sky / 12-2. Game Character
# cat_invasion.py
class CatInvasion:
    def __init__(self):
        pygame.init()   # initializes the background settings
        self.clock = pygame.time.Clock() # frame rate
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.cat = Cat(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.cat.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    ci = CatInvasion()
    ci.run_game()


# cat.py 
import pygame

class Cat:
    def __init__(self, ci_game):
        self.screen = ci_game.screen
        self.screen_rect = ci_game.screen.get_rect()

        self.image = pygame.image.load('images/animal_crossing_character.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)


# settings.py
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (173, 216, 230)
