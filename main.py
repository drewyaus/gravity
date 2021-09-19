# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import pygame
import random
import math

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

CLOCK = pygame.time.Clock()

SCREEN = pygame.display.set_mode((900, 600), 0, 32)
MARGIN_SIZE = 100

BALL_SIZE = 20
BALL_RADIUS = pygame.math.Vector2(math.sqrt(BALL_SIZE), math.sqrt(BALL_SIZE))
BALL_DIAMETER = (2 * BALL_RADIUS.magnitude(), 2 * BALL_RADIUS.magnitude())

TOP_BLOCK_NORMAL = pygame.math.Vector2(0, -1)
BOTTOM_BLOCK_NORMAL = pygame.math.Vector2(0, 1)
LEFT_BLOCK_NORMAL = pygame.math.Vector2(1, 0)
RIGHT_BLOCK_NORMAL = pygame.math.Vector2(-1, 0)

TOP_BLOCK_RECT = pygame.Rect((MARGIN_SIZE, MARGIN_SIZE - BALL_SIZE), (SCREEN.get_width() - 2 * MARGIN_SIZE, BALL_SIZE))
BOTTOM_BLOCK_RECT = pygame.Rect((MARGIN_SIZE, SCREEN.get_height() - MARGIN_SIZE), (SCREEN.get_width() - 2 * MARGIN_SIZE, BALL_SIZE))
LEFT_BLOCK_RECT = pygame.Rect((MARGIN_SIZE - BALL_SIZE, MARGIN_SIZE), (BALL_SIZE, SCREEN.get_height() - 2 * MARGIN_SIZE))
RIGHT_BLOCK_RECT = pygame.Rect((SCREEN.get_width() - MARGIN_SIZE, MARGIN_SIZE), (BALL_SIZE, SCREEN.get_height() - 2 * MARGIN_SIZE))

balls = []
blocks = []


class Block:
    def __init__(self, rect, normal):
        self.rect = rect
        self.normal = normal
        pygame.draw.rect(SCREEN, WHITE, self.rect)


class Ball:

    def __init__(self, x, y):
        self.velocity = pygame.math.Vector2(random.randint(-9, 9), random.randint(-9, 9))
        self.pos = pygame.math.Vector2(x, y)
        self.rect = pygame.Rect(self.pos - BALL_RADIUS, BALL_DIAMETER)
        pygame.draw.circle(SCREEN, WHITE, self.pos, BALL_RADIUS.magnitude())

    def update(self):
        old_pos = pygame.math.Vector2(self.pos)
        self.pos += self.velocity
        pygame.draw.circle(SCREEN, BLACK, old_pos, BALL_RADIUS.magnitude())
        pygame.draw.circle(SCREEN, WHITE, self.pos, BALL_RADIUS.magnitude())
        self.rect = pygame.Rect(self.pos - BALL_RADIUS, BALL_DIAMETER)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# see https://math.stackexchange.com/questions/13261/how-to-get-a-reflection-vector for details
def reflect(ball_velocity, block_normal):
    return ball_velocity - 2 * (ball_velocity.dot(block_normal)) * block_normal


def main():
    if pygame.get_sdl_version()[0] == 2:
        pygame.mixer.pre_init(44100, 32, 2, 1024)
    pygame.init()

    # top block
    blocks.append(Block(TOP_BLOCK_RECT, TOP_BLOCK_NORMAL))
    # bottom block
    blocks.append(Block(BOTTOM_BLOCK_RECT, BOTTOM_BLOCK_NORMAL))
    # left block
    blocks.append(Block(LEFT_BLOCK_RECT, LEFT_BLOCK_NORMAL))
    # right block
    blocks.append(Block(RIGHT_BLOCK_RECT, RIGHT_BLOCK_NORMAL))

    for i in range(1, 3):
        balls.append(Ball(random.randint(TOP_BLOCK_RECT.left, TOP_BLOCK_RECT.right), random.randint(LEFT_BLOCK_RECT.top, LEFT_BLOCK_RECT.bottom)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for ball in balls:
            ball.update()
            for block in blocks:
                if block.rect.colliderect(ball.rect):
                    ball.velocity = reflect(ball.velocity, block.normal)

        pygame.display.update()

        CLOCK.tick(100)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
