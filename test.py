import pygame
import sys
import random
from entity_generation import Entity

class GameScreen:
    def __init__(self):
            
        pygame.init()

        display = pygame.display.set_mode()
        clock = pygame.time.Clock()

        FPS = 30
        DISPLAY_SIZE = display.get_size()
        self.screen_length = DISPLAY_SIZE[0]
        self.screen_height = DISPLAY_SIZE[1]
        
        pygame.mixer.init()
        pygame.mixer.music.load("assets/vids/game_audio.mp3")
        pygame.mixer.music.play()

        entity = Entity(250, 250, display)

        running = True

        while running == True:

            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.display.iconify()

           

            display.fill("black")

            mouse_coords = (0,0)
    
            for cell in entity.cell_coords:
            
                cell.draw()

                if cell.x < mouse_coords[0]:
                    cell.move_right()
                else:
                    cell.move_left()

                if cell.y < mouse_coords[1]:
                    cell.move_down()
                else:
                    cell.move_up()

                x_distance = abs(cell.x-mouse_coords[0]) 
                y_distance = abs(cell.y-mouse_coords[1])

                if x_distance > 150:
                    cell.x_speed = random.randrange(5, 12)
                elif 50 < x_distance <= 150:
                    cell.x_speed = random.randrange(1, 5)
                elif 0 < x_distance <= 50:
                    cell.x_speed = 0.5
                else:
                    cell.x_speed = 0
                
                if y_distance > 150:
                    cell.y_speed = random.randrange(5, 12)
                elif 50 < y_distance <= 150:
                    cell.y_speed = random.randrange(1, 5)
                elif 0 < y_distance <= 50:
                    cell.y_speed = 0.5
                else:
                    cell.y_speed = 0


            pygame.display.update()
            clock.tick(FPS)

GameScreen()