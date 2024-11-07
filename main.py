import pygame
import numpy as np
from grid import Grid

# pygame setup
pygame.init()
width, height = 500, 500
grid = Grid(500,500)
grid.checkerboard()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
start_simulation = False

pixels = pygame.PixelArray(screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse was pressed")
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            grid.on_click(mouse_pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space was pressed")
                start_simulation = not start_simulation
    
    # RENDER YOUR GAME HERE
    if(start_simulation):
        grid.iterate()

    # get mouse position
    
    # flip() the display to put your work on screen

    grid.draw(screen)

    pygame.display.flip()    

    clock.tick(60)  # limits FPS to 60

pygame.quit()