import pygame

class Image:
    """ Class to manage game images """
    def __init__(self, game, image, x, y, add=False) -> None:
        # Access game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        # Detail attributes
        self.hover_color = (255, 31, 31)
        # Load image and get its rect
        self.image = image
        self.rect = self.image.get_rect()
        # Set the initial position
        self.x = x
        self.y = y
        self.screen_rect.x = self.x 
        self.screen_rect.y = self.y 
        self.rect.center = self.screen_rect.x, self.screen_rect.y
    
    def draw_image(self):
        self.screen.blit(self.image, self.rect)
    
    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.screen.fill(self.hover_color, self.rect)
    
    def transform_scale(self, width, height):
        """ Transfor a scale of the image """
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y


