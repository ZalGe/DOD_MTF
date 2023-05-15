import pygame


class PauseMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = (255, 255, 255)

    def pause(self, start_menu, t):
        running = True

        screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        pygame.display.set_caption("Pause")
        # pick a font you have and set its size
        myfont = pygame.font.SysFont("Comic Sans MS", 30)
        # apply it to text on a label1
        label1 = myfont.render("Game is paused!", True, self.color)
        label2 = myfont.render("Press SPACE to continue!", True, self.color)
        label3 = myfont.render("Press M to return to main menu!", True, self.color)
        label4 = myfont.render("Press Q to quit!", True, self.color)
        # put the label1 object on the screen at point x=100, y=100
        screen.blit(label1, (self.width / 2 - label1.get_width() / 2, self.height / 2 - label1.get_height()))
        screen.blit(label2, (self.width / 2 - label2.get_width() / 2, self.height / 2 + label2.get_height()))
        screen.blit(label3, (self.width / 2 - label3.get_width() / 2, self.height / 2 + 2 * label3.get_height()))
        screen.blit(label4, (self.width / 2 - label4.get_width() / 2, self.height / 2 + 3 * label4.get_height()))
        # show the whole thing
        pygame.display.flip()

        # event loop
        while running:
            for event in pygame.event.get():
                # exit conditions --> windows titlebar x click
                if event.type == pygame.QUIT:
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False
                        t.start_timer()
                    if event.key == pygame.K_q:
                        raise SystemExit
                    if event.key == pygame.K_m:
                        start_menu()
