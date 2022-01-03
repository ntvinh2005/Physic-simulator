import pygame
from quantity.constants import *
from objects.objects import Ball
from .control_element import Label, Button
pygame.init()
pygame.font.init()

FONT = pygame.font.Font('asset/Merriweather-Bold.ttf', 10)

class Controller():
    def __init__(self, player):
        if player.balls != []:
            self.ball = player.balls[0]
        else:
            self.ball = Ball(0, 0)
        self.buttons = [
            Button(10,10,50,20,YELLOW)
        ]
        self.labels = [
            Label(WIDTH-100, 10, self.ball)
        ]
    
    def catch_motion(self, player):
        if player.balls != []:
            self.ball = player.balls[0]
        else:
            self.ball = Ball(0, 0)
        self.labels = [
            Label(WIDTH-100, 10, self.ball)
        ]
        
    def draw(self):
        for button in self.buttons:
            button.draw()
        for label in self.labels:
            label.render()

    def activate(self):
        for button in self.buttons:
            if button.click_on() == True:
                return True
        return False



