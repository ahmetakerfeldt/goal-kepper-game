import pygame
pygame.init()
font = pygame.font.SysFont('Arial', 50)

from screen import screen
from player import player_1
from player import player_2


class Bullet:

    def __init__(self, x, y, radius, x1_change, x2_change, fire_mode, fire_mode_2):
        self.x = x
        self. y = y
        self.r = radius
        self.x1_change = x1_change
        self.x_2change = x2_change
        self.fire_mode = fire_mode
        self.fire_mode_2 = fire_mode_2

    def draw_bullet(self):
        pygame.draw.circle(screen.window, (255, 255, 255), (self.x, self.y), self.r, 1)

    def move_1(self):

        self.x += self.x1_change
        if not self.fire_mode:
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                self.y -= 10
            if key[pygame.K_s]:
                self.y += 10

    def move_2(self):

        self.x += self.x_2change
        if not self.fire_mode_2:
            key = pygame.key.get_pressed()
            if key[pygame.K_UP]:
                self.y -= 10
            if key[pygame.K_DOWN]:
                self.y += 10

    def limits_1(self):
        if self.y < 50:
            self.y = 50
        if self.y > 575:
            self.y = 575

        if player_2.y < bullet_1.y < player_2.y + 100 and player_2.x < bullet_1.x < player_2.x + 100:
            self.x = player_1.x + 15
            self.y = player_1.y + 50
            player_1.score_1 += 1
            self.x1_change = 0
            self.fire_mode = False

        elif self.x > 1000:
            self.x = (player_1.x + 15)
            self.x1_change = 0
            self.y = (player_1.y + 50)
            self.fire_mode = False

    def limits_2(self):
        if self.y < 50:
            self.y = 50
        if self.y > 550:
            self.y = 550

        if player_1.y < bullet_2.y < player_1.y + 100 and player_1.x - 100 < bullet_2.x < player_1.x + 15:
            self.x = player_2.x + 15
            self.y = player_2.y + 50
            player_2.score_2 += 1
            self.x_2change = 0
            self.fire_mode_2 = False

        elif self.x < 0:
            self.x = (screen.width - 35)
            self.x_2change = 0
            self.y = (player_2.y + 50)
            self.fire_mode_2 = False


bullet_1 = Bullet((player_1.x + player_1.width/2), (player_1.y + player_1.height/2), 10, 0, 0, False, False)
bullet_2 = Bullet((player_2.x + player_2.width/2), (player_2.y + player_2.height/2), 10, 0, 0, False, False)
