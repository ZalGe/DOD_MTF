import pygame

from Functionality.pause_menu import PauseMenu
from Functionality.timer import Timer
from Functionality.start_menu import start_menu

screen_info = pygame.display.Info()
_width = screen_info.current_w
_height = screen_info.current_h

p = PauseMenu(_width, _height)
t = Timer(_width, _height)
