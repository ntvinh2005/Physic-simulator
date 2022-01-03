import pygame
from quantity.constants import *
pygame.init()
pygame.font.init()

FONT = pygame.font.Font('asset/Merriweather-Bold.ttf', 10)



class CoordinateSystem:
    def __init__(self):
        self.horizontal_lines = []
        self.vertical_lines = []
        horizontal_index = 0
        vertical_index = 0
        while horizontal_index <= HEIGHT:
            horizontal_new_line = HorizontalLine(0, horizontal_index)
            horizontal_new_line.index = horizontal_index
            self.horizontal_lines.append(horizontal_new_line)
            horizontal_index+=CELL_HEIGHT

        while vertical_index <= WIDTH:
            vertical_new_line = VerticalLine(vertical_index, 0)
            vertical_new_line.index = vertical_index
            self.vertical_lines.append(vertical_new_line)
            vertical_index+=CELL_WIDTH

    def draw(self):
        for horizontal_line in self.horizontal_lines:
            horizontal_line.draw()
        for vertical_line in self.vertical_lines:
            vertical_line.draw()

class HorizontalLine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = WIDTH
        self.height = 1
        self.index = 0
    
    def draw(self):
        pygame.draw.rect(WIN, BLACK, (self.x, self.y, self.width, self.height))
        text_surface = FONT.render(str(self.index), 1, BLACK)
        WIN.blit(text_surface, (self.x, self.y - text_surface.get_width()/2))

class VerticalLine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 1
        self.height = HEIGHT
        self.index = 0
    
    def draw(self):
        pygame.draw.rect(WIN, BLACK, (self.x, self.y, self.width, self.height))
        text_surface = FONT.render(str(self.index), 1, BLACK)
        WIN.blit(text_surface, (self.x - text_surface.get_height()/2, self.y))
