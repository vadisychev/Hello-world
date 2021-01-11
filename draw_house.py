# imports
import pygame
from pygame.draw import *
import random
from random import *

# Functions description.
# Main is the function which draw a house


def main(x, y, width, height):
    """
    Draw a house with a foundation in (x,y) point.
    Dimensions of the house are width * height. (x, y) and house dimensions should be set up manually.
    :param x: x coordinate of the house center
    :param y: y coordinate of the house bottom
    :param width: width of the house
    :param height: height of the house
    :return: None
    """
    draw_house(x, y, width, height)


# draw_scene functions draws scene of the picture

def draw_scene(width, height):
    """
    Draw a scene of the picture: sky and land.
    :param width: Width of the screen
    :param height: Height of the screen
    :return: None
    """
    draw_sky_x = 0
    draw_sky_y = 0
    draw_sky_height = 2 / 3 * height
    draw_sky(draw_sky_x, draw_sky_y, width, draw_sky_height)
    draw_land_x = 0
    draw_land_y = 2 / 3 * height
    draw_land_height = height / 3
    draw_land(draw_land_x, draw_land_y, width, draw_land_height)


def draw_sky(x, y, width, height):
    """
    Draw blue sky
    :param x: X coordinate of rect
    :param y: Y coordinate of rect
    :param width: Width of the sky = width of the screen
    :param height: Height of the sky = 2/3 of the screen height
    :return: None
    """
    rect(screen, (0, 191, 255), (x, y, width, height))


def draw_land(x, y, width, height):
    """
    Draw land.
    :param x: X coordinate of rectangle (=0).
    :param y: Y coordinate of rectagnle.
    :param width: Width of land. it's equal to screen width
    :param height: Height of land.
    :return: None
    """
    rect(screen, (0, 155, 50), (x, y, width, height))


def draw_clouds_and_sun(width, height):
    draw_clouds()
    draw_sun()


def draw_clouds():
    pass


def draw_sun():
    pass


def draw_house(x, y, width, height):
    """
    Draw a house with center in (x, y), width = width and height = height.
    Also this function defines coordindates and dimension parameters for foundation, walls and roof.
    :param x: X coordinate of center House
    :param y: Y coordinate of House bottom
    :param width: Width of the House
    :param height: Height of the House
    :return: None
    """
    print("I'm drawing a house")
    foundation_width = 1.1 * width
    foundation_height = 0.1 * height
    foundation_x = x - foundation_width / 2
    foundation_y = y - foundation_height
    draw_foundation(foundation_x, foundation_y, foundation_width, -foundation_height)
    walls_height = 0.5 * height
    walls_y = y - 2 * foundation_height - walls_height
    walls_x = x - width / 2
    draw_walls(walls_x, walls_y, width, walls_height)
    roof_width = 1.15 * width
    roof_height = 0.4 * height
    roof_x = x - roof_width / 2
    roof_y = walls_y
    draw_roof(roof_x, roof_y, roof_width, roof_height)


def draw_foundation(x, y, width, height):
    """
    Draw foundation of the house which consist of frame and prints on frame.
    :param x: X coordinate of foundation center
    :param y: Y coordinate of foundation center
    :param width: Width of foundation
    :param height: Height of foundation
    :return: None
    """
    draw_foundation_frame(x, y, width, height)
    draw_foundation_print(x, y, width, height)


def draw_walls(x, y, width, height):
    """
    Draw walls of the house which consist of walls frame, prints and window.
    Aslo this functions defines coordinates fo window and dimension parameters.
    :param x: X coordinate of walls center
    :param y: Y coordinate of walls center
    :param width: Width of walls
    :param height: Height of walls
    :return: None
    """
    draw_walls_frame(x, y, width, height)
    draw_walls_print(x, y, width, height)
    window_y = y + height / 4
    window_x = x + width / 2 - width / 8
    window_width = width / 4
    window_height = height / 2
    draw_walls_window(window_x, window_y, window_width, window_height)


