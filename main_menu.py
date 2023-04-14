from time import sleep
import pygame, sys
from pygame.constants import QUIT
from settings import Settings
from button import Button
from image import Image
from ship import Ship
from alien import Alien
from bullets import *
from game_stats import GameStats
from scoreboard import Scoreboard
from text import Text

class MainMenu:
    """ Class to manage main assets and game resources """
    
    def __init__(self) -> None:
        """ Initialize game attributes """
        pygame.init()
        self.settings = Settings()
        width = self.settings.screen_width
        height = self.settings.screen_height
        self.screen = pygame.display.set_mode((width, height))
        self.screen_rect = self.screen.get_rect()   
        pygame.display.set_caption(self.settings.caption)
        pygame.display.set_icon(self.settings.icon)
        self.clock = pygame.time.Clock()
# Game Assets
        self.ship = Ship(self)
        self.game_stats = GameStats(self)
        self.game_stats.load_statistics()
        self.sb = Scoreboard(self, 65, 65)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()
# Designs
        # Stars
        self.stars = self._prep_stars_image()
        self.stars.transform_scale(1200, 
                                725)
        # Nebula
        self.nebula = self._prep_nebula_image()
        # heart
        self.heart = self._prep_heart_image()
        self.heart.transform_scale(65, 65)
        # ship left text
        self.ship_left_text = self._prep_ship_left()
        # Background
        self.backround = self._prep_bg_image()
# Game Buttons and text
        self.play_button = self._prep_play_button()
        self.settings_button = self._prep_setting_button()
        self.exit_button = self._prep_exit_button()
        self.difficulty_button = self._prep_diff_button()
        self.next_button = self._prep_next_button()
        self.prev_botton = self._prep_prev_button()
        self.back_button = self._prep_back_button()
        self.logo = self._logo_image()
        self.pause_button = self._prep_pause_button()
        self.exit_main_menu_button = self._prep_exit_to_main_menu_button()
        self.game_over = self._prep_game_over()
        self.restart_button = self._prep_restart_button()
        self.high_score_text = self._prep_highscore_text()
        self.difficulty_text = self._prep_difficulty_text()
# Sounds
        self.click_sound = pygame.mixer.Sound("sounds/click.wav")
        self.explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
        self.shoot_sound = pygame.mixer.Sound("sounds/lasershoot.wav")
# Switches
        # Switches
        self.mainmenu = True
        self.setting_switch = False
        self.play_switch = False
        self.pause_switch = False
# Checkings
        self._check_print()
# Game methods
    def main_menu(self):
        """ Loop of the main menu """
        while self.mainmenu:
            for event in pygame.event.get():
                self._check_events(event)
            self._update_screen_main_menu()
    
    def setting_menu(self):
        """ Loop of the setting menu """
        while self.setting_switch:
            for event in pygame.event.get():
                self._check_events(event)
            self._update_screen_setting_menu()
    
    def main_game(self):
        """ Loop for the main game """
        while self.play_switch:
            for event in pygame.event.get():
                self._check_events(event)
            self._update_screen_main_game()
            

#######################
# REFACTORED FUNCTION #
#######################

# Screen
    def _update_screen_main_menu(self):
        self.screen.fill(self.settings.bg_color)
        self._draw_check_hover()
        pygame.display.flip()
    
    def _update_screen_setting_menu(self):
        self.screen.fill(self.settings.bg_color)
        self._draw_check_hover_settings()
        pygame.display.flip()
    
    def _update_screen_main_game(self):
        self.screen.blit(self.backround.image, self.backround.rect)
        #stars.draw_image()
        #self.nebula.draw_image()
        if self.game_stats.ship_left > 0:
            self.high_score_text.draw_text()
            self.heart.draw_image()
            self.ship_left_text.draw_text()
            self.sb.show_score()
            self._draw_bullet()
            self._draw_alien_bullet()
            self.aliens.draw(self.screen)
            self.ship.draw_ship()
            self._update_event()
        else:
            self.game_over.draw_button()
            self.restart_button.draw_button()
            self.restart_button.check_hover()
        pygame.display.flip()

