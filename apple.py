import random

from settings import *

class Apple:

    def __init__(self):

        self.position = (
            random.randrange(0, WIDTH, BLOCK_SIZE),
            random.randrange(0, HEIGHT, BLOCK_SIZE)
        )

    def respawn(self):

        self.position = (
            random.randrange(0, WIDTH, BLOCK_SIZE),
            random.randrange(0, HEIGHT, BLOCK_SIZE)
        )