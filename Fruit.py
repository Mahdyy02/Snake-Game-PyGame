import pygame
import random
from pygame.math import Vector2

class Fruit:

    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.position = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.position.x)*cell_size, int(self.position.y)*cell_size,cell_size, cell_size)
        #pygame.draw.rect(screen,(162,102,102),fruit_rect)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.position = Vector2(self.x, self.y)


cell_size = 35
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_size*cell_number))
apple = pygame.image.load('imgs/apple.png').convert_alpha()

