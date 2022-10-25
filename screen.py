import pygame
pygame.init()
pygame.display.set_caption('test')


class Screen:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))

    def screen_fill(self):
        self.window.fill((0, 0, 0))

    @staticmethod
    def screen_update():
        pygame.display.update()


screen = Screen(1000, 600)
