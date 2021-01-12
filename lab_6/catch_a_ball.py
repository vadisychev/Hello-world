# Imports
import pygame
from pygame.draw import *
from random import randint

pygame.init()

print('Please input size dimension with space separation')
# size = input().split(' ')
# width, height = int(size[0]), int(size[1])
width, height = 500, 500
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
    global x, y, radius
    x = randint(0, width)
    y = randint(0, height)
    radius = randint(10, 30)
    color = COLORS[randint(0, 8)]
    circle(screen, color, (x, y), radius)


def event_handler(mouse_event):
    check_circles_crossing(mouse_event.pos, x, y, radius)
    circle(screen, (255, 255, 255), mouse_event.pos, 20)
    pygame.display.update()
    print(mouse_event.type, mouse_event.pos)


def calculate_distance(event_coords, circle_coords):
    x_coords_square = (event_coords[0] - circle_coords[0])**2
    y_coords_square = (event_coords[1] - circle_coords[1])**2
    distance = (x_coords_square + y_coords_square)**0.5
    return distance


def check_circles_crossing(mouse_event_coords, x, y, radius):
    distance = calculate_distance(mouse_event_coords, (x, y))
    if distance <= radius + 40:
        print('WIN')
    else:
        print('the distance is ', abs(distance - radius))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS * 4)
    screen.fill((0, 0, 0))
    draw_a_ball()
    pygame.display.update()
    pygame.time.delay(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            event_handler(event)
            print(x, y)


pygame.quit()
