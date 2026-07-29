import pygame
import os

from settings import *
from game import Game


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

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        self.options = [
            "START GAME",
            "HIGH SCORE",
            "DIFFICULTY",
            "EXIT"
        ]

        self.selected = 0

        self.difficulties = ["EASY", "MEDIUM", "HARD"]
        self.difficulty = 1

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

                elif event.key == pygame.K_DOWN:

                    self.selected += 1

                    if self.selected >= len(self.options):
                        self.selected = 0
                
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

                    # SETTINGS
                    elif self.selected == 2:

                        print("Settings Menu Coming Soon")

                    # EXIT
                    elif self.selected == 3:

                        pygame.quit()
                        raise SystemExit

                elif event.key == pygame.K_ESCAPE:

                    pygame.quit()
                    raise SystemExit

    def draw(self):

        self.screen.fill((12, 16, 32))

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