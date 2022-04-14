import pygame

class Ship():

    def __init__(self, screen):
        self.screen = screen

        # load image of ship and access image data
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (30, 60))
        # tells computer to interpret self.image as a rectangle
        self.rect = self.image.get_rect()
        # tells computer to interpret the screen as a rectangle
        self.screen_rect = screen.get_rect()

        # set starting location of each ship
        # makes center x value of ship equal to the center x value of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # makes the bottom of the ship the same as the bottom of screen
        self.rect.bottom = self.screen_rect.bottom

        # create movement flag to determine if ship is moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """ draw the ship on the screen"""
        # image.blit(image being added, location)
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ updates image of ship left/ right"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1
