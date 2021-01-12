# Imports
import pygame
from pygame.draw import *
from random import randint

pygame.init()

print('Please input size dimension with space separation')
size = input().split(' ')
width, height = int(size[0]), int(size[1])
screen = pygame.display.set_mode((width, height))
FPS = 2
grey = (128, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
azure = (0, 255, 192)
blue = (0, 0, 255)
purple = (128, 0, 255)
COLORS = (grey, white, red, orange, yellow, green,
         azure, blue, purple
         )


def draw_a_ball():
    x = randint(0, width)
    y = randint(0, height)
    radius = randint(10, 30)
    color = COLORS[randint(0, 8)]
    circle(screen, color, (x, y), radius)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.fill((0, 0, 0))
    draw_a_ball()
    pygame.display.update()

pygame.quit()