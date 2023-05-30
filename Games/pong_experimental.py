import pygame

from Functionality.timer import Timer

pygame.init()

t = Timer

# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf', 20)

# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Basic parameters of the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_info = pygame.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h

pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 30


# Striker class
class Striker:
    # Take the initial position, dimensions, speed and color of the object
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        # Rect that is used to control the position and collision of the object
        self.Rect = pygame.Rect(posx, posy, width, height)
        # Object that is blit on the screen
        self.geek = pygame.draw.rect(screen, self.color, self.Rect)

    # Used to display the object on the screen
    def display(self):
        self.geek = pygame.draw.rect(screen, self.color, self.Rect)

    def update(self, y_fac):
        self.posy = self.posy + self.speed * y_fac

        # Restricting the striker to be below the top surface of the screen
        if self.posy <= 0:
            self.posy = 0
        # Restricting the striker to be above the bottom surface of the screen
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height

        # Updating the rect with the new values
        self.Rect = (self.posx, self.posy, self.width, self.height)

    def display_score(self, text, score, x, y, color):
        text = font20.render(text + str(score), True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)

        screen.blit(text, text_rect)

    def get_rect(self):
        return self.Rect


# Ball class
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1

    def display(self):
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac

        # If the ball hits the top or bottom surfaces,
        # then the sign of y_fac is changed, and
        # it results in a reflection
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1

        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xFac *= -1
        self.firstTime = 1

    # Used to reflect the ball along the X-axis
    def hit(self):
        self.xFac *= -1

    def get_rect(self):
        return self.ball


def show_winner(p1_score, p2_score, t):
    if p1_score == 10 or p2_score == 10:
        winner = ""
        font20v2 = pygame.font.Font('freesansbold.ttf', 30)

        if p1_score == 10:
            winner = "Player1"
        elif p2_score == 10:
            winner = "Player2"

        screen.fill(BLACK)

        label1 = font20v2.render(f"Winner is {winner}", True, WHITE)
        label2 = font20v2.render("Press SPACE to play again!", True, WHITE)
        # label3 = font20v2.render("Press M to return to main menu!", True, WHITE)
        label4 = font20v2.render("Press Q to quit!", True, WHITE)

        screen.blit(label1, (WIDTH / 2 - label1.get_width() / 2, HEIGHT / 2 - label1.get_height()))
        screen.blit(label2, (WIDTH / 2 - label2.get_width() / 2, HEIGHT / 2 + label2.get_height()))
        # screen.blit(label3, (WIDTH / 2 - label3.get_width() / 2, HEIGHT / 2 + 2 * label3.get_height() + 10))
        screen.blit(label4, (WIDTH / 2 - label4.get_width() / 2, HEIGHT / 2 + 3 * label4.get_height() + 20))

        pygame.display.flip()

        # event loop
        while True:
            for event in pygame.event.get():
                # exit conditions --> windows titlebar x click
                if event.type == pygame.QUIT:
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        play_pong()
                    if event.key == pygame.K_q:
                        raise SystemExit
                    # if event.key == pygame.K_m:
                    #     start_menu()


# Game Manager
def play_pong():
    # Defining the objects
    player1 = Striker(20, HEIGHT // 2 - 50, 10, 100, 10, GREEN)
    player2 = Striker(WIDTH - 30, HEIGHT // 2 - 50, 10, 100, 10, GREEN)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

    list_of_players = [player1, player2]

    # Initial parameters of the players
    player1_score, player2_score = 0, 0
    player1_y_fac, player2_y_fac = 0, 0

    t.start_timer()

    running = True
    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player2_y_fac = -1
                if event.key == pygame.K_DOWN:
                    player2_y_fac = 1
                if event.key == pygame.K_w:
                    player1_y_fac = -1
                if event.key == pygame.K_s:
                    player1_y_fac = 1
                # if event.key == pygame.K_p:
                #     p.pause(start_menu, t)
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    player2_y_fac = 0
                if event.key in (pygame.K_w, pygame.K_s):
                    player1_y_fac = 0

        # Collision detection
        for player in list_of_players:
            if pygame.Rect.colliderect(ball.get_rect(), player.get_rect()):
                ball.hit()

        # Updating the objects
        player1.update(player1_y_fac)
        player2.update(player2_y_fac)
        point = ball.update()

        # -1 -> Player_1 has scored
        # +1 -> Player_2 has scored
        #  0 -> None of them scored
        if point == -1:
            player1_score += 1
        elif point == 1:
            player2_score += 1

        show_winner(player1_score, player2_score, t)

        # Someone has scored
        # a point and the ball is out of bounds.
        # So, we reset its position
        if point:
            ball.reset()

        # Displaying the objects on the screen
        player1.display()
        player2.display()
        ball.display()

        # Displaying the scores of the players
        player1.display_score("Player 1 : ",
                              player1_score, 100, 20, WHITE)
        player2.display_score("Player 2 : ",
                              player2_score, WIDTH - 100, 20, WHITE)

        pygame.display.update()
        clock.tick(FPS)


play_pong()
