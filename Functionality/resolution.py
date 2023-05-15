import pygame
import os


def get_screen_resolution():
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # You have to call this before pygame.init()

    pygame.init()

    info = pygame.display.Info()  # You have to call this before pygame.display.set_mode()
    var = info.current_w, info.current_h
