# import library for pygame
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


# define main game function
def alien_invasion():
    # initialize library pygame
    pygame.init()
    #
    settings = Settings()
    # creates our display by inputting width and height of display
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    #
    pygame.display.set_caption('Alien Invasion')
    # add ship
    ship = Ship(screen)

    aliens = Group()
    bullets = Group()

    gf.create_fleet(settings, screen, ship, aliens)

    # loop to start animation
    while True:

        # access event handler as function
        gf.check_events(settings, screen, ship, bullets)
       # updates the screen from game functions
        gf.update_screen(settings, screen, ship, aliens, bullets)

        #

alien_invasion()
