import pygame.font

class Button:
    """ Class to manage buttons in the game """

    def __init__(self, game, msg, x ,y, width=200, height=50, fontsize=48) -> None:
        """ Initialize button attributes """
        # Screen Access
        self.msg = msg
        self.screen = game.screen
        self.settings = game.settings
        # Screen Rectangle
        self.screen_rect = self.screen.get_rect()
        self.screen_rect.y = y
        self.screen_rect.x = x
        # Set the main attributes and properties of the button
        self.width, self.height = width, height
        self.button_color = (208, 0, 0)
        self.text_color  = (3, 7, 30)
        self.font = pygame.font.SysFont('Terminal', fontsize)
        self.list_of_fonts = pygame.font.get_fonts()
        # Button's rect
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.x, self.screen_rect.y
        # Prepare the message
        self.prep_msg()
    
    def prep_msg(self):
        """ Turn the msg into rendered image and center text on the button """
        self.msg_image = self.font.render(self.msg, True, self.text_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center
    
    def draw_button(self):
        """ Draw the blank button and the message on the screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)
    
    def check_hover(self):
        """ Highlight the button if the mouse hover """
        highlight = self._check_mouse_hover()
        self._text_highlight(highlight)
    
    def update_msg(self, msg):
        """ Updates the text on the screen """
        self.msg = msg
        self.msg_image = self.font.render(self.msg, True, self.text_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center

    
    

########################
# REFACTORED FUNCTIONS #
########################

# Check hover
    def _check_mouse_hover(self):
        """ Returns True if mouse and button rect collide"""
        highlight = False
        mouse_pos = pygame.mouse.get_pos()
        hover = self.rect.collidepoint(mouse_pos)
        if hover:
            highlight = True
        else:
            highlight = False
        return highlight
    
    def _text_highlight(self, highlight):
        """ Changes the attributes value """
        if highlight:
            self.text_color = (208, 0, 0)
            self.button_color = (255, 31, 31)
        else:
            self._default_values()
    
    def _default_values(self):
        """ Returns the default value of attributes """
        self.text_color = (3, 7, 30)
        self.button_color = (208, 0, 0)

# 