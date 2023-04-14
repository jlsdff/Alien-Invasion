import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Class to manage bullets of the game """
    def __init__(self, game) -> None:
        """ Initialize bullet attributes """
        # Initialize bullet inheritance
        super().__init__()
        # Access the game
        self.ship = game.ship
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        # Attributes
        self.width = self.settings.bllt_width
        self.height = self.settings.bllt_height
        self.color = self.settings.bllt_color
        # Bullet rect
        self.rect = pygame.Rect(0,0, self.width, self.height)
        # Initial position
        self.rect.midtop = self.ship.rect.midtop
        # Coordinates
        self.y = self.rect.y
    
    def draw_bullet(self):
        """ Draw bullet to the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def update(self):
        """ Update the overall movement of the bullet """
        self.y -= self.settings.bllt_speed
        self.rect.y = self.y

class AlienBullet(Sprite):
    """ Class to manage alien bullets """
    def __init__(self, game, rect) -> None:
        super().__init__()
        # Access the game
        self.ship = rect
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.color = self.settings.bllt_color
        # Rect
        self.rect = pygame.Rect(
            0,0,self.settings.bllt_width, self.settings.bllt_height
            )
        # Initial position
        self.rect.midbottom = self.ship
        # Coordinates
        self.y = self.rect.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.y += self.settings.alien_bllt_spd
        self.rect.y = self.y
    
    


        
# _add_bullet
# _draw
# _update