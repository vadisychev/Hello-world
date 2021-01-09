def main(x, y, width, height):
    """
    Draw a house with a center in x,y point.
    Dimension of the house is width * height
    :param x: x coordinate of the house center
    :param y: y coordinate of the house center
    :param width: width of the house
    :param height: height of the house
    :return: None
    """
    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Draw a house.
    :param x: X coordinate of center House
    :param y: Y coordinate of House bottom
    :param width: Width of the House
    :param height: Height of the House
    :return:
    """
    print("I'm drawing a house")
    foundation_width = 1.05 * width
    foundation_height = 0.05 * height
    foundation_y = 0.95 * y
    draw_foundation(x, foundation_y, foundation_width, foundation_height)
    walls_height = 0.55 * height
    walls_y = 0.4 * y
    draw_walls(x, walls_y, width, walls_height)
    roof_width = 1.1 * width
    roof_height = 0.4 * height
    roof_y = 0
    draw_roof(x, roof_y, roof_width, roof_height)


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
    :param x: X coordinate of walls center
    :param y: Y coordinate of walls center
    :param width: Width of walls
    :param height: Height of walls
    :return: None
    """
    draw_walls_frame(x, y, width, height)
    draw_walls_print(x, y, width, height)
    window_y = 0.65 * y
    window_width = width / 4
    window_height = height / 2
    draw_walls_window(x, window_y, window_width, window_height)


def draw_roof(x, y, width, height):
    """
    Draw roof of the house which consist of roof frame, print, window and chimney.
    :param x: X coordinate of roof center
    :param y: Y coordinate of roof center
    :param width: Width of roof
    :param height: Height of roof
    :return: None
    """
    chimney_x = x - width / 2
    chimney_y = y + height / 2
    chimney_width = width / 5
    chimney_height = height / 3
    draw_chimney(chimney_x, chimney_y, chimney_width, chimney_height)
    draw_roof_frame(x, y, width, height)
    draw_roof_print(x, y, width, height)
    roof_window_width = width / 4
    roof_window_height = height / 3
    draw_roof_window(x, y, roof_window_width, roof_window_height)


def draw_foundation_frame(x, y, width, height):
    pass


def draw_foundation_print(x, y, width, height):
    pass


def draw_walls_frame(x, y, width, height):
    pass


def draw_walls_print(x, y, width, height):
    pass


def draw_walls_window(x, y, width, height):
    pass


def draw_chimney(x, y, width, height):
    pass


def draw_roof_frame(x, y, width, height):
    pass


def draw_roof_print(x, y, width, height):
    pass


def draw_roof_window(x, y, width, height):
    pass


# main(x, y, width, height)

