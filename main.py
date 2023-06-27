import pygame
import sys
import random
from pygame.math import Vector2
import Fruit
import Snake

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()


class Main:
    def __init__(self):
        self.snake = Snake.Snake()
        self.fruit = Fruit.Fruit()

    def game_update(self):
        self.snake.move_snake()
        self.check_collission()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collission(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_eating_sound()

            for part in self.snake.body[1:]:
                if part == self.fruit.position:
                    self.fruit.randomize()

    def check_fail(self):
        if not (0 <= self.snake.body[0].x < cell_number and 0 <= self.snake.body[0].y < cell_number):
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    @staticmethod
    def draw_grass():
        grass_color = (177, 255, 111)
        for row in range(cell_number):
            if row%2 == 0:
                for col in range(cell_number):
                    if col%2 == 0:
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col%2 != 0:
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = "Score: "+str((len(self.snake.body)-3)*10)
        score_surface = game_font.render(score_text,True,(199, 55, 47))
        score_rect = score_surface.get_rect(center=(int(cell_size*cell_number - 100), 40))
        screen.blit(score_surface, score_rect)


# initialisation
cell_size = 35
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_size*cell_number))
clock = pygame.time.Clock()
apple = pygame.image.load('imgs/apple.png').convert_alpha()
main_game = Main()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)

game_font = pygame.font.Font('Font/BiggyJohn.ttf', 25)

#main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screen_update:
            main_game.game_update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            elif event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            elif event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            elif event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)

    screen.fill((138, 226, 62))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

