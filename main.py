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

BALL_SIZE = 20
BALL_RADIUS = pygame.math.Vector2(math.sqrt(BALL_SIZE), math.sqrt(BALL_SIZE))
BALL_DIAMETER = (2 * BALL_RADIUS.magnitude(), 2 * BALL_RADIUS.magnitude())

X_BLOCK_SIZE = (SCREEN.get_width(), SCREEN.get_width())
Y_BLOCK_SIZE = (SCREEN.get_height(), SCREEN.get_height())

TOP_BLOCK_NORMAL = pygame.math.Vector2(0, -1)
BOTTOM_BLOCK_NORMAL = pygame.math.Vector2(0, 1)
LEFT_BLOCK_NORMAL = pygame.math.Vector2(1, 0)
RIGHT_BLOCK_NORMAL = pygame.math.Vector2(-1, 0)

TOP_BLOCK = pygame.Rect(X_BLOCK_SIZE[0] * TOP_BLOCK_NORMAL, X_BLOCK_SIZE)
BOTTOM_BLOCK = pygame.Rect(Y_BLOCK_SIZE[0] * BOTTOM_BLOCK_NORMAL, X_BLOCK_SIZE)
LEFT_BLOCK = pygame.Rect(-1 * Y_BLOCK_SIZE[0] * LEFT_BLOCK_NORMAL, Y_BLOCK_SIZE)
RIGHT_BLOCK = pygame.Rect(-1 * X_BLOCK_SIZE[0] * RIGHT_BLOCK_NORMAL, Y_BLOCK_SIZE)

balls = []


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


def reflect(ball_velocity, block_normal):
    return ball_velocity - 2 * (ball_velocity.dot(block_normal)) * block_normal


def main():
    if pygame.get_sdl_version()[0] == 2:
        pygame.mixer.pre_init(44100, 32, 2, 1024)
    pygame.init()

    for i in range(1, 3):
        balls.append(Ball(random.randint(0, SCREEN.get_width()), random.randint(0, SCREEN.get_height())))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for ball in balls:
            ball.update()
            if TOP_BLOCK.colliderect(ball.rect):
                ball.velocity = reflect(ball.velocity, TOP_BLOCK_NORMAL)
            elif BOTTOM_BLOCK.colliderect(ball.rect):
                ball.velocity = reflect(ball.velocity, BOTTOM_BLOCK_NORMAL)
            elif LEFT_BLOCK.colliderect(ball.rect):
                ball.velocity = reflect(ball.velocity, LEFT_BLOCK_NORMAL)
            elif RIGHT_BLOCK.colliderect(ball.rect):
                ball.velocity = reflect(ball.velocity, RIGHT_BLOCK_NORMAL)

        pygame.display.update()

        CLOCK.tick(100)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
