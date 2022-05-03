

class Settings():
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """ initialize games setting"""
        # screen settings
        self.bg_color = (200,200,200)
        self.screen_width = 1200
        self.screen_height = 620

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_speed = 2
        self.bullet_limit = 3

        self.game_active = False
