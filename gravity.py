import pygame

from objects.objects import Player
from game_control.speed_control import *
from environment import *
from quantity.constants import *

pygame.init()
pygame.font.init
pygame.HWSURFACE


pygame.display.set_caption("Gravity")

def draw_window(coordinate_system, controller, player):
    WIN.fill(WHITE)
    coordinate_system.draw()

    controller.draw()

    for ball in player.balls:
        ball.draw()
        ball.dot_line.draw()

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    coordinate_system = CoordinateSystem()

    player = Player()

    controller = Controller(player)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if controller.activate() == True:
                    controller.activate()
                else:
                    player.add_ball()
        if controller.activate() == False:
            for ball in player.balls:
                ball.fall_down()
            player.remove_ball()
        controller.catch_motion(player)
        draw_window(coordinate_system, controller, player)
    pygame.quit()

if __name__ == "__main__":
    main()