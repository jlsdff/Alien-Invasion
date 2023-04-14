import pygame.font
class Scoreboard:
    """ class to manage scoreboard in the game """
    def __init__(self, game, x, y) -> None:
        """ Initialize scoreboard attributes, etc.."""
        # Game Access
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.game_stats
        # curren score attributes
        self.x, self.y = x, y
        self.width = 65
        self.height = 65
        # Font attributes
        self.font_color = (202, 240, 248)
        self.font = pygame.font.SysFont(None, 48)
        # rect
        self.prep_score()
        self.prep_highscore()
    
    def prep_score(self):
        self.msg = str(self.stats.score)
        self.image = self.font.render(
            self.msg, True, self.font_color
        )
        self.image_rect = self.image.get_rect()
        self.image_rect.center = 65, 65
    
    def prep_highscore(self):
        self.high_score = str(self.stats.high_score)
        self.img_high_score = self.font.render(
            self.high_score, True, self.font_color
        )
        self.img_high_score_rect = self.img_high_score.get_rect()
        self.img_high_score_rect.center = (self.screen_rect.width - 65), 65
    
    def show_score(self):
        self.screen.blit(self.image, self.image_rect)
        self.screen.blit(self.img_high_score, self.img_high_score_rect)
    
    def reset_score(self):
        self.stats.score = 0