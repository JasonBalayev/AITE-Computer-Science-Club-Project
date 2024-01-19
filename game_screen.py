import pygame
import sys
import random
from player_movement import Player
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

        bg_image = pygame.image.load("assets/vids/helloarn.jpg").convert_alpha()
        bg_image = pygame.transform.scale(bg_image, (self.screen_length, self.screen_height))

        player = Player(display)
        enemies = [Entity(random.randrange(-self.screen_length,0), random.randrange(-self.screen_height,0), display) for entity in range(3)]

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

            display.blit(bg_image, (0,0))

            mouse_coords = pygame.mouse.get_pos()
    
            for cell in player.cell_coords:
                
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
                    cell.y_speed = random.randrange(7, 12)
                elif 50 < y_distance <= 150:
                    cell.y_speed = random.randrange(4, 7)
                elif 0 < y_distance <= 50:
                    cell.y_speed = 3
                else:
                    cell.y_speed = 0

            player_tracker = (player.cell_coords[0].x, player.cell_coords[0].y)

            for entity in enemies:
                for cell in entity.cell_coords:
                
                    cell.draw()

                    if cell.x < player_tracker[0]:
                        cell.move_right()
                    else:
                        cell.move_left()

                    if cell.y < player_tracker[1]:
                        cell.move_down()
                    else:
                        cell.move_up()

                    x_distance = abs(cell.x-player_tracker[0]) 
                    y_distance = abs(cell.y-player_tracker[1])

                    if x_distance > 150:
                        cell.x_speed = random.randrange(10, 12)
                    elif 50 < x_distance <= 150:
                        cell.x_speed = random.randrange(6, 10)
                    elif 0 < x_distance <= 50:
                        cell.x_speed = 3
                    else:
                        cell.x_speed = 0
                    
                    if y_distance > 150:
                        cell.y_speed = random.randrange(10, 12)
                    elif 50 < y_distance <= 150:
                        cell.y_speed = random.randrange(6, 10)
                    elif 0 < y_distance <= 50:
                        cell.y_speed = 3
                    else:
                        cell.y_speed = 0

            for entity in enemies:
                for cell in entity.cell_coords:
                    
                    for player_cell in player.cell_coords:
                        
                        if cell.x-25 <= player_cell.x <= cell.x+25 and cell.y-25<= player_cell.y <= cell.y+25:
                            
                            player.cell_coords.pop()
                            entity.cell_coords.pop()

            pygame.display.update()
            clock.tick(FPS)

# GameScreen()