import random
from settings import *


class MenuSnake:

    def __init__(self):

        self.body = []

        self.length = 18

        self.direction = "RIGHT"

        start_x = -BLOCK_SIZE * self.length
        start_y = random.randrange(
            120,
            HEIGHT - 120,
            BLOCK_SIZE
        )

        for i in range(self.length):

            self.body.append(
                (
                    start_x - i * BLOCK_SIZE,
                    start_y
                )
            )

    def update(self):

        head_x, head_y = self.body[0]

        if self.direction == "RIGHT":
            new_head = (head_x + BLOCK_SIZE, head_y)

        self.body.insert(0, new_head)

        self.body.pop()

        if head_x > WIDTH + BLOCK_SIZE * self.length:

            start_y = random.randrange(
                120,
                HEIGHT - 120,
                BLOCK_SIZE
            )

            self.body.clear()

            start_x = -BLOCK_SIZE * self.length

            for i in range(self.length):

                self.body.append(
                    (
                        start_x - i * BLOCK_SIZE,
                        start_y
                    )
                )