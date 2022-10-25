from screen import screen

import pygame
pygame.init()


class Player:
    def __init__(self, width, height, x, y, score_1, score_2, red, green, blue):
        self. width = width
        self.height = height
        self.x = x
        self.y = y
        self.score_1 = score_1
        self.score_2 = score_2
        self.red = red
        self.green = green
        self.blue = blue

    def draw_player(self):
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen.window, (self.red, self.green, self.blue), rect, 2, 5)

    def move_1(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.y -= 10

        if key[pygame.K_s]:
            self.y += 10

    def move_2(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.y -= 10

        if key[pygame.K_DOWN]:
            self.y += 10

    def limits(self):
        if self.y < 0:
            self.y = 0
        if self.y > (screen.height - self.height):
            self.y = screen.height - self.height


player_1 = Player(30, 100, 20, 275, 0, 0, 0, 0, 255)
player_2 = Player(30, 100, 950, 275, 0, 0, 255, 0, 0)