def draw_roof(x, y, width, height):
    """
    Draw roof of the house which consist of roof frame, print, window and chimney.
    Also this function defines coordinates of chimney, roof window and dimension parameters.
    :param x: X coordinate of roof center
    :param y: Y coordinate of roof center
    :param width: Width of roof
    :param height: Height of roof
    :return: None
    """
    chimney_x = x + width / 5
    chimney_y = y - height / 1.3
    chimney_width = width / 8
    chimney_height = height / 2
    draw_chimney(chimney_x, chimney_y, chimney_width, chimney_height)
    draw_roof_frame(x, y, width, height)
    draw_roof_print(x, y, width, height)
    roof_window_width = width / 4
    roof_window_height = height / 3
    roof_window_x = x + width / 2
    roof_window_y = y - height / 2
    draw_roof_window(roof_window_x, roof_window_y, roof_window_width, roof_window_height)


def draw_foundation_frame(x, y, width, height):
    """
    This function draws foundation. Color and shape of foundation are defined in this function.
    :param x: X coordindate of upper left corner of the foundation
    :param y: Y coordindate of upper left corner of the foundation
    :param width: Width of foundation
    :param height: Height of foundation
    :return: None
    """
    rect(screen, (0, 0, 0), (x, y, width, height), 2)
    rect(screen, (76, 72, 76), (x, y, width, height))


def draw_foundation_print(x, y, width, height):
    """
    Add some prints on foundation. Shape of the prints is defined here.
    """
    number_of_prints = 20
    prints_size = width / number_of_prints
    center_x = x + prints_size / 2
    center_y = y + height / 2
    for i in range(number_of_prints):
        circle(screen, (100, 150, 100), (center_x, center_y), prints_size)
        center_x += prints_size


def draw_walls_frame(x, y, width, height):
    """
    Draw walls frame and fill it with a color whih is defined here.
    :param x: X coordindate of upper left corner of the walls
    :param y: Y coordindate of upper left corner of the walls
    :param width: Walls width
    :param height: Walls height
    :return: None
    """
    rect(screen, (155, 0, 155), (x, y, width, height))
    rect(screen, (0, 0, 0), (x, y, width, height), 2)


def draw_walls_print(x, y, width, height):
    pass


def draw_walls_window(x, y, width, height):
    """
    Draw window in the wall. Window and window frame shapes and color are defined here.
    """
    rect(screen, (0, 155, 155), (x, y, width, height))
    rect(screen, (0, 0, 0), (x, y, width, height), 2)
    rect(screen, (0, 0, 0), (x, y, width / 2, height), 2)
    rect(screen, (0, 0, 0), (x, y, width, height / 2), 2)


def draw_chimney(x, y, width, height):
    """
    Draw a chimney on the roof. Shape and color of the chimney are defined here
    """
    rect(screen, (76, 72, 76), (x, y, width, height))
    rect(screen, (0, 0, 0), (x, y, width, height), 2)


def draw_roof_frame(x, y, width, height):
    """
    Draw roof of the house. Roof shape and color are defined here.
    """
    polygon(screen, (144, 144, 0), [(x, y), (x + width / 2, y - height), (x + width, y)])
    polygon(screen, (0, 0, 0), [(x, y), (x + width / 2, y - height), (x + width, y)], 2)


def draw_roof_print(x, y, width, height):
    pass


def draw_roof_window(x, y, width, height):
    """
    Draw window in the roof. Shape and color of the window are defined here.
    """
    ellipse(screen, (0, 155, 155), (x - width / 2, y, width, height))
    ellipse(screen, (0, 0, 0), (x - width / 2, y, width, height), 2)


# Initialize pygame module. Set basic parameters of the screen: width, height, FPS

pygame.init()
FPS = 30
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
draw_scene(screen_width, screen_height)

# Call the function to draw the house / houses.

main(screen_width / 4, 0.95 * screen_height, 250, 250)
main(0.75 * screen_width, 0.85 * screen_height, 150, 150)
main(0.55 * screen_width, 0.6 * screen_height, 50, 50)

# Updating screen till the window closing

while not finished:
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

