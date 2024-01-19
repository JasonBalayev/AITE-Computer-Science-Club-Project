import pygame
import sys
from start_screen import StartScreen
from transitions import ClubTransition
from transitions import InstructionsTransition
from game_screen import GameScreen
import turtle

if __name__ == "__main__":
    
    #press s key to skip through transitions

    StartScreen()
    ClubTransition()
    InstructionsTransition()
    GameScreen()
    