import sys
import pygame
from setting import Settings
from ship import Ship
import game_funcion as gf
def run_game():
    # Инициализирует игру и создает объект экрана.
    bg_color = (230, 230, 230)
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)

    
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
run_game()