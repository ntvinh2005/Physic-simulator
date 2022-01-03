import pygame
from quantity.constants import *
pygame.init()


class Button:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))
    
    def click_on(self):
        (x,y) = pygame.mouse.get_pos()
        if x >= self.x and x<=self.x+self.width and y >= self.y and y<=self.y+self.height:
            return True
        else: 
            return False


class Label:
    def __init__(self, x, y, ball):
        self.x = x
        self.y = y
        self.indexes = [["Ball's y: ", ball.y, "m"], 
                    ["Distance: ", ball.distance, "m"], 
                    ["Velocity: ", ball.fall_vel, "m/s"], 
                    ["Fall time: ", ball.fall_time, "s"]]
    
    def receive_new_index(self,ball):
        self.indexes = [["Ball's y: ", ball.y, "m"], 
                    ["Distance: ", ball.distance, "m"], 
                    ["Velocity: ", ball.fall_vel, "m/s"], 
                    ["Fall time: ", ball.fall_time, "s"]]
    
    def render(self):
        i = 0
        for index in self.indexes:
            text_surface = FONT.render(index[0]+str(int(index[1]))+index[2], 1, BLACK)
            WIN.blit(text_surface, (self.x - text_surface.get_height()/2, self.y+i))
            i+=40