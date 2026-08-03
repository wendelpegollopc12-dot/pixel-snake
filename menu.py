import pygame
import os

from settings import *
from game import Game
from menu_snake import MenuSnake


class Menu:

    def __init__(self):

        pygame.init()

        pygame.mixer.init()

        pygame.mixer.music.load("assets/music/menu.mp3")
        pygame.mixer.music.set_volume(0.35)
        pygame.mixer.music.play(-1)

        self.start_sound = pygame.mixer.Sound(
            "assets/sounds/start.wav"
        )
        self.start_sound.set_volume(0.7)

        self.select_sound = pygame.mixer.Sound(
            "assets/sounds/select.wav"
        )

        self.select_sound.set_volume(0.5)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        self.options = [
            "START GAME",
            "HIGH SCORE",
            "DIFFICULTY",
            "SKIN",
            "EXIT"
        ]

        self.selected = 0

        self.difficulties = ["EASY", "MEDIUM", "HARD"]
        self.difficulty = 1

        self.skin_names = [
            "DEFAULT",
            "BLUE",
            "PINK",
            "VIOLET",
            "GOLD"
        ]

        self.skin_selected = 0

        self.menu_snake = MenuSnake()

        self.title_font = pygame.font.Font(
            "assets/fonts/PressStart2P-Regular.ttf",
            36
        )

        self.font = pygame.font.Font(
            "assets/fonts/PressStart2P-Regular.ttf",
            18
        )

    def run(self):

        self.running = True

        while self.running:

            self.events()

            self.menu_snake.update()

            self.draw()

            self.clock.tick(FPS)

    def load_high_score(self):

        if not os.path.exists("highscore.txt"):

             with open("highscore.txt", "w") as file:
                file.write("0")

        with open("highscore.txt", "r") as file:
            return int(file.read())

    def high_score_screen(self):

        high_score = self.load_high_score()

        viewing = True

        while viewing:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:

                        viewing = False

            self.screen.fill((12, 16, 32))

            title = self.title_font.render(
                "HIGH SCORE",
                True,
                (255,255,0)
            )

            score = self.title_font.render(
                str(high_score).zfill(3),
                True,
                WHITE
            )

            info = self.font.render(
                "PRESS ESC TO RETURN",
                True,
                (170, 170, 170)
            )

            self.screen.blit(
                title,
                (
                    WIDTH//2-title.get_width()//2,
                    120
                )
            )

            self.screen.blit(
                score,
                (
                    WIDTH//2-score.get_width()//2,
                    260
                )
            )

            self.screen.blit(
                info,
                (
                    WIDTH//2-info.get_width()//2,
                    520
                )
            )

            pygame.display.flip()

            self.clock.tick(FPS)


    def difficulty_screen(self):

        viewing = True

        while viewing:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    raise SystemExit

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:

                        self.difficulty -= 1

                        if self.difficulty < 0:
                            self.difficulty = len(
                                self.difficulties
                            ) - 1

                        self.select_sound.play()

                    elif event.key == pygame.K_DOWN:

                        self.difficulty += 1

                        if self.difficulty >= len(
                            self.difficulties
                        ):
                            self.difficulty = 0

                        self.select_sound.play()

                    elif event.key == pygame.K_RETURN:

                        import settings

                        if self.difficulty == 0:
                            settings.DIFFICULTY = "EASY"
                            settings.MOVE_SPEED = 12

                        elif self.difficulty == 1:
                            settings.DIFFICULTY = "MEDIUM"
                            settings.MOVE_SPEED = 8

                        else:
                            settings.DIFFICULTY = "HARD"
                            settings.MOVE_SPEED = 5

                        self.select_sound.play()

                        viewing = False

                    elif event.key == pygame.K_ESCAPE:

                        viewing = False

            self.screen.fill((12, 16, 32))

            title = self.title_font.render(
                "DIFFICULTY",
                True,
                (255, 255, 0)
            )

            self.screen.blit(
                title,
                (
                    WIDTH // 2 -
                    title.get_width() // 2,
                    100
                )
            )

            start_y = 220

            difficulty_colors = [
                (80, 255, 140),
                (255, 255, 0),
                (255, 80, 80)
            ]

            for i, difficulty in enumerate(
                self.difficulties
            ):

                y = start_y + i * 70

                if i == self.difficulty:

                    pygame.draw.rect(
                        self.screen,
                        (45, 45, 65),
                        (
                            WIDTH // 2 - 230,
                            y - 15,
                            460,
                            55
                        ),
                        border_radius=6
                    )

                    pygame.draw.rect(
                        self.screen,
                        (255, 255, 0),
                        (
                            WIDTH // 2 - 230,
                            y - 15,
                            460,
                            55
                        ),
                        2,
                        border_radius=6
                    )

                text = self.font.render(
                    difficulty,
                    True,
                    difficulty_colors[i]
                    if i == self.difficulty
                    else WHITE
                )

                self.screen.blit(
                    text,
                    (
                        WIDTH // 2 -
                        text.get_width() // 2,
                        y
                    )
                )

            info = self.font.render(
                "UP / DOWN = SELECT",
                True,
                (170, 170, 170)
            )

            self.screen.blit(
                info,
                (
                    WIDTH // 2 -
                    info.get_width() // 2,
                    HEIGHT - 85
                )
            )

            info2 = self.font.render(
                "ENTER = SELECT   ESC = BACK",
                True,
                (170, 170, 170)
            )

            self.screen.blit(
                info2,
                (
                    WIDTH // 2 -
                    info2.get_width() // 2,
                    HEIGHT - 50
                )
            )

            pygame.display.flip()

            self.clock.tick(FPS)

    def skin_screen(self):

        viewing = True

        while viewing:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    raise SystemExit

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:

                        self.skin_selected -= 1

                        if self.skin_selected < 0:
                            self.skin_selected = len(
                                self.skin_names
                            ) - 1

                        self.select_sound.play()

                    elif event.key == pygame.K_DOWN:

                        self.skin_selected += 1

                        if self.skin_selected >= len(
                            self.skin_names
                        ):
                            self.skin_selected = 0

                        self.select_sound.play()

                    elif event.key == pygame.K_RETURN:

                        import settings

                        settings.CURRENT_SKIN = self.skin_names[
                            self.skin_selected
                        ]

                        self.select_sound.play()

                        viewing = False

                    elif event.key == pygame.K_ESCAPE:

                        viewing = False

            self.screen.fill((12, 16, 32))

            title = self.title_font.render(
                "SELECT SKIN",
                True,
                (255, 255, 0)
            )

            self.screen.blit(
                title,
                (
                    WIDTH // 2 -
                    title.get_width() // 2,
                    70
                )
            )

            skin_colors = {
                "DEFAULT": (
                    GREEN,
                    (60, 255, 170),
                    (180, 255, 220)
                ),
                "BLUE": (
                    (60, 140, 255),
                    (100, 180, 255),
                    (180, 220, 255)
                ),
                "PINK": (
                    (255, 105, 180),
                    (255, 160, 210),
                    (255, 200, 230)
                ),
                "VIOLET": (
                    (160, 80, 255),
                    (200, 140, 255),
                    (220, 190, 255)
                ),
                "GOLD": (
                    (255, 190, 40),
                    (255, 220, 100),
                    (255, 240, 170)
                )
            }

            start_y = 150

            for i, skin in enumerate(self.skin_names):

                snake_color, snake_glow, snake_highlight = (
                    skin_colors[skin]
                )

                y = start_y + i * 65

                if i == self.skin_selected:

                    pygame.draw.rect(
                        self.screen,
                        (45, 45, 65),
                        (
                            WIDTH // 2 - 230,
                            y - 15,
                            460,
                            55
                        ),
                        border_radius=6
                    )

                    pygame.draw.rect(
                        self.screen,
                        (255, 255, 0),
                        (
                            WIDTH // 2 - 230,
                            y - 15,
                            460,
                            55
                        ),
                        2,
                        border_radius=6
                    )

                # Preview snake: separate pixel blocks
                preview_x = WIDTH // 2 - 175

                for segment in range(5):

                    x = preview_x + segment * BLOCK_SIZE

                    pygame.draw.rect(
                        self.screen,
                        snake_glow,
                        (
                            x - 2,
                            y - 2,
                            BLOCK_SIZE + 4,
                            BLOCK_SIZE + 4
                        ),
                        border_radius=5
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
                        border_radius=3
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

                text = self.font.render(
                    skin,
                    True,
                    (
                        255,
                        255,
                        0
                    ) if i == self.skin_selected else WHITE
                )

                self.screen.blit(
                    text,
                    (
                        WIDTH // 2 + 5,
                        y + 2
                    )
                )

            info = self.font.render(
                "UP / DOWN = SELECT",
                True,
                (170, 170, 170)
            )

            self.screen.blit(
                info,
                (
                    WIDTH // 2 -
                    info.get_width() // 2,
                    HEIGHT - 85
                )
            )

            info2 = self.font.render(
                "ENTER = SELECT   ESC = BACK",
                True,
                (170, 170, 170)
            )

            self.screen.blit(
                info2,
                (
                    WIDTH // 2 -
                    info2.get_width() // 2,
                    HEIGHT - 50
                )
            )

            pygame.display.flip()

            self.clock.tick(FPS)

    def events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:

                    self.selected -= 1

                    if self.selected < 0:
                        self.selected = len(self.options) - 1

                    self.select_sound.play()

                elif event.key == pygame.K_DOWN:

                    self.selected += 1

                    if self.selected >= len(self.options):
                        self.selected = 0

                    self.select_sound.play()
                
                elif event.key == pygame.K_LEFT:

                    pass

                elif event.key == pygame.K_RIGHT:

                    pass

                elif event.key == pygame.K_RETURN:

                    # START GAME
                    if self.selected == 0:

                        self.start_sound.play()

                        pygame.time.wait(250)

                        pygame.mixer.music.stop()

                        game = Game()
                        game.run()

                        pygame.mixer.music.play(-1)

                    # HIGH SCORE
                    elif self.selected == 1:

                        self.high_score_screen()

                    # DIFFICULTY
                    elif self.selected == 2:

                        self.difficulty_screen()

                    # SKIN
                    elif self.selected == 3:

                        self.skin_screen()

                    # EXIT
                    elif self.selected == 4:

                        pygame.quit()
                        raise SystemExit

                elif event.key == pygame.K_ESCAPE:

                    pygame.quit()
                    raise SystemExit

    def draw(self):

        self.screen.fill((12, 16, 32))

        for x, y in self.menu_snake.body:

            pygame.draw.rect(
                self.screen,
                (40, 180, 120),
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
                GREEN,
                (
                    x,
                    y,
                    BLOCK_SIZE,
                    BLOCK_SIZE
                ),
                border_radius=4
            )

            head_x, head_y = self.menu_snake.body[0]

            pygame.draw.circle(
                self.screen,
                WHITE,
                (head_x + 6, head_y + 6),
                2
            )

            pygame.draw.circle(
                self.screen,
                WHITE,
                (head_x + 14, head_y + 6),
                2
            )

            pygame.draw.circle(
                self.screen,
                (0, 0, 0),
                (head_x + 6, head_y + 6),
                1
            )

            pygame.draw.circle(
                self.screen,
                (0, 0, 0),
                (head_x + 14, head_y + 6),
                1
            )

        title = self.title_font.render(
            "PIXEL SNAKE",
            True,
            (255, 255, 0)
        )

        self.screen.blit(
            title,
            (
                WIDTH // 2 - title.get_width() // 2,
                90
            )
        )

        for i, option in enumerate(self.options):

            color = WHITE

            if i == self.selected:
                color = (255, 255, 0)

            if option == "DIFFICULTY":

                import settings

                option = f"DIFFICULTY : {settings.DIFFICULTY}"

            if option == "SKIN":

                import settings

                option = f"SKIN : {settings.CURRENT_SKIN}"

            text = self.font.render(
                option,
                True,
                color
            )

            self.screen.blit(
                text,
                (
                    WIDTH // 2 - text.get_width() // 2,
                    230 + i * 60
                )
            )

        info = self.font.render(
            "ARROWS = MOVE   ENTER = SELECT",
            True,
            (170, 170, 170)
        )

        self.screen.blit(
            info,
            (
                WIDTH // 2 - info.get_width() // 2,
                HEIGHT - 50
            )
        )

        pygame.display.flip()