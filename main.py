import pygame
import numpy as np
from grid import Grid

# pygame setup
pygame.init()
width, height = 500, 500
grid = Grid(500,500)
# grid.checkerboard()
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
            mouse_pos = pygame.mouse.get_pos()
            grid.on_click(mouse_pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_simulation = not start_simulation
            if event.key == pygame.K_c:
                grid.checkerboard()
            # if event.key == pygame.K_r:
            #     grid.grid = np.zeros((500,500))
            # if event.key == pygame.K_s:
            #     grid.grid = np.random.choice([0,1], size=(500,500), p=[0.9,0.1]).tolist()
    
    if(start_simulation):
        grid.iterate()
        pygame.time.wait(10)    

    grid.draw(screen)
    pygame.display.flip()    
    clock.tick(60)

pygame.quit()