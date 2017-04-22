import sys
import pygame
from settings import Settings

ai_settings=Settings()
class Ship():
    def __init__(self):
        self.image=pygame.image.load('ship.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.c


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (80, 255, 0)
    while True:
        screen.fill(ai_settings.bg_colour)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


run_game()