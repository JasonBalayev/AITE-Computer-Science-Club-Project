import pygame
import sys
import random


class Circle:
    def __init__(self, x, y, radius, color, x_speed, y_speed, surface):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.surface = surface

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)

    def move_right(self):
        self.x += self.x_speed

    def move_left(self):
        self.x -= self.x_speed

    def move_down(self):
        self.y += self.y_speed

    def move_up(self):
        self.y -= self.y_speed 

class Entity:
    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        num_cells = random.randrange(2, 5)
        colors = ["red", "yellow", "blue"]
        self.cell_coords = [Circle(random.randrange(self.x-25, self.x+25, 10), random.randrange(self.y-25, self.y+25, 10), 20, random.choice(colors), 3, 3, surface) for y in range(num_cells) for x in range(num_cells)]
