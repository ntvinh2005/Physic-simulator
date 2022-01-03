import pygame
from quantity.constants import *
from quantity.variable import *
from math import *
from game_control.control_element import Label


    
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1

    def draw(self):
        pygame.draw.circle(WIN, BLACK, (self.x, self.y), self.radius)

class Dot_Line:
    def __init__(self):
        self.dots = []
    
    def add_dot(self, x, y):
        new_dot = Dot(x, y)
        self.dots.append(new_dot)
    
    def draw(self):
        for dot in self.dots:
            dot.draw()

class Ball:
    def __init__(self, x, y):
        self.initial_x = x
        self.initial_y = y
        self.x = x
        self.y = y

        self.radius = 10
        self.weight = 0.5
        self.color = RED
        self.dot_line = Dot_Line()

        self.distance = 0
        self.fall_vel = 0
        self.fall_time = 0 
        self.fake_fall_time = 0

        #move by throwing velocity
        self.navigated = False
        self.throwed = False
        self.target = [0, 0]  
        self.vel = 0
        self.vel_x = 0
        self.vel_y = pi
        self.angle = 0
        print('Added')
        
        self.label = Label(x, y, self)

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius)
        self.label.render()

    def fall_down(self):
        if self.navigated == True:
            if self.throwed == False and (self.target[0]-self.x)!=0:
                self.vel = sqrt((self.target[0]-self.x)**2+(self.target[1]-self.y)**2)/CELL_WIDTH
                self.angle = atan2((self.target[1]-self.y),(self.target[0]-self.x))
                self.throwed = True
            elif self.throwed == False and (self.target[0]-self.x)==0:
                self.throwed = True

        # wait until the ball is navigated
        if self.navigated == True:
            #fall down because of gravity
            self.fall_vel = gravity_acceleration*self.fall_time
            self.fall_time += 1/60
            self.fake_fall_time+=1
            self.label.y = (self.initial_y + self.y)/2
            self.y += self.fall_vel/60
            self.move()

            #create line with dot
            if abs(self.y - self.initial_y)%10 < 2:
                self.dot_line.add_dot(self.x, self.y)

            if self.fake_fall_time%60==0:
                self.distance += self.fall_vel
            
            #label will receive indexes here
            self.label.receive_new_index(self)
    
    def move(self):
        self.vel_x = self.vel*cos(self.angle)
        self.vel_y = self.vel*sin(self.angle)
        self.x = self.x + self.vel_x
        self.y = self.y + self.vel_y
    

class Player:
    def __init__(self):
        self.name = 'vinh'
        self.balls = []
        self.added = False
    
    def add_ball(self):
        (x, y) = pygame.mouse.get_pos()
        new_ball = Ball(x, y)
        self.balls.append(new_ball)
    
    def remove_ball(self):
        for ball in self.balls:
            if ball.y + ball.radius >= WIDTH:
                self.balls.remove(ball)
    
    def throw_ball(self):
        if self.added == False:
            self.add_ball()
            self.added = True
        else: 
            (x, y) = pygame.mouse.get_pos()
            self.added = False    
            self.balls[-1].target = [x, y]
            self.balls[-1].navigated = True

