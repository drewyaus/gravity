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

BALL_SIZE = 10
BALL_RADIUS = pygame.math.Vector2(math.sqrt(BALL_SIZE), math.sqrt(BALL_SIZE))
BALL_DIAMETER = (2 * BALL_RADIUS.magnitude(), 2 * BALL_RADIUS.magnitude())

GRAVITY = pygame.math.Vector2(0, 1)

TOP_WALL_NORMAL = pygame.math.Vector2(0, -1)
BOTTOM_WALL_NORMAL = pygame.math.Vector2(0, 1)
LEFT_WALL_NORMAL = pygame.math.Vector2(1, 0)
RIGHT_WALL_NORMAL = pygame.math.Vector2(-1, 0)

WALL_THICKNESS = 20
TOP_WALL_RECT = pygame.Rect((MARGIN_SIZE, MARGIN_SIZE - WALL_THICKNESS),
                            (SCREEN.get_width() - 2 * MARGIN_SIZE, WALL_THICKNESS))
BOTTOM_WALL_RECT = pygame.Rect((MARGIN_SIZE, SCREEN.get_height() - MARGIN_SIZE),
                               (SCREEN.get_width() - 2 * MARGIN_SIZE, WALL_THICKNESS))
LEFT_WALL_RECT = pygame.Rect((MARGIN_SIZE - WALL_THICKNESS, MARGIN_SIZE),
                             (WALL_THICKNESS, SCREEN.get_height() - 2 * MARGIN_SIZE))
RIGHT_WALL_RECT = pygame.Rect((SCREEN.get_width() - MARGIN_SIZE, MARGIN_SIZE),
                              (WALL_THICKNESS, SCREEN.get_height() - 2 * MARGIN_SIZE))

balls = []
walls = []


class Wall:
    def __init__(self, rect, normal, color):
        self.rect = rect
        self.normal = normal
        pygame.draw.rect(SCREEN, color, self.rect)


class Ball:

    def __init__(self, x, y, velocity):
        self.velocity = velocity
        self.pos = pygame.math.Vector2(x, y)
        self.rect = pygame.Rect(self.pos - BALL_RADIUS, BALL_DIAMETER)
        pygame.draw.circle(SCREEN, WHITE, self.pos, BALL_RADIUS.magnitude())
        pygame.draw.rect(SCREEN, pygame.Color(255, 0, 255), (self.pos - BALL_RADIUS, BALL_DIAMETER))

    def update(self):
        old_pos = pygame.math.Vector2(self.pos)
        self.velocity += GRAVITY
        self.pos = self.pos + self.velocity
        pygame.draw.circle(SCREEN, BLACK, old_pos, BALL_RADIUS.magnitude())
        pygame.draw.circle(SCREEN, WHITE, self.pos, BALL_RADIUS.magnitude())
        self.rect = pygame.Rect(self.pos - BALL_RADIUS, BALL_DIAMETER)
        pygame.draw.rect(SCREEN, pygame.Color(255, 0, 255), (self.pos - BALL_RADIUS, BALL_DIAMETER))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main():
    if pygame.get_sdl_version()[0] == 2:
        pygame.mixer.pre_init(44100, 32, 2, 1024)
    pygame.init()

    # top wall
    walls.append(Wall(TOP_WALL_RECT, TOP_WALL_NORMAL, pygame.Color(255, 0, 0)))
    # bottom wall
    walls.append(Wall(BOTTOM_WALL_RECT, BOTTOM_WALL_NORMAL, pygame.Color(0, 255, 0)))
    # left wall
    walls.append(Wall(LEFT_WALL_RECT, LEFT_WALL_NORMAL, pygame.Color(0, 0, 255)))
    # right wall
    walls.append(Wall(RIGHT_WALL_RECT, RIGHT_WALL_NORMAL, pygame.Color(255, 0, 255)))

    for i in range(1, 3):
        rand_x = random.randint(LEFT_WALL_RECT.left, RIGHT_WALL_RECT.right)
        rand_y = random.randint(TOP_WALL_RECT.bottom, BOTTOM_WALL_RECT.top)
        velocity = pygame.math.Vector2(random.randint(0, 9), 0).rotate(random.randint(-10, 10))
        balls.append(Ball(rand_x, rand_y, velocity))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for ball in balls:
            for wall in walls:
                projected_rect = ball.rect.move(ball.velocity)
                if pygame.Rect.colliderect(projected_rect, wall.rect) or wall.rect.contains(projected_rect):
                    ball.velocity = ball.velocity.reflect(wall.normal)
                    ball.rect = ball.rect.move(50 * wall.normal)
                else:
                    ball.update()

        pygame.display.update()

        CLOCK.tick(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
