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
                WHITE
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
                    if self.selected == 2:
                        self.difficulty -= 1

                        if self.difficulty < 0:
                            self.difficulty = 2

                        import settings

                        if self.difficulty == 0:
                            settings.MOVE_SPEED = 12

                        elif self.difficulty == 1:
                            settings.MOVE_SPEED = 8

                        else:
                            settings.MOVE_SPEED = 5

                        self.select_sound.play()

                    elif self.selected == 3:

                        self.skin_selected -= 1

                        if self.skin_selected < 0:
                            self.skin_selected = len(self.skin_names) - 1

                        import settings

                        settings.CURRENT_SKIN = self.skin_names[
                            self.skin_selected
                        ]

                        self.select_sound.play()

                elif event.key == pygame.K_RIGHT:

                    if self.selected == 2:

                        self.difficulty += 1

                        if self.difficulty > 2:
                            self.difficulty = 0

                        import settings
                                                    
                        if self.difficulty == 0:
                            settings.MOVE_SPEED = 12

                        elif self.difficulty == 1:
                            settings.MOVE_SPEED = 8

                        else:
                            settings.MOVE_SPEED = 5

                        self.select_sound.play()

                    elif self.selected == 3:

                        self.skin_selected += 1

                        if self.skin_selected >= len(self.skin_names):
                            self.skin_selected = 0

                        import settings

                        settings.CURRENT_SKIN = self.skin_names[
                            self.skin_selected
                        ]

                        self.select_sound.play()

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

                        pass

                    #SKIN
                    elif self.selected == 3:

                        pass

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
                option = f"DIFFICULTY : {self.difficulties[self.difficulty]}"

            if option == "SKIN":
                option = f"SKIN : {self.skin_names[self.skin_selected]}"

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