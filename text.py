import pygame.font

class Text:
    """ Class to manage texts' in game """
    def __init__(self, game, msg, x, y, fontsize=48) -> None:
        """ Initialize game attributes """
        # Access the game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.msg = msg
        self.x, self.y = x, y
        self.text_color = (3, 7, 30)
        self.font = pygame.font.SysFont(None, fontsize)
        # Text
        self.prep_msg()

    def prep_msg(self):
        self.image = self.font.render(self.msg, True, self.text_color)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.x, self.y
    
    def draw_text(self):
        self.screen.blit(self.image, self.image_rect)
