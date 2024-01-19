import pygame
import sys
import random

# pygame.init()
# display = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()


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

class Player:
    def __init__(self, surface):
        self.cell_coords = [Circle(random.randrange(200, 250, 10), random.randrange(200, 250, 10), 20, "green", 3, 3, surface) for y in range(200, 250, 10) for x in range(200, 250, 10)]

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     display.fill("black")

#     mouse_coords = pygame.mouse.get_pos()
#     mouse_circle.x, mouse_circle.y = mouse_coords
#     mouse_circle.draw()
    
#     for cell in cell_coords:
#         cell.draw()

#         if cell.x < mouse_circle.x:
#             cell.move_right()
#         else:
#             cell.move_left()

#         if cell.y < mouse_circle.y:
#             cell.move_down()
#         else:
#             cell.move_up()

#         x_distance = abs(cell.x-mouse_circle.x) 
#         y_distance = abs(cell.y-mouse_circle.y)

#         if x_distance > 150:
#             cell.x_speed = random.randrange(5, 12)
#         elif 50 < x_distance <= 150:
#             cell.x_speed = random.randrange(1, 5)
#         elif 0 < x_distance <= 50:
#             cell.x_speed = 0.5
#         else:
#             cell.x_speed = 0
        
#         if y_distance > 150:
#             cell.y_speed = random.randrange(5, 12)
#         elif 50 < y_distance <= 150:
#             cell.y_speed = random.randrange(1, 5)
#         elif 0 < y_distance <= 50:
#             cell.y_speed = 0.5
#         else:
#             cell.y_speed = 0


#     pygame.display.update()
#     clock.tick(30)
