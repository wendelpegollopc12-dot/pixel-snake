import pygame
import settings
import os

from settings import *
from snake import Snake
from apple import Apple


class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True
        self.game_over = False
        self.paused = False
        self.pause_selected = 0
        self.pause_options = ["RESUME", "QUIT TO MENU"]

        self.snake = Snake()
        self.apple = Apple()

        self.score = 0
        self.high_score = self.load_high_score()
        self.move_timer = 0

        self.font = pygame.font.Font(
            "assets/fonts/PressStart2P-Regular.ttf",
            16
        )

        self.big_font = pygame.font.Font(
            "assets/fonts/PressStart2P-Regular.ttf",
            34
        )

        self.gameover_sound = pygame.mixer.Sound(
            "assets/sounds/gameover.wav"
        )

        self.gameover_sound.set_volume(0.8)

        self.eat_sound = pygame.mixer.Sound(
            "assets/sounds/bite.wav"
        )

        self.eat_sound.set_volume(0.6)

    def reset_game(self):

        self.snake = Snake()
        self.apple = Apple()

        self.score = 0
        self.game_over = False

    def load_high_score(self):

        if not os.path.exists("highscore.txt"):

            with open("highscore.txt", "w") as file:
                file.write("0")

        with open("highscore.txt", "r") as file:

            return int(file.read())

    def save_high_score(self):

        with open("highscore.txt", "w") as file:

            file.write(str(self.high_score))

    def run(self):

        self.running = True

        while self.running:

            self.events()

            if not self.game_over and not self.paused:
                self.update()

            self.draw()

            self.clock.tick(FPS)

    def events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN:

                if self.game_over:

                    if event.key == pygame.K_r:
                        self.reset_game()

                    elif event.key == pygame.K_q:
                        self.running = False

                else:

                    if self.paused:

                        if event.key == pygame.K_UP:
                            self.pause_selected -= 1

                            if self.pause_selected < 0:
                                self.pause_selected = len(self.pause_options) - 1

                        elif event.key == pygame.K_DOWN:
                            self.pause_selected += 1

                            if self.pause_selected >= len(self.pause_options):
                                self.pause_selected = 0

                        elif event.key == pygame.K_RETURN:

                            if self.pause_selected == 0:
                                self.paused = False

                            else:
                                self.running = False

                        elif event.key == pygame.K_SPACE:
                            self.paused = False

                    elif event.key == pygame.K_SPACE:
                        self.paused = True
                        self.pause_selected = 0

                    elif event.key == pygame.K_UP and self.snake.direction != "DOWN":
                        self.snake.direction = "UP"

                    elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                        self.snake.direction = "DOWN"

                    elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                        self.snake.direction = "LEFT"

                    elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                        self.snake.direction = "RIGHT"

    def update(self):

        self.move_timer += 1

        if self.move_timer >= settings.MOVE_SPEED:

            self.snake.move()

            if self.snake.body[0] == self.apple.position:

                self.score += 1
                self.snake.grow = True
                self.eat_sound.play()
                self.apple.respawn()

            if self.snake.body[0] in self.snake.body[1:]:

                if self.score > self.high_score:

                    self.high_score = self.score
                    self.save_high_score()

                self.gameover_sound.play()

                self.game_over = True

            self.move_timer = 0

    def draw(self):

        # ==========================
        # BACKGROUND
        # ==========================

        self.screen.fill(BACKGROUND)

        # ==========================
        # APPLE
        # ==========================

        apple_x, apple_y = self.apple.position

        # Apple dark red outline

        pygame.draw.rect(
            self.screen,
            (120, 20, 20),
            (
                apple_x - 2,
                apple_y - 2,
                BLOCK_SIZE + 4,
                BLOCK_SIZE + 4
            ),
            border_radius=5
        )

        # Apple body

        pygame.draw.rect(
            self.screen,
            RED,
            (
                apple_x,
                apple_y,
                BLOCK_SIZE,
                BLOCK_SIZE
            ),
            border_radius=3
        )

        # Apple highlight

        pygame.draw.rect(
            self.screen,
            (255, 150, 150),
            (
                apple_x + 4,
                apple_y + 4,
                4,
                4
            )
        )

        # Apple stem

        pygame.draw.rect(
            self.screen,
            (90, 50, 20),
            (
                apple_x + BLOCK_SIZE // 2 - 1,
                apple_y - 4,
                3,
                5
            )
        )

        # ==========================
        # SNAKE
        # ==========================

        if settings.CURRENT_SKIN == "DEFAULT":

            snake_color = GREEN
            snake_glow = (60, 255, 170)
            snake_highlight = (180, 255, 220)

        elif settings.CURRENT_SKIN == "BLUE":

            snake_color = (60, 140, 255)
            snake_glow = (100, 180, 255)
            snake_highlight = (180, 220, 255)

        elif settings.CURRENT_SKIN == "PINK":

            snake_color = (255, 105, 180)
            snake_glow = (255, 160, 210)
            snake_highlight = (255, 200, 230)

        elif settings.CURRENT_SKIN == "VIOLET":

            snake_color = (160, 80, 255)
            snake_glow = (200, 140, 255)
            snake_highlight = (220, 190, 255)

        elif settings.CURRENT_SKIN == "GOLD":

            snake_color = (255, 190, 40)
            snake_glow = (255, 220, 100)
            snake_highlight = (255, 240, 170)

        else:

            snake_color = GREEN
            snake_glow = (60, 255, 170)
            snake_highlight = (180, 255, 220)

        for x, y in self.snake.body:

            pygame.draw.rect(
                self.screen,
                snake_glow,
                (
                    x - 2,
                    y - 2,
                    BLOCK_SIZE + 4,
                    BLOCK_SIZE + 4
                ),
                border_radius=6
            )

            pygame.draw.rect(
                self.screen,
                snake_color,
                (
                    x,
                    y,
                    BLOCK_SIZE,
                    BLOCK_SIZE
                ),
                border_radius=4
            )

            pygame.draw.rect(
                self.screen,
                snake_highlight,
                (
                    x + 3,
                    y + 3,
                    5,
                    5
                ),
                border_radius=2
            )

            if (x, y) == self.snake.body[0]:

                pygame.draw.circle(
                    self.screen,
                    WHITE,
                    (x + 6, y + 6),
                    2
                )

                pygame.draw.circle(
                    self.screen,
                    WHITE,
                    (x + 14, y + 6),
                    2
                )

                pygame.draw.circle(
                    self.screen,
                    (0, 0, 0),
                    (x + 6, y + 6),
                    1
                )

                pygame.draw.circle(
                    self.screen,
                    (0, 0, 0),
                    (x + 14, y + 6),
                    1
                )

        # ==========================
        # HUD
        # ==========================

        title = self.font.render(
            "PIXEL SNAKE",
            True,
            (255, 255, 0)
        )

        score = self.font.render(
            f"SCORE {self.score:03}",
            True,
            WHITE
        )

        high_score = self.font.render(
            f"BEST {self.high_score:03}",
            True,
            (255, 255, 0)
        )

        self.screen.blit(title, (15, 12))
        self.screen.blit(score, (15, 42))
        self.screen.blit(high_score, (15, 72))

        # ==========================
        # GAME OVER
        # ==========================

        if self.game_over:

            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(190)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))

            game_over = self.big_font.render(
                "GAME OVER",
                True,
                RED
            )

            score_text = self.font.render(
                f"FINAL SCORE {self.score:03}",
                True,
                WHITE
            )

            restart = self.font.render(
                "PRESS R",
                True,
                (255, 255, 0)
            )

            restart2 = self.font.render(
                "TO RESTART",
                True,
                (255, 255, 0)
            )

            menu_text = self.font.render(
                "PRESS Q",
                True,
                (60, 255, 170)
            )

            menu_text2 = self.font.render(
                "FOR MENU",
                True,
                (60, 255, 170)
            )

            self.screen.blit(
                game_over,
                (
                    WIDTH // 2 - game_over.get_width() // 2,
                    HEIGHT // 2 - 110
                )
            )

            self.screen.blit(
                score_text,
                (
                    WIDTH // 2 - score_text.get_width() // 2,
                    HEIGHT // 2 - 35
                )
            )

            self.screen.blit(
                restart,
                (
                    WIDTH // 2 - restart.get_width() // 2,
                    HEIGHT // 2 + 25
                )
            )

            self.screen.blit(
                restart2,
                (
                    WIDTH // 2 - restart2.get_width() // 2,
                    HEIGHT // 2 + 50
                )
            )

            self.screen.blit(
                menu_text,
                (
                    WIDTH // 2 - menu_text.get_width() // 2,
                    HEIGHT // 2 + 90
                )
            )

            self.screen.blit(
                menu_text2,
                (
                    WIDTH // 2 - menu_text2.get_width() // 2,
                    HEIGHT // 2 + 115
                )
            )

        # ==========================
        # PAUSE SCREEN
        # ==========================

        if self.paused:

            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(190)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))

            paused = self.big_font.render(
                "PAUSED",
                True,
                (255, 255, 0)
            )

            self.screen.blit(
                paused,
                (
                    WIDTH // 2 - paused.get_width() // 2,
                    HEIGHT // 2 - 125
                )
            )

            for i, option in enumerate(self.pause_options):

                color = WHITE

                if i == self.pause_selected:
                    color = (255, 255, 0)

                text = self.font.render(
                    option,
                    True,
                    color
                )

                self.screen.blit(
                    text,
                    (
                        WIDTH // 2 - text.get_width() // 2,
                        HEIGHT // 2 - 35 + i * 55
                    )
                )

            controls = self.font.render(
                "ARROWS = MOVE   ENTER = SELECT",
                True,
                (150, 150, 150)
            )

            self.screen.blit(
                controls,
                (
                    WIDTH // 2 - controls.get_width() // 2,
                    HEIGHT - 55
                )
            )

        pygame.display.flip()