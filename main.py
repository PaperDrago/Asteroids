# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    i = 0
    while i == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()