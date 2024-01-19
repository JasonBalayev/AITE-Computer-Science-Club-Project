import pygame
import sys
import cv2
from button import Button

class StartScreen:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode()
        self.clock = pygame.time.Clock()

        DISPLAY_SIZE = self.display.get_size()

        self.screen_length = DISPLAY_SIZE[0]
        self.screen_height = DISPLAY_SIZE[1]

        self.run_button_length = self.screen_length / 5
        self.run_button_height = self.screen_height / 15
        self.run_button_x = (self.screen_length / 2) - (1.25*self.run_button_length)
        self.run_button_y = (self.screen_height / 2) - (self.run_button_height)

        self.start_button_img = pygame.image.load("assets/ui_img_start_button.png").convert_alpha()
        self.button = Button(self.run_button_x, self.run_button_y, self.start_button_img, 1)

        video = cv2.VideoCapture("assets/vids/game_logo.mov")
        success, video_image = video.read()
        FPS = video.get(cv2.CAP_PROP_FPS)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.display.iconify()

            self.display.fill("black")            

            success, video_image = video.read()
            if success:
                video_surf = pygame.image.frombuffer(
                    video_image.tobytes(), video_image.shape[1::-1], "BGR")
                video_surf = pygame.transform.smoothscale(video_surf, (self.screen_length, self.screen_height))
            
            self.display.blit(video_surf, (0,100))
            self.button.draw(self.display)

            if self.button.clicked == True:
                running = False

            pygame.display.update()