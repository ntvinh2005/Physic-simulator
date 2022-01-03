import pygame
pygame.font.init()
FONT = pygame.font.Font('asset/Merriweather-Bold.ttf', 10)

WIDTH, HEIGHT=1200, 600
CELL_WIDTH, CELL_HEIGHT = 100, 100
#1 metres in our simulator equal to 1 pixels

WIN=pygame.display.set_mode((WIDTH, HEIGHT))

WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
RED=(255,0,0)
GREEN=(0,255,0)
YELLOW=(255,255,0)

gravity_acceleration = 10


FPS=60