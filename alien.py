import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the alien fleet"""

    def __init__(self, settings, screen):
        super(Alien, self).__init__()

        # define attributes screen and settings
        self.screen = screen
        self.settings = settings

        # load alien ship image and scale it to fit screen & get rectangular properties
        self.image = pygame.image.load('images/alien.png') # loads image of alien ship from directory (pixabay.com)
        self.image = pygame.transform.scale(self.image, (80, 40)) # scales image of alien ship
        self.rect = self.image.get_rect()

        # set starting location
        self.rect.x =self.rect.width
        self.rect.y = self.rect.height
        self.rect.right = self.rect.right
        self.rect.left = self.rect.left

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # spacing for the fleet
        self.available_space_x = self.settings.screen_width -(2 * self.rect.width)
        self.number_of_aliens = int(self.available_space_x / (2* self.rect.width))

        self.speed = 1
        self.direction = 1


    def blitme(self):
        """ draw the alien on the screen"""
        # image_destination.blit(image being added, location)
        self.screen.blit(self.image, self.rect)

    def check_wall(self):
        """return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= -1:
            return True
    def update(self):
        if self.check_wall()    == True:
            print(self.direction)
            # self.rect.y += 1
            self.direction *= -1
        self.x += self.speed * self.direction
        self.rect.x = self.x


