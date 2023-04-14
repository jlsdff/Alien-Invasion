import json
class GameStats:
    """ Class to manage game statistics """
    def __init__(self, game) -> None:
        """ Initialize game statistics attributes """
        # Game Access
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.score = 0
        self.high_score = 0
        self.ship_left = self.settings.ship_left
        self.alien_destroyed = 0
    
    def reset_stats(self):
        self.score = 0
        self.ship_left = 3
    
    def save_statistics(self):
        filename = "high_score.txt"
        with open(filename, 'w') as f:
            f.write(str(self.high_score))
    
    def load_statistics(self):
        filename = "high_score.txt"
        with open(filename, 'r') as f:
            highscore = f.read()
        self.high_score = int(highscore)
    
    def new_highscore(self, score):
        """ Replace the new high score """
        self.high_score = score