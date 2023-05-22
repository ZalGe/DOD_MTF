import pygame
import random
pygame.init()

# Global Constants
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_info = pygame.display.Info()
SCREEN_WIDTH = SCREEN_info.current_w
SCREEN_HEIGHT = SCREEN_info.current_h

RUNNING = [pygame.image.load("Games/Images/Dino_Chrome/DinoRun1.png"),
           pygame.image.load("Games/Images/Dino_Chrome/DinoRun2.png")]
JUMPING = pygame.image.load("Games/Images/Dino_Chrome/DinoJump.png")
DUCKING = [pygame.image.load("Games/Images/Dino_Chrome/DinoDuck1.png"),
           pygame.image.load("Games/Images/Dino_Chrome/DinoDuck2.png")]

SMALL_CACTUS = [pygame.image.load("Games/Images/Dino_Chrome/SmallCactus1.png"),
                pygame.image.load("Games/Images/Dino_Chrome/SmallCactus2.png"),
                pygame.image.load("Games/Images/Dino_Chrome/SmallCactus3.png")]
LARGE_CACTUS = [pygame.image.load("Games/Images/Dino_Chrome/LargeCactus1.png"),
                pygame.image.load("Games/Images/Dino_Chrome/LargeCactus2.png"),
                pygame.image.load("Games/Images/Dino_Chrome/LargeCactus3.png")]

BIRD = [pygame.image.load("Games/Images/Dino_Chrome/Bird1.png"),
        pygame.image.load("Games/Images/Dino_Chrome/Bird2.png")]

CLOUD = pygame.image.load("Games/Images/Dino_Chrome/Cloud.png")

BG = pygame.image.load("Games/Images/Dino_Chrome/Track.png")


class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput, start_menu, p, t):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] or userInput[pygame.K_w] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] or userInput[pygame.K_s] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN] or userInput[pygame.K_s]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

        if userInput[pygame.K_p]:
            p.pause(start_menu, t)

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1


def main(start_menu, p, t):
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput, start_menu, p, t)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count, start_menu, p, t)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count, start_menu, p, t):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text1 = font.render("Press SPACE Key to Start", True, (0, 0, 0))
            text2 = font.render("Press M Key to return to Start menu", True, (0, 0, 0))
            text3 = font.render("Press Q Key to Quit", True, (0, 0, 0))
        elif death_count > 0:
            text1 = font.render("Press SPACE Key to Restart", True, (0, 0, 0))
            text2 = font.render("Press M Key to return to Start menu", True, (0, 0, 0))
            text3 = font.render("Press Q Key to Quit", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            SCREEN.blit(score, (SCREEN_WIDTH / 2 - score.get_width() / 2, SCREEN_HEIGHT / 2 + 4 * score.get_height()))
        SCREEN.blit(text1, (SCREEN_WIDTH / 2 - text1.get_width() / 2, SCREEN_HEIGHT / 2 - text1.get_height()))
        SCREEN.blit(text2, (SCREEN_WIDTH / 2 - text2.get_width() / 2, SCREEN_HEIGHT / 2 + text2.get_height()))
        SCREEN.blit(text3, (SCREEN_WIDTH / 2 - text3.get_width() / 2, SCREEN_HEIGHT / 2 + 2 * text3.get_height()))
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main(start_menu, p, t)
                if event.key == pygame.K_m:
                    start_menu()
                if event.key == pygame.K_q:
                    raise SystemExit


def play_dino_chrome(start_menu, p, t):
    menu(0, start_menu, p, t)
    