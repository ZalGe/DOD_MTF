import pygame
import time


class Timer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = (255, 255, 255)

    def start_timer(self):
        myfont = pygame.font.SysFont("Comic Sans MS", 30)
        num = 3

        for i in range(3):
            # apply it to text on a label1
            screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
            label1 = myfont.render(str(num), True, self.color)
            screen.blit(label1, (self.width / 2 - label1.get_width() / 2, self.height / 2 - label1.get_height() / 2))
            pygame.display.update()
            num = num - 1
            time.sleep(1)
