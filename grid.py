import pygame
import numpy as np

class Grid():

    def __init__(self,width:int, height:int, tilesize = 2, spawn_rule = [3], kill_rule = [0,1,4,5,6,7,8,9], mono_color = False):
        self.w, self.h = (int)(width/tilesize), (int)(height/tilesize)
        self.tilesize = tilesize
        self.grid = [[0 for x in range(self.w)] for y in range(self.h)] 
        self.colors = [[(255,255,255) for x in range(self.w)] for y in range(self.h)] 
        self.spawn_rule = spawn_rule
        self.kill_rule = kill_rule
        self.color = (100,200,255)
        self.mono_color = mono_color
    
    def add(self, x:int, y:int):
        self.grid[x][y] = 1
        
    def rm(self, x:int, y:int):
        self.grid[x][y] = 0

    def switch(self, x:int, y:int):
        if self.grid[x][y] == 0:
            self.grid[x][y] = 1
        else:
            self.grid[x][y] = 0


    def checkerboard(self):
        for x in range(self.w):
            for y in range(self.h):
                if (x+y)%2 == 0:
                    self.grid[x][y] = 1
                else:
                    self.grid[x][y] = 0

    def draw(self, screen):
        for x in range(self.w):
            for y in range(self.h):
                new_rect = pygame.Rect(x*self.tilesize, y*self.tilesize, self.tilesize, self.tilesize)
                if self.mono_color:
                    if self.grid[x][y] == 1:
                        pygame.draw.rect(rect=new_rect, color=self.color, surface=screen)
                    else:
                        pygame.draw.rect(rect=new_rect, color=(0,0,0), surface=screen)
                else:
                    if self.grid[x][y] == 1:
                        pygame.draw.rect(rect=new_rect, color=self.colors[x][y], surface=screen)
                    else:
                        pygame.draw.rect(rect=new_rect, color=(0,0,0), surface=screen)

    def on_click(self, mouse_pos):
        tile_x = (int)(mouse_pos[0]/self.tilesize)
        tile_y = (int)(mouse_pos[1]/self.tilesize)
        self.switch(tile_x,tile_y)


    def is_alive(self, x:int, y:int):
        try:
            if self.grid[x][y] == 1:
                return 1
            else:
                return 0
        except:
            return 0


    def count_neighbors(self, x:int, y:int):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                count += self.is_alive(x+i, y+j)
                # if self.is_alive(x, y) == 1:
                    # print(f"{count} Total; counted {self.is_alive(x+i, y+i)} at {x+i} {y+i}")
        return count


    def iterate(self):
        old_grid = self.grid.copy()

        for row in enumerate(self.grid):
            for col in enumerate(row[1]):
                x = row[0]
                y = col[0]
                n = self.count_neighbors(x, y)
                if self.is_alive(x, y):
                    if n in self.kill_rule:
                        self.grid[x][y] = 0
                    else:
                        self.colors[x][y] = np.array(self.colors[x][y]) * np.array((0.7,0.8,0.9)) + np.array((20,20,20))
                else:
                    if n in self.spawn_rule:
                        self.grid[x][y] = 1
                        self.colors[x][y] =  (255,255,255)


        self.grid = old_grid.copy()
        
