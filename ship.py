import pygame

class Ship:
    """ Class to manage the main ship """
    def __init__(self, game) -> None:
        # Access the game screen
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        # Load image of ship and get it's rect
        self.image = pygame.image.load("Assets/1.png")
        self.image = pygame.transform.scale(self.image, (65,65))
        self.rect = self.image.get_rect()
        # Initial position
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = self.rect.x
        self.y = self.rect.y
        # Movement Flag
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
    
    def draw_ship(self):
        self.screen.blit(self.image, self.rect)
    
    def move_ship(self):
        """ Move the ship """
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        if self.move_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        # Update rect
        self.rect.x = self.x
        self.rect.y = self.y
    
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = self.rect.x
        self.y = self.rect.y