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

#colors
BLACK = (0, 0, 0)
GOLD = (194, 148, 83)
RED = (161, 73, 67)
WHITE = (255, 255, 255)
DARK_GRAY = (30, 30, 30)
BASE = (107, 106, 105)
LIGHT_GRAY = (217, 217, 217)
BRIGHT_GOLD = (255, 215, 0)

# high score that will be tracked
SAVED_HIGH_SCORE = 0

# added the images into the GUI
pony_images = [pygame.image.load("FLAPPY/assets/pony_up.png"), pygame.image.load("FLAPPY/assets/pony_mid.png"), pygame.image.load("FLAPPY/assets/pony_down.png")]
skyline_image = pygame.image.load("FLAPPY/assets/background.png")
ground_image = pygame.image.load("FLAPPY/assets/ground.png")
top_fence_image = pygame.image.load("FLAPPY/assets/fence_top.png")
bottom_fence_image = pygame.image.load("FLAPPY/assets/fence_bottom.png")
game_over_image = pygame.image.load("FLAPPY/assets/game_over.png")
start_image = pygame.image.load("FLAPPY/assets/start.png")

#game - sets the scroll speed, pony position, settings score & changing the score, and
# puts the fonts on there
scroll_speed = 4
last_speedup_score = 0
fence_lower = 45
fence_higher = 62
pony_start_position = (100, 160)
score = 0
high_score = SAVED_HIGH_SCORE
score_font = pygame.font.FONT("FLAPPY/assets/PressStart2P-Regular.ttf", 14)
small_font = pygame.font.FONT("FLAPPY/assets/PressStart2P-Regular.ttf", 10)
game_stopped = True

# Function to update high score in the file
def update_high_score_in_file(new_high_score):
  """Update the high score directly in the script file"""
  try:
    #Getting the path to the current script
    script_path = os.path.abspath(__file__)

    #Read the file
    with open(script_path, 'r') as f:
      content = f.read()

    new_content = re.sub(r'SAVED_HIGH_SCORE = \d+', f'SAVED_HIGH_SCORE = {new_high_score}', content)

    # Write the updated content back to the file
    with open(script_path, 'w') as f:
        f.write(new_content)

        return True
  except Exception as e:
      print(f"Failed to update high score: {e}")
      return False
# ENDED HERE CONTINUE CODING FROM HERE
# Pony Class goes here

# Fence Class
class Fence(pygame.sprite.Sprite):
    def __init__(self, x, y, image, fence_type): # takes coordinates of fence, image
        pygame.sprite.Sprite.__init__(self) #initialize parent class
        self.image = image # = to image we are passing in agrs
        # conveinent for checking for collisions
        self.rect = self.image.get_rect() # manipulate position of img
        self.rect.x, self.rect.y = x, y # set xy coords of img = to the xy coords we pass in agrs
        self.enter, self.exit, self.passed = False, False, False
        self.fence_type = fence_type

    def update(self): # responsible for moving fences from left to right side of screen
        # move fences
        self.rect.x -= scroll_speed
        if self.rect.x <= -SCREEN_WIDTH:
            self.kill()

        global score
        if self.fence_type == "bottom":
            if pony_start_position[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if pony_start_position[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                score += 1
# exiting game
def quit_game():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
