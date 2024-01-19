import pygame
import sys
import cv2

class ClubTransition:
    def __init__(self):
        video = cv2.VideoCapture("assets/vids/aite_glitch.mov")
        success, video_image = video.read()
        fps = video.get(cv2.CAP_PROP_FPS)

        window = pygame.display.set_mode()
        clock = pygame.time.Clock()

        pygame.mixer.init()
        pygame.mixer.music.load("assets/vids/aite_glitch_audio.mp3")
        pygame.mixer.music.play()

        run = success
        while run:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.display.iconify()
                    if event.key == pygame.K_s:
                        run = False
            
            success, video_image = video.read()
            if success:
                video_surf = pygame.image.frombuffer(
                    video_image.tobytes(), video_image.shape[1::-1], "BGR")
                video_surf = pygame.transform.smoothscale(video_surf, (window.get_size()[0],window.get_size()[1]))
            else:
                run = False
            
            window.blit(video_surf, (0, 0))
            pygame.display.flip()

class InstructionsTransition:
    def __init__(self):
        video = cv2.VideoCapture("assets/vids/instructions.mp4")
        success, video_image = video.read()
        fps = video.get(cv2.CAP_PROP_FPS)

        window = pygame.display.set_mode()
        clock = pygame.time.Clock()

        run = success
        while run:
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.display.iconify()
                    if event.key == pygame.K_s:
                        run = False
            
            success, video_image = video.read()
            if success:
                video_surf = pygame.image.frombuffer(
                    video_image.tobytes(), video_image.shape[1::-1], "BGR")
                video_surf = pygame.transform.smoothscale(video_surf, (window.get_size()[0],window.get_size()[1]))
            else:
                run = False
            
            window.blit(video_surf, (0, 0))
            pygame.display.flip()

        # pygame.quit()
        # exit()
