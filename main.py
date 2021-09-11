# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import pygame
import random

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((500, 400), 0, 32)

dots = []


class Dot:

    def __init__(self, x, y):
        self.velocity = pygame.math.Vector2(random.randint(-9, 9), random.randint(-9, 9))
        self.rect = pygame.Rect(x, y, 10, 10)
        pygame.draw.rect(SCREEN, WHITE, self.rect)

    def update(self):
        old_rect = pygame.Rect(self.rect)
        self.rect.topleft = pygame.math.Vector2(self.rect.topleft) + self.velocity
        print(f'Updating... topleft = {self.rect.topleft}')
        pygame.draw.rect(SCREEN, BLACK, old_rect)
        pygame.draw.rect(SCREEN, WHITE, self.rect)
        bounding_rect = SCREEN.get_bounding_rect()
        if not bounding_rect.contains(self.rect):
            if self.rect.centerx < bounding_rect.left or self.rect.centerx > bounding_rect.right:
                self.velocity = pygame.math.Vector2(-1 * self.velocity.x, self.velocity.y)
            elif self.rect.centery < bounding_rect.top or self.rect.centery > bounding_rect.bottom:
                self.velocity = pygame.math.Vector2(self.velocity.x, -1 * self.velocity.y)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main():
    if pygame.get_sdl_version()[0] == 2:
        pygame.mixer.pre_init(44100, 32, 2, 1024)
    pygame.init()

    for i in range(1, 50):
        dots.append(Dot(random.randint(0, 500), random.randint(0, 400)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for dot in dots:
            dot.update()

        pygame.display.update()
        CLOCK.tick(99999)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
