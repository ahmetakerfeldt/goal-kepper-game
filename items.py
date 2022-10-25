import pygame
from screen import screen


class Side:
    def __init__(self, width, height, x, y, red, green, blue):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.red = red
        self.green = green
        self.blue = blue

    def draw_side(self):
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen.window, (self.red, self.green, self.blue), rect)

    def color(self):
        self.red += 5
        if self.red == 250:
            self.red = 10

        self.green += 5
        if self.green == 250:
            self.green = 25

        self.blue += 5
        if self.blue == 250:
            self.blue = 20

    def draw_middle(self):
        pygame.draw.circle(screen.window, (self.red, self.green, self.blue), (self.x, self.y), 100, 2)


side_1 = Side(4, 1000, 0, 0, 245, 245, 245)
side_2 = Side(1000, 4, 0, 0, 245, 245, 245)
side_3 = Side(4, 1000, 996, 0, 245, 245, 245)
side_4 = Side(1000, 4, 0, 596, 245, 245, 245)
side_5 = Side(4, 600, 498, 0, 245, 245, 245)
middle = Side(0, 0, 500, 300, 245, 245, 245)
