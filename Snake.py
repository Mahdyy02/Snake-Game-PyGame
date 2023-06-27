from pygame.math import Vector2
import pygame

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        #Head design
        self.head_up = pygame.image.load('imgs/head_up.png')
        self.head_down = pygame.image.load('imgs/head_down.png')
        self.head_left = pygame.image.load('imgs/head_left.png')
        self.head_right = pygame.image.load('imgs/head_right.png')

        #Tail design
        self.tail_up = pygame.image.load('imgs/tail_up.png')
        self.tail_down = pygame.image.load('imgs/tail_down.png')
        self.tail_left = pygame.image.load('imgs/tail_left.png')
        self.tail_right = pygame.image.load('imgs/tail_right.png')

        #Body design
        self.body_vertical = pygame.image.load('imgs/body_vertical.png')
        self.body_horizontal = pygame.image.load('imgs/body_horizontal.png')
        self.body_bl = pygame.image.load('imgs/body_bl.png')
        self.body_br = pygame.image.load('imgs/body_br.png')
        self.body_tl = pygame.image.load('imgs/body_tl.png')
        self.body_tr = pygame.image.load('imgs/body_tr.png')

        self.head = self.head_right
        self.tail = self.tail_right

        self.eat_sound = pygame.mixer.Sound('Sound/water_drop.mp3')

    def draw_snake(self):

        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            snake_rect = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, snake_rect)

            elif index == len(self.body)-1:
                screen.blit(self.tail, snake_rect)
            else:
                previous_block_correlation = self.body[index-1] - block
                next_block_correlation = self.body[index+1] - block
                if previous_block_correlation.x == next_block_correlation.x:
                    screen.blit(self.body_vertical, snake_rect)
                elif previous_block_correlation.y == next_block_correlation.y:
                    screen.blit(self.body_horizontal, snake_rect)
                else:
                    if previous_block_correlation.x == -1 and next_block_correlation.y == -1 or previous_block_correlation.y == -1 and next_block_correlation.x == -1:
                        screen.blit(self.body_tl, snake_rect)
                    elif previous_block_correlation.x == -1 and next_block_correlation.y == 1 or previous_block_correlation.y == 1 and next_block_correlation.x == -1:
                        screen.blit(self.body_bl, snake_rect)
                    elif previous_block_correlation.x == 1 and next_block_correlation.y == -1 or previous_block_correlation.y == -1 and next_block_correlation.x == 1:
                        screen.blit(self.body_tr, snake_rect)
                    elif previous_block_correlation.x == 1 and next_block_correlation.y == 1 or previous_block_correlation.y == 1 and next_block_correlation.x == 1:
                        screen.blit(self.body_br, snake_rect)

    def update_head_graphics(self):

        head_correlation = self.body[1] - self.body[0]

        if head_correlation == Vector2(1,0):
            self.head = self.head_left
        elif head_correlation == Vector2(-1,0):
            self.head = self.head_right
        elif head_correlation == Vector2(0, 1):
            self.head = self.head_up
        else:
            self.head = self.head_down

    def update_tail_graphics(self):

        tail_correlation = self.body[-2] - self.body[-1]

        if tail_correlation == Vector2(1,0):
            self.tail = self.tail_left
        elif tail_correlation == Vector2(-1,0):
            self.tail = self.tail_right
        elif tail_correlation == Vector2(0, 1):
            self.tail = self.tail_up
        else:
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block:
            self.new_block = False
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_eating_sound(self):
        self.eat_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


cell_size = 35
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_size*cell_number))