# Events
    def _check_events(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._click_resume()
            self._click_play()
            self._click_setting()
            self._click_exit()
            self._click_next()
            self._click_prev()
            self._click_back()
            self._click_exit_main_menu()
            self._click_restart()
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            if self.pause_switch == True:
                self.pause_switch = False
            else:
                self.pause_switch = True
        elif event.key == pygame.K_d:
            self.ship.move_right = True
        elif event.key == pygame.K_a:
            self.ship.move_left = True
        elif event.key == pygame.K_w:
            self.ship.move_up = True
        elif event.key == pygame.K_s:
            self.ship.move_down = True
        elif event.key == pygame.K_SPACE:
            self.shoot_sound.play()
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.ship.move_right = False
        elif event.key == pygame.K_a:
            self.ship.move_left = False
        elif event.key == pygame.K_w:
            self.ship.move_up = False
        elif event.key == pygame.K_s:
            self.ship.move_down = False

    def _update_event(self):
        if self.pause_switch:
            self.pause_button.draw_button()
            self.pause_button.check_hover()
            self.exit_main_menu_button.draw_button()
            self.exit_main_menu_button.check_hover()
        elif not self.pause_switch:
            self._add_alien()
            self._update_alien()
            self._update_sensor()
            self._add_bullet()
            self._update_alien_bullets()
            self._check_print()
            self._update_bullets()
            if self._check_ship_collision() or self._check_alien_bullet_collision():
                self._ship_hit()
            self.ship.move_ship()
# Buttons
    def _draw_check_hover(self):
        self.play_button.draw_button()
        self.play_button.check_hover()
        self.settings_button.draw_button()
        self.settings_button.check_hover()
        self.exit_button.draw_button()
        self.exit_button.check_hover()
        self.logo.draw_image()
    
    def _draw_check_hover_settings(self):
        self.difficulty_text.draw_text()
        self.difficulty_button.draw_button()
        self.back_button.draw_button()
        self.back_button.check_hover()
        self.next_button.check_hover()
        self.prev_botton.check_hover()
        self.next_button.draw_image()
        self.prev_botton.draw_image()
        self.difficulty_button.update_msg(self.settings.set_difficulty)

# Refactored buttons
    def _prep_play_button(self):
        """ Return an instance of button (play button) """
        play_x = self.settings.screen_width * (1/2)
        play_y = (self.settings.screen_height * (1/3)) + 250
        return (Button(self, "Play", play_x, play_y))
    
    def _prep_setting_button(self):
        """ Return an instance of button (setting button) """
        settings_x = self.settings.screen_width * (1/2)
        settings_y = (self.settings.screen_height * (1/3)) + 325
        return (Button(self, "Settings",settings_x,settings_y))
    
    def _prep_exit_button(self):
        """ Return an instance of button (exit button) """
        exit_x = self.settings.screen_width * (1/2)
        exit_y = (self.settings.screen_height * (1/3)) + 400
        return (Button(self, "Exit" , exit_x, exit_y))
    
    def _prep_diff_button(self):
        """ Return an instance of button (diff button) """
        diff_x = self.settings.screen_width * (1/2)
        diff_y = self.settings.screen_height * (1/3)
        diff = self.settings.set_difficulty
        return (Button(self, diff, diff_x, diff_y))
    
    def _prep_next_button(self):
        """ Return an instance of button (next button) """
        next = pygame.image.load("Assets/next.png")
        next_x = self.difficulty_button.rect.right + 50
        next_y = self.difficulty_button.rect.centery
        return Image(self, next, next_x, next_y)
    
    def _prep_back_button(self):
        """ Return an instance of button (back button) """
        back_x = self.difficulty_button.rect.centerx
        back_y = self.difficulty_button.rect.centery + 100
        return Button(self, "Back", back_x, back_y)

    def _prep_prev_button(self):
        """ return an instance of button (prev button) """
        prev = pygame.image.load("Assets/prev.png")
        prev_x = self.difficulty_button.rect.left - 50
        prev_y = self.difficulty_button.rect.centery
        return Image(self, prev, prev_x, prev_y, True)
    
    def _logo_image(self):
        """ Return an instance of the logo """
        logo = pygame.image.load("Assets/logo.png")
        logo_x = (self.settings.screen_width * (1/2))
        logo_y = (self.settings.screen_height * (1/3))
        return Image(self, logo, logo_x, logo_y, True)
    
    def _prep_pause_button(self):
        """ Return an instance of pause button """
        pause_x = self.screen_rect.centerx
        pause_y = self.screen_rect.centery
        return Button(self, "Resume", pause_x, pause_y)
    
    def _prep_exit_to_main_menu_button(self):
        """ Return an instance of button """
        x = self.pause_button.rect.centerx
        y = self.pause_button.rect.centery + 75
        return Button(self,"Exit to main menu", x, y, 300)
    
    def _prep_stars_image(self):
        """ return an instance of the star image """
        star_x, star_y = self.screen_rect.center
        image = pygame.image.load("Assets/Stars.png")
        return Image(self, image, star_x, star_y)
    
    def _prep_nebula_image(self):
        """ Return an instance of the star image """
        image = pygame.image.load("Assets/Nebula3.png")
        x = self.screen_rect.centerx
        y = self.screen_rect.centery
        return Image(self, image, x, y)
    
    def _prep_game_over(self):
        """ Return an instance of the game over pop-up"""
        x,y = self.screen_rect.center
        return Button(self,"Game over", x, y)
    
    def _prep_restart_button(self):
        """ Return an instance of restart button """
        x, y = self.screen_rect.center
        return Button(self, "Restart", x, y+75)
    
    def _prep_highscore_text(self):
        """ Return an instance of highscore """
        msg = "High Score"
        x = self.settings.screen_width - 65
        y = 40
        return Text(self, msg, x, y, 30)
    
    def _prep_heart_image(self):
        """ Return an instance of heart image """
        image = pygame.image.load("Assets/heart.png")
        x = self.screen_rect.centerx - 65
        y = 65
        return Image(self, image, x, y)
    
    def _prep_ship_left(self):
        """ Return an instance of ship left text """
        msg = (f"x {str(self.game_stats.ship_left)}")
        x = self.screen_rect.centerx
        y = 65
        return Text(self, msg, x, y, 48)
    
    def _prep_difficulty_text(self):
        """ Return an instance of text (difficulty) """
        diff_x = self.settings.screen_width * (1/2)
        diff_y = self.settings.screen_height * (1/3) - 50
        msg = "Difficulty"
        return Text(self, msg, diff_x, diff_y, 30)
    
    def _prep_bg_image(self):
        """ Return an instance of bg image """
        image = pygame.image.load("Assets/background.bmp")
        x, y = self.screen_rect.center
        return Image(self, image, x, y)

# Mouse events
    def _click_setting(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.settings_button.rect.collidepoint(mouse_pos) and self.mainmenu:
            self.setting_switch = True
            self.mainmenu = False
            self.click_sound.play()
            self.setting_menu()
    
    def _click_exit(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.exit_button.rect.collidepoint(mouse_pos) and self.mainmenu:
            self.click_sound.play()
            sys.exit()
    
    def _click_next(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.next_button.rect.collidepoint(mouse_pos) and self.setting_switch:
            self.click_sound.play()
            self.settings.increase_diff()
    
    def _click_prev(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.prev_botton.rect.collidepoint(mouse_pos) and self.setting_switch:
            self.click_sound.play()
            self.settings.decrease_diff()
    
    def _click_back(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.back_button.rect.collidepoint(mouse_pos) and self.setting_switch:
            self.click_sound.play()
            self.mainmenu = True
            self.setting_switch = False
    
    def _click_play(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.rect.collidepoint(mouse_pos) and self.mainmenu:
            self.click_sound.play()
            self._restart_diff()
            self.game_stats.reset_stats()
            self.game_stats.load_statistics()
            self.ship.center_ship()
            self.ship_left_text.msg = (f"x {self.game_stats.ship_left}")
            self.ship_left_text.prep_msg()
            self.alien_bullets.empty()
            self.aliens.empty()
            self.bullets.empty()
            self.play_switch = True
            self.mainmenu = False
            self.main_game()
    
    def _click_resume(self):
        mousep_pos = pygame.mouse.get_pos()
        if self.pause_button.rect.collidepoint(mousep_pos) and self.pause_switch:
            self.click_sound.play()
            if self.pause_switch == True:
                self.pause_switch = False
            else:
                self.pause_switch = True
    
    def _click_exit_main_menu(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.exit_main_menu_button.rect.collidepoint(mouse_pos) and self.pause_switch:
            self.pause_switch = False
            self.game_stats.save_statistics()
            self.game_stats.reset_stats()
            self.click_sound.play()
            self.alien_bullets.empty()
            self.aliens.empty()
            self.bullets.empty()
            self.mainmenu = True
            self.play_switch = False
            self.sb.prep_score()
            self.sb.prep_highscore()
    
    def _click_restart(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.restart_button.rect.collidepoint(mouse_pos) and self.game_stats.ship_left < 1:
            self._restart_diff()
            self.click_sound.play()
            if self.game_stats.score >= self.game_stats.high_score:
                self.game_stats.save_statistics()
            self.game_stats.reset_stats()
            self.game_stats.load_statistics()
            self.alien_bullets.empty()
            self.aliens.empty()
            self.bullets.empty()
            self.ship.center_ship()
            self.sb.prep_score()
            self.sb.prep_highscore()
            self.ship_left_text.msg = (f"x {self.game_stats.ship_left}")
            self.ship_left_text.prep_msg()
            
# Aliens
    def _add_alien(self):
        if len(self.aliens) < self.settings.aliens_allowed:
            alien = Alien(self)
            self.aliens.add(alien)
    
    def _update_alien(self):
        for alien in self.aliens.sprites():
            if alien.check_edges_x():
                alien.speed_x *= -1
                alien.update()
            elif alien.check_edges_y():
                alien.speed_y *= -1
                alien.update()
            else:
                alien.update()
    # Alien Bullet
    def _add_bullet(self):
        if len(self.alien_bullets) < self.settings.alien_bullet_allowed:
            for alien in self.aliens.sprites():
                new_bullet = AlienBullet(self,alien.rect.midbottom)
                if self._sensor_collide(alien):
                    self.shoot_sound.play()
                    self.alien_bullets.add(new_bullet)
    
    def _sensor_collide(self, alien):
        if (alien.sensor_rect_left.colliderect(self.ship.rect) or
                 alien.sensor_rect_right.colliderect(self.ship.rect)):
            return True

    def _draw_alien_bullet(self):
        for bullet in self.alien_bullets.sprites():
            bullet.draw_bullet()
    
    def _update_alien_bullets(self):
        self.alien_bullets.update()
        for bullet in self.alien_bullets.copy():
            if bullet.rect.top >= self.screen_rect.bottom:
                self.alien_bullets.remove(bullet)
    # Alien sensor
    def _draw_alien_sensor(self):
        for alien in self.aliens.sprites():
            alien.draw_sensor()
    
    def _update_sensor(self):
        for alien in self.aliens.sprites():
            alien.update_sensor()

# Bullets
    def _draw_bullet(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _fire_bullet(self):
        """ Event for firing bullets """
        if len(self.bullets) < self.settings.bllt_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Refactored for updateting bullets """
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= self.screen_rect.top:
                self.bullets.remove(bullet)
        self._check_bullet_collision() 
    
    def _check_bullet_collision(self):
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if collision:
            self.explosion_sound.play()
            self.game_stats.alien_destroyed += 1
            self.game_stats.score += self.settings.alien_points
            self.sb.stats.score = self.game_stats.score
            self.sb.prep_score()
            self._check_high_score()
            if self.game_stats.alien_destroyed == 5:
                self._increase_diff()
                self.game_stats.alien_destroyed = 0

# Ship
    def _ship_hit(self):
        if self.settings.ship_left > 0:
            self.explosion_sound.play()
            self.game_stats.ship_left -= 1
            self.ship_left_text.msg = (f"x {self.game_stats.ship_left}")
            self.ship_left_text.prep_msg()
            self.aliens.empty()
            self.alien_bullets.empty()
            self.bullets.empty()
            self.ship.center_ship()
            sleep(0.5)
        else:
            pass
    
    def _check_ship_collision(self):
        return pygame.sprite.spritecollideany(self.ship, self.aliens)
    
    def _check_alien_bullet_collision(self):
        return pygame.sprite.spritecollideany(self.ship, self.alien_bullets)
# Score
    def _check_high_score(self):
        if self.game_stats.score > self.game_stats.high_score:
            self.game_stats.high_score = self.game_stats.score
# Game

    def _increase_diff(self):
        self.settings.ship_speed += .2
        self.settings.alien_speed += .2
        self.settings.alien_bllt_spd += .2
        self.settings.aliens_allowed += 1
        self.settings.alien_bullet_allowed += 1
        self.settings.alien_points += 2
        self.settings.bllt_speed += .2
    
    def _restart_diff(self):
        self.settings.ship_speed = 2
        self.settings.alien_speed = 1
        self.settings.alien_bllt_spd = 1.5
        self.settings.aliens_allowed = 2
        self.settings.alien_bullet_allowed = 2
        self.settings.alien_points = 5
        self.settings.bllt_speed = 1.5
        self.game_stats.alien_destroyed = 0

###########
# ------- #
###########
    def _check_print(self):
        pass
    
if __name__ == "__main__":
    game = MainMenu()
    game.main_menu()