import pygame

class Grid():

    def __init__(self,width:int, height:int, tilesize = 10):
        self.w, self.h = (int)(width/tilesize), (int)(height/tilesize)
        self.tilesize = tilesize
        self.grid = [[0 for x in range(self.w)] for y in range(self.h)] 
    
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
                if self.grid[x][y] == 1:
                    pygame.draw.rect(rect=new_rect, color=(255, 255, 255), surface=screen)
                else:
                    pygame.draw.rect(rect=new_rect, color=(0,0,0), surface=screen)
    
    def on_click(self, mouse_pos):
        tile_x = (int)(mouse_pos[0]/10)
        tile_y = (int)(mouse_pos[1]/10)
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
        return count


    def iterate(self):
        for x in self.grid:
            for y in x:
                n = self.count_neighbors(x, y)
                if self.is_alive(x, y):
                    if n < 2 or n > 3:
                        self.grid[x][y] = 0
                    if n == 2 or n == 3:
                        self.grid[x][y] = 1
        
