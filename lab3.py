import pygame
from pygame.draw import *
import random
from random import *

pygame.init()
FPS = 10
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Angry face')

color = [randint(0, 255), randint(0, 255), randint(0, 255)]

x = 200
y = 200
r = 150
rect(screen, (0, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (0, 0, 0), (200, 200), 150, 5)
circle(screen, (0, 0, 0), (130, 150), 30)
circle(screen, (0, 0, 0), (270, 150), 30)
circle(screen, (color), (130, 150), 13)
circle(screen, (color), (270, 150), 19)
line(screen, (0, 0, 0), (85, 95), (170, 120), 20)
line(screen, (0, 0, 0), (315, 95), (230, 120), 20)
circle(screen, (color), (180, 270), 20)
circle(screen, (255, 0, 0), (180, 270), 20, 5)
circle(screen, (color), (230, 270), 20)
circle(screen, (255, 0, 0), (230, 270), 20, 5)
rect(screen, (color),(180, 250, 50, 40))
line(screen, (255, 0, 0), (180, 250), (230, 250), 5)
line(screen, (255, 0, 0), (180, 290), (230, 290), 5)

'''
circle(screen, (255, 250, 250), (200, 270), 20)
circle(screen, (255, 0, 0), (200, 270), 20, 10)
circle(screen, (255, 250, 250), (208, 270), 20)
circle(screen, (255, 250, 250), (216, 270), 20)
circle(screen, (255, 0, 0), (216, 270), 20, 10)

polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)
'''
pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    color = [randint(0, 255), 0, randint(0, 56)]
    circle(screen, (color), (130, 150), 13)
    circle(screen, (color), (270, 150), 19)
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()