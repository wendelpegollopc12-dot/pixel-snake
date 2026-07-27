import pygame

from settings import *
from game import Game


class Menu:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        self.options = [
            "START GAME",
            "HIGH SCORE",
            "SETTINGS",
            "EXIT"
        ]

        self.selected = 0

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

                elif event.key == pygame.K_RETURN:

                    # START GAME
                    if self.selected == 0:

                        game = Game()
                        game.run()

                    # HIGH SCORE
                    elif self.selected == 1:

                        print("High Score Menu Coming Soon")

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

        self.screen.fill((28, 48, 22))

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