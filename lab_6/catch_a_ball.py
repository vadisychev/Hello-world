# Imports
import pygame
from pygame.draw import *
from random import randint

# pygame module initialization
pygame.init()
print('Please inout your player ID')
player = input()


# Create surface (screen) and set basic parameters: screen size, set of colors, FPS.

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
FPS = 2
total_points = 0
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
    """
    Draw a ball (circle) with a center in (x, y) point and radius.
    Ball dimension and position are set randomly.
    Ball color is set randomly from set of COLORS which is listed before
    :return: None
    """
    global x, y, radius, color_index
    x = randint(0, width)
    y = randint(0, height)
    radius = randint(20, 40)
    color = COLORS[randint(0, 8)]
    color_index = COLORS.index(color)
    circle(screen, color, (x, y), radius)


def event_handler(mouse_event):
    """
    Handle mouse clicks:
    1) Check does ball cross with mouse and if yes add points
    2) Draw white ball at click place
    3) Print mouse event type and position (x, y).
    :param mouse_event: event.MOUSEBUTTONDOWN
    :return: None
    """
    global total_points
    if check_circles_crossing(mouse_event.pos, x, y, radius):
        total_points += calculate_points(radius)
    circle(screen, (255, 255, 255), mouse_event.pos, 20)
    pygame.display.update()


def calculate_distance(event_coords, circle_coords):
    """
    Calculate distance between ball center and click.
    :param event_coords: Mouse click coordinates
    :param circle_coords: Ball center coordinates
    :return: distance between ball center and click
    """
    x_coords_square = (event_coords[0] - circle_coords[0])**2
    y_coords_square = (event_coords[1] - circle_coords[1])**2
    distance = (x_coords_square + y_coords_square)**0.5
    return distance


def calculate_points(ball_radius):
    """
    It will calculate points for a ball if mouse cross the ball.
    :param ball_radius: it's a global parameter. Radius of appeared  on the screen ball
    :return: points for the ball
    """
    radius_price = 40 - ball_radius
    color_price = color_index
    points = radius_price * color_price
    print('WIN {} points!!!'.format(points))
    return points


def write_points_in_file(points):
    """
    Write total points in file total_pointx.txt
    :param points: points number to write
    :return: None
    """
    out = open('total_points.txt', 'a')
    string = '{} scored {} points!\n'.format(player, points)
    out.write(string)
    out.close()


def check_circles_crossing(mouse_event_coords, x, y, radius):
    """
    Check whether click cross the ball. Print "WIN" message if click lays inside ball's borders.
    :param mouse_event_coords: Coordinates of mouse click
    :param x: X coordinate of the ball center
    :param y: Y coordinate of the ball center
    :param radius: Radius of the ball
    :return: None
    """
    distance = calculate_distance(mouse_event_coords, (x, y))
    if distance <= radius:
        return True
    else:
        return False


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
            write_points_in_file(total_points)
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            event_handler(event)


pygame.quit()
