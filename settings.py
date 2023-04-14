from alien import Alien
import pygame

class Settings:
    """ Class to manage game attributes """
    
    def __init__(self) -> None:
        """ Initialize the settings attributes """
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 720
        self.icon = pygame.image.load("Assets/icon.png")
        self.caption = "Alien Invasion"
        self.bg_color = (255, 186, 8)
        self.bg_color_main_game = (3, 4, 94)
        # Diffiulty
        self.diff_dict = {'easy':{
                                    'setted':'easy',                                    
                                    'alien_speed': 1, 
                                    'alien_bllt_spd': 1.5,
                                    'aliens_allowed': 2,
                                    'alien_bullet_allowed': 2,
                                    'ship_speed': 2,
                                    'bllt_speed': 1.5
                            }, 'medium':{
                                    'setted':'medium',
                                    'alien_speed': 2, 
                                    'alien_bllt_spd': 2,
                                    'aliens_allowed': 4,
                                    'alien_bullet_allowed': 5,
                                    'ship_speed': 2.5,
                                    'bllt_speed': 2
                            }, 'hard':{
                                    'setted':'hard',
                                    'alien_speed': 3, 
                                    'alien_bllt_spd': 2.5,
                                    'aliens_allowed': 6,
                                    'alien_bullet_allowed': 5,
                                    'ship_speed': 3,
                                    'bllt_speed': 2.5
                            }, 'insane':{
                                    'setted':'insane',
                                    'alien_speed': 3.5, 
                                    'alien_bllt_spd': 3,
                                    'aliens_allowed': 7,
                                    'alien_bullet_allowed': 6,
                                    'ship_speed': 3.5,
                                    'bllt_speed': 3
                                }}
        self.diff = 0
        self.difficulty = [ self.diff_dict['easy']['setted'], 
                            self.diff_dict['medium']['setted'], 
                            self.diff_dict['hard']['setted'], 
                            self.diff_dict['insane']['setted']
                            ]
        self.set_difficulty = self.difficulty[self.diff]
        # Ship settings
        self.ship_speed = 2
        self.ship_left = 3
        # Alien Settings
        self.alien_speed = 1
        self.alien_bllt_spd = 1.5
        self.aliens_allowed = 2
        self.alien_direction = 1
        self.alien_bullet_allowed = 2
        self.alien_points = 5
        # Bullet Settings
        self.bllt_width = 5
        self.bllt_height = 15
        self.bllt_color = (255, 186, 8)
        self.bllt_speed = 1.5
        self.bllt_allowed = 5
        
    
    def increase_diff(self):
        """" Increase the difficulty of the game """
        try:
            if self.diff <= 2 and self.diff >= 0:
                self.diff = self.diff + 1
                self.set_difficulty = self.difficulty[self.diff]
            else:
                self.diff = 0
                self.set_difficulty = self.difficulty[self.diff]
        except:
            print("Out of range")
            pass
        
    
    def decrease_diff(self):
        """ Decrease the difficulty of the game """
        try:
            if self.diff <= 3 and self.diff >= 1:
                self.diff = self.diff - 1
                self.set_difficulty = self.difficulty[self.diff]
            else:
                self.diff = 3
                self.set_difficulty = self.difficulty[self.diff]
        except:
            print("Out of range")
            pass
    
    
