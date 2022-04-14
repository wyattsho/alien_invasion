import pygame
from pygame.sprite import Sprite
from alien import Alien

class Bullets(Sprite):
    """a class to manage the bullets fired from ship"""

    def __init__(self, settings, screen, ship):
        """initilizes a bullet object and tracks he position of the screen"""
        super(Bullets, self).__init__()
        self.screen = screen


        # create bullet rectangle
        # create a rectangular bullet at 0,0
        self.rect = pygame.Rect(0,0, settings.bullet_width, settings.bullet_height)
        # move bullet to center top of ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # stores the bullets position as a decimal value
        self.y = float(self.rect.y)

        # assign color to bullets
        self.color = settings.bullet_color

        # speed of bullet
        self.speed = settings.bullet_speed

        # bullet magazine
        self.limit = 3

    def update(self):
        # moves bullet up screen
        self.y -= self.speed
        self.rect.y = self.y



    def draw_bullets(self):
        # draw bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)
        
