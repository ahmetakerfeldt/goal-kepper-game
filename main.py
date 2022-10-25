import sys
import pygame
pygame.init()

from screen import screen
from player import player_1, player_2
from bullet import bullet_1, bullet_2
from items import side_1, side_2, side_3, side_4, side_5, middle


while True:

    #screen
    pygame.time.Clock().tick(90)
    screen.screen_update()
    screen.screen_fill()

    #player_1
    player_1.move_1()
    player_1.limits()
    player_1.draw_player()

    #player_2
    player_2.draw_player()
    player_2.move_2()
    player_2.limits()

    #bullet
    bullet_1.draw_bullet()
    bullet_2.draw_bullet()
    bullet_1.move_1()
    bullet_2.move_2()
    bullet_1.limits_1()
    bullet_2.limits_2()

    x_change = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:

                bullet_1.x1_change += 21
                bullet_1.fire_mode = True

            elif event.key == pygame.K_m:
                bullet_2.x_2change += -21
                bullet_2.fire_mode_2 = True

    #texts
    font = pygame.font.SysFont('Agency FB', 40, 0)
    text_1 = font.render(f'Score:{player_1.score_1}', True, (0, 0, 244))
    screen.window.blit(text_1, (20, 10))

    text_2 = font.render(f'Score:{player_2.score_2}', True, (244, 0, 0))
    screen.window.blit(text_2, (870, 10))


    #side
    side_1.draw_side()
    side_2.draw_side()
    side_3.draw_side()
    side_4.draw_side()
    side_5.draw_side()
    middle.draw_middle()

    side_1.color()
    side_2.color()
    side_3.color()
    side_4.color()
    side_5.color()
    middle.color()
