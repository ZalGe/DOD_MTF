import pygame
import pygame_menu
from typing import Tuple, Any
from Functionality.pause_menu import PauseMenu
from Functionality.timer import Timer, pygame
from Games.pong import play_pong
from Games.flappy import play_flappy
from Games.dino_chrome import play_dino_chrome


pygame.init()


class GetSetGame:
    def __init__(self):
        self._game = 0

    def set_game(self, game):
        self._game = game

    def get_game(self):
        return self._game


def game_choice(selected: Tuple, value: Any, gs_game: GetSetGame):
    if isinstance(value, int):
        print(value)
        gs_game.set_game(value)
    else:
        pygame.quit()


def game_start(gs: GetSetGame, p: PauseMenu, t: Timer):
    if gs.get_game() == 1:
        print("play")
        play_pong(start_menu, p, t)

    elif gs.get_game() == 2:
        print("play")
        play_flappy(start_menu, p, t)

    elif gs.get_game() == 3:
        play_dino_chrome(start_menu, p, t)


def start_menu():
    surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_info = pygame.display.Info()
    Width = screen_info.current_w
    Height = screen_info.current_h

    gs = GetSetGame()
    p = PauseMenu(Width, Height)
    t = Timer(Width, Height)

    menu = pygame_menu.Menu('Welcome to MTF STU', Width, Height, theme=pygame_menu.themes.THEME_DARK)
    gs.set_game(1)

    menu.add.selector('Select Game :', [('Pong', 1), ('Flappy Bird', 2), ('Chrome Dinosaur', 3)],
                      onchange=lambda selected, value: game_choice(selected, value, gs))
    menu.add.button('Play', lambda: game_start(gs, p, t))
    menu.add.button('Leaderboard')
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)


def start():
    start_menu()
