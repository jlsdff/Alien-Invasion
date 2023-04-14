import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    """ Class to manage aliens in the game """
    def __init__(self, game) -> None:
        super().__init__()
        # Access to the screen
        self.ship = game.ship
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        # Image and rect
        self.image = pygame.image.load("Assets/alien.png")
        self.rect = self.image.get_rect()
        self.speed_x = self.settings.alien_speed
        self.speed_y = self.settings.alien_speed
        # initial position
        self.rect.midtop = random.randint(65,1100), self.screen_rect.top + 65
        # Coordinates
        self.x = self.rect.x
        self.y = self.rect.y
        self.randomx()

        # Sensor
            # Left
        self.sensor_rect_left = pygame.Rect(0, 0, 65, 65)
        self.sensor_rect_left.center = (
            self.rect.centerx, self.ship.rect.centery
        )
        self.sensor_x = self.sensor_rect_left.x - 100
        self.sensor_y = self.sensor_rect_left.y
            # Right
        self.sensor_rect_right = pygame.Rect(0,0, 65, 65)
        self.sensor_rect_right.center = (
            self.rect.centerx, self.ship.rect.centery
        )
        self.sensor_xr = self.sensor_rect_right.x + 100
        self.sensor_yr = self.sensor_rect_right.y
    
    def randomx(self):
        randomx = random.randint(1,2)
        randomy = random.randint(1,2)
        if randomx == 1:
            self.speed_x *= -1
        else:
            self.speed_x *= 1
        if randomy == 1:
            self.speed_y *= -1
        else:
            self.speed_y *= 1

    
    def update(self):
        """ update movement of aliens """
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges_x(self):
        if (self.rect.right >= self.screen_rect.right or 
                self.rect.left <= self.screen_rect.left
            ):
            return True
    
    def check_edges_y(self):
        if (
            self.rect.top <= 0 or
            self.rect.bottom >= self.screen_rect.bottom
        ):
            return True
        
    
# Sensors
    def draw_sensor(self):
        self.screen.fill((255, 186, 8), self.sensor_rect_left)
        self.screen.fill((255, 186, 8), self.sensor_rect_right)
    
    def update_sensor(self):
        # sensor left
        self.sensor_x = self.rect.x - 100
        self.sensor_y = self.ship.rect.centery
        self.sensor_xr = self.rect.x + 100
        self.sensor_yr = self.ship.rect.centery
        # update left
        self.sensor_rect_left.x = self.sensor_x
        self.sensor_rect_left.y = self.sensor_y
        self.sensor_rect_right.x = self.sensor_xr
        self.sensor_rect_right.y = self.sensor_yr
