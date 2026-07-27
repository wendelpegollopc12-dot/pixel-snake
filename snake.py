from settings import *

class Snake:

    def __init__(self):

        self.body = [
            (200, 200),
            (180, 200),
            (160, 200)
        ]

        self.direction = "RIGHT"

        self.grow = False

    def move(self):

        head_x, head_y = self.body[0]

        if self.direction == "UP":
            head_y -= BLOCK_SIZE

        elif self.direction == "DOWN":
            head_y += BLOCK_SIZE

        elif self.direction == "LEFT":
            head_x -= BLOCK_SIZE

        elif self.direction == "RIGHT":
            head_x += BLOCK_SIZE

        # Screen Wrap
        if head_x < 0:
            head_x = WIDTH - BLOCK_SIZE

        elif head_x >= WIDTH:
            head_x = 0

        if head_y < 0:
            head_y = HEIGHT - BLOCK_SIZE

        elif head_y >= HEIGHT:
            head_y = 0

        new_head = (head_x, head_y)

        self.body.insert(0, new_head)

        if self.grow:
            self.grow = False
        else:
            self.body.pop()