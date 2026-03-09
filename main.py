import pygame
from sys import exit
import random
import os
import re

pygame.init()

# screen dimensions
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# high score that will be tracked
SAVED_HIGH_SCORE = 0

# added the images into the GUI
pony_images = [pygame.image.load("flappygame/assets/pony_up.png"), pygame.image.load("flappygame/assets/pony_mid.png"), pygame.image.load("flappygame/assets/pony_down.png")]
skyline_image = pygame.image.load("flappygame/assets/background.png")
ground_image = pygame.image.load("flappygame/assets/ground.png")
top_fence_image = pygame.image.load("flappygame/assets/fence_top.png")
bottom_fence_image = pygame.image.load("flappygame/assets/fence_bottom.png")
game_over_image = pygame.image.load("flappygame/assets/game_over.png")
start_image = pygame.image.load("flappygame/assets/start.png")

# exiting game
def quit_game():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
