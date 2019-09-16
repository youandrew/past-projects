import pygame # learn more: https://python.org/pypi/Pygame
import random
import math
import time
from itertools import cycle
pygame.init()
pixels = 20
score = 0
diff = 1
clock = pygame.time.Clock()
musicChoice = "Regular.mp3"
lines = 0
grid = []
gridcolor = []
screen = pygame.display.set_mode((pixels * 10 + 100, pixels * 20))
blockI = [
    [[0,0,0,0],
    [1,2,1,1],
     
    [0,0,0,0],
    [0,0,0,0]]
    ,
    [[0,1,0,0],
    [0,2,0,0],
    [0,1,0,0],
    [0,1,0,0]]
    
          ] 
blockL = [
   [[0,0,0,0],
    [1,2,1,0],
    [1,0,0,0],
    [0,0,0,0]]
    ,
    [[1,1,0,0],
    [0,2,0,0],
    [0,1,0,0],
    [0,0,0,0]]
    ,
    [[0,0,1,0],
    [1,2,1,0],
    [0,0,0,0],
    [0,0,0,0]]
    ,
    [[0,1,0,0],
    [0,2,0,0],
    [0,1,1,0],
    [0,0,0,0]]
          ] 
blockO = [
   [ [0,0,0,0],
    [0,2,1,0],
    [0,1,1,0],
    [0,0,0,0]]
   
          ] 
blockS = [
   [ [0,0,0,0],
    [0,2,1,0],
    [1,1,0,0],
    [0,0,0,0]]
     ,
   [ [1,0,0,0],
    [1,2,0,0],
    [0,1,0,0],
    [0,0,0,0]]
    
    
          ] 
blockT = [
    [[0,0,0,0],
    [1,2,1,0],
    [0,1,0,0],
    [0,0,0,0]]
     ,
   [ [0,1,0,0],
    [1,2,0,0],
    [0,1,0,0],
    [0,0,0,0]]
    ,
    [[0,1,0,0],
    [1,2,1,0],
    [0,0,0,0],
    [0,0,0,0]]
    ,
   [ [0,1,0,0],
    [0,2,1,0],
    [0,1,0,0],
    [0,0,0,0]]
          ] 
blockZ =  [
   [ [0,0,0,0],
    [0,1,2,0],
    [0,0,1,1],
    [0,0,0,0]]
     ,
   [ [0,0,1,0],
    [0,0,2,1],
    [0,0,0,1],
    [0,0,0,0]]
   ]
   
blockJ =  [
   [[0,0,0,0],
    [0,1,2,1],
    [0,0,0,1],
    [0,0,0,0]]
    ,
   [ [0,0,1,1],
    [0,0,2,0],
    [0,0,1,0],
    [0,0,0,0]]
    ,
    [[0,1,0,0],
    [0,1,2,1],
    [0,0,0,0],
    [0,0,0,0]]
    ,
   [ [0,0,1,0],
    [0,0,2,0],
    [0,1,1,0],
    [0,0,0,0]]
          ]
    
          
blocks = [blockI, blockL, blockO, blockS, blockT, blockZ, blockJ]
colors = ["lightblue", "red", "orange", "yellow", "purple" , "green" , "blue"]
class DisplayBlock:
    def __init__(self,b,color):
        self.blocks = []
        self.color = color
        self.rotation = b[0]
        for count in range(len(self.rotation)): # read rotation block
            for j in range(len(self.rotation[count])):
                if self.rotation[count][j] == 1:
                    block = Block(j, count , self.color)
                    self.blocks.append(block)
                if self.rotation[count][j] == 2:
                    block = Block(j, count, self.color)
                    self.blocks.append(block)
    def Render(self):
        
        for count in range(len(self.blocks)):
            screen.blit(self.blocks[count].surface, ((self.blocks[count].x + 10) * pixels , (self.blocks[count].y + 15) * pixels))
class TetrisBlock:
    def __init__(self,b,color):
        self.matrix = b
        self.blocks = []
        self.origin = 0
        self.counter = 0
        self.color = color
        self.rotation = self.matrix[self.counter]
        self.ReadRotation()
        self.CheckIt()
        self.origin.x = 5 # set in middle
        self.origin.y = 1
        self.SetDifference()
    def Render(self):
        screen.blit(self.origin.surface, (self.origin.x * pixels, self.origin.y * pixels))
        for count in range(len(self.blocks)):
            screen.blit(self.blocks[count].surface, ((self.blocks[count].x) * pixels , (self.blocks[count].y) * pixels))
    def CheckIt(self):
        for count in range(len(self.blocks)): # set difference 
            self.blocks[count].diffx = self.origin.x - self.blocks[count].x
            self.blocks[count].diffy = self.origin.y - self.blocks[count].y
    def GoDown(self):
          canmove = True
          try:
              if (grid[self.origin.y + 1][self.origin.x] != 1):
                  pass
              else:
                  canmove = False  
              for count in range(len(self.blocks)):
                  if (grid[self.blocks[count].y + 1][self.blocks[count].x] != 1):
                      pass
                  else:
                      canmove = False
              if canmove:        
                  if (grid[self.origin.y + 1][self.origin.x] != 1):
                      self.origin.y += 1
                  for count in range(len(self.blocks)):
                      if (grid[self.blocks[count].y + 1][self.blocks[count].x] != 1):
                          self.blocks[count].y += 1
          except IndexError:
                canmove = False
          return canmove  
    def GoRight(self):
          yeet = True
          try:
              for count in range(len(self.blocks)):
                  if (grid[self.blocks[count].y][self.blocks[count].x +1] != 1):
                      pass
                  else:
                      yeet = False
                      break
              if (grid[self.origin.y][self.origin.x + 1] != 1 & yeet == True):
                  self.origin.x += 1
                  for count in range(len(self.blocks)):  
                      self.blocks[count].x += 1
          except IndexError:
                pass
    def GoLeft(self):
          yeet = True
          try:
              for count in range(len(self.blocks)):
                  if (grid[self.blocks[count].y][self.blocks[count].x - 1] != 1 and self.blocks[count].x != 0):   
                      pass
                  else:
                      yeet = False  
                      break
              if (grid[self.origin.y][self.origin.x - 1] != 1 & yeet == True):
                  self.origin.x += -1
                  for count in range(len(self.blocks)):
                      self.blocks[count].x += -1
          except IndexError:
                pass
    def SetDifference(self):
        needToMove = False
        needToMoveLeft = False
        for count in range(len(self.blocks)): # set difference
            self.blocks[count].x = self.origin.x + self.blocks[count].diffx
            self.blocks[count].y = self.origin.y + self.blocks[count].diffy
            if self.blocks[count].x == 10:
                needToMove = True
            if self.blocks[count].x == -1:
                needToMoveLeft = True
        if needToMove == True:
            self.origin.x += -1
            for count in range(len(self.blocks)):
                self.blocks[count].x += -1
        if needToMoveLeft == True:
            self.origin.x += 1
            for count in range(len(self.blocks)):
                self.blocks[count].x += 1
    def ReadRotation(self): # make sure to reset origin
        self.blocks = []
        
        for count in range(len(self.rotation)): # read rotation block
            for j in range(len(self.rotation[count])):
                if self.rotation[count][j] == 1:
                    block = Block(j, count , self.color)
                    self.blocks.append(block)
                if self.rotation[count][j] == 2:
                    block = Block(j, count, self.color)
                    self.origin = block
    def RotateLeft(self):
         self.counter += -1
         if self.counter == -1:
             self.counter = len(self.matrix) - 1
         self.rotation = self.matrix[self.counter]    
         tempx = self.origin.x
         tempy = self.origin.y
         self.ReadRotation()
         self.CheckIt()
         self.origin.x = tempx
         self.origin.y = tempy
         self.SetDifference()
               
    def RotateRight(self):
         self.counter += 1
         if self.counter == len(self.matrix):
             self.counter = 0
         self.rotation = self.matrix[self.counter]    
         tempx = self.origin.x
         tempy = self.origin.y
         
         self.ReadRotation()
         self.CheckIt()
         self.origin.x = tempx
         self.origin.y = tempy
         self.SetDifference()
             
    def HardDrop(self):
        global diff, score
        go = True
        asd = 0
        while go:
            go = self.GoDown()
            asd += 10 * diff
        score += asd
        return go

    def SetGrid(self):
          grid[self.origin.y][self.origin.x] = 1
          gridcolor[self.origin.y][self.origin.x] = self.origin.surface
          for count in range(len(self.blocks)):
                  grid[self.blocks[count].y][self.blocks[count].x] = 1
                  gridcolor[self.blocks[count].y][self.blocks[count].x] = self.blocks[count].surface
class Block:
    def __init__(self, x,y,color):
        self.x = x
        self.y = y
        self.diffx = 0
        self.diffy = 0
        self.surface = pygame.image.load(color+".png")

def End(cBlock):
    asd = False
    for counter in range(len(cBlock.blocks)):
        if grid[cBlock.blocks[counter].y][cBlock.blocks[counter].y] == 1:
            asd = True
    if grid[cBlock.origin.y][cBlock.origin.x] == 1:
        asd = True
    return asd
def CheckLines():
    global lines, score, diff
    yeet = True
    asd = 0
    ds = []
    for counter in range(len(grid)):
        for j in range(len(grid[counter])):
            if grid[counter][j] != 1:
                yeet = False
                         
        if yeet == True:
            lines += 1
            asd += 1
            ds.append(counter)
            for i in range(10):
                grid[counter][i] = 0
        yeet = True
        
    if(asd != 0):
        if asd == 4:
            score += 1200 * diff
        elif asd == 3:
            score +=  300 * diff
        elif asd == 2:
            score += 100 * diff
        elif asd == 1:
            score += 40 * diff
        for counter in reversed(range(max(ds))):
            
            for j  in range(len(grid[counter])):
              if grid[counter][j] == 1:
                  if counter + 1 != 20:      
                    grid[counter][j] = 0
                    grav = True
                    nasd = 1
                    
                    while grav:
                        if counter + nasd <= 20:
                            if grid[counter + nasd][j] == 0:
                                nasd += 1
                            else:
                                grav = False
                        else:
                            grav = False
                    print(nasd)       
                    gridcolor[counter + nasd][j] = gridcolor[counter][j]
                    gridcolor[counter][j] = 0
 
        asd = 0
def main():
    global lines, grid,gridcolor, score, diff
    lines = 0
    diff = 1
    grid = []
    gridcolor = []
    score = 0
    pygame.mixer.music.load(musicChoice)
    pygame.mixer.music.play(-1)
    # tetris record 79 950  # FIX BEING ABLE TO ROTATE OUT OF BOUNDS THANKS
    yeetDiff = 0
    
    run = True
    move = True
    downcounter = 0
    autodown = 0
        ######
    for x in range(20):
        row = []
        color = []
        for y in range(10): #I SNATCHED THIS BIT OF CODE FROM THE DEVIL(stackoverflow)
            row.append(0)
            color.append(0)
        grid.append(row)
        gridcolor.append(color)

      
#######
    prevRn = random.randint(0,6)
    rn = random.randint(0,6)
    nextblock = DisplayBlock(blocks[rn],colors[rn])
    currentblock = TetrisBlock(blocks[prevRn], colors[prevRn])
    run = True
    forwhat = pygame.font.SysFont(None,20,True,True)
    while run:
         yeetDiff += 1
         if yeetDiff == 10000:
             diff += 1
             yeetDiff = 0
         levelimage = forwhat.render("Level" + " " + str(diff), False,(255,0,0))    
         fontimage = forwhat.render("Lines" + " " + str(lines), False, (255,0,0))
         scoreImage = forwhat.render("Score" + " " + str(score), False, (255,0,0))
         autodown += 1
         if autodown >= 25 / diff:
             autodown = 0
             move = currentblock.GoDown()
         screen.fill((0,0,0))
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        currentblock.RotateRight()
                    if event.key == pygame.K_a:
                        currentblock.RotateLeft()
                    if event.key == pygame.K_LEFT:
                        currentblock.GoLeft()
                    if event.key == pygame.K_RIGHT:
                        currentblock.GoRight()
                    if event.key == pygame.K_SPACE:
                        move = currentblock.HardDrop()
         keys = pygame.key.get_pressed()
         downcounter += 1
         if keys[pygame.K_DOWN]:
                if downcounter >= 5:
                    downcounter = 0
                    move = currentblock.GoDown()
         if move == False:
             move = True
             currentblock.SetGrid()
             prevRn = rn
             currentblock = TetrisBlock(blocks[prevRn], colors[prevRn])
             rn = random.randint(0,6)
             nextblock = DisplayBlock(blocks[rn], colors[rn])
             CheckLines()
             if End(currentblock):
                 run = False
                 GameEnd()
         for counter in range(len(grid)): 
             for j in range(len(grid[counter])):
               
                 if grid[counter][j] == 1:
                     screen.blit(gridcolor[counter][j], (j * pixels,counter * pixels))
         currentblock.Render()
         nextblock.Render()
         screen.blit(fontimage,(200, 50))
         screen.blit(scoreImage, (200,100))
         screen.blit(levelimage,(200,150))
         clock.tick(60)
         pygame.display.flip()
    pygame.mixer.music.stop()   
def GameEnd():
    global musicChoice
    
    yeet = pygame.Surface((75,75))
    forwhat = pygame.font.SysFont(None,20,True,True)
    rect = pygame.Rect(100,200,75,75)
    asd = True
    r = 0
    g = 0
    b = 0 # 200 by 400
    i = 0
    fontimage = forwhat.render("Tetris", False, (255,0,0))

    seinfeldSurface = pygame.Surface((75,75))
    seinfeldRect = pygame.Rect(0,0,75,75)
    seinfeldFont = forwhat.render("Seinfeld", False, (255,0,0))
    regularSurface = pygame.Surface((75,75))
    regularRect = pygame.Rect(0,80,75,75)
    regularFont = forwhat.render("Regular", False, (255,0,0))
    while asd: 
        screen.fill((r,g,b))
        yeet.fill((r,b,g))
        seinfeldSurface.fill((g,r,b))
        regularSurface.fill((g,r,b))
        screen.blit(seinfeldSurface,(0,0))
        screen.blit(regularSurface,(0,80))
        screen.blit(yeet,(100,200))
        screen.blit(fontimage,(100,200))
        screen.blit(seinfeldFont,(0,0)) # r g b  : r b g : b r g : b g r : g r b : g b r
        screen.blit(regularFont,(0,80))
        fontimage = forwhat.render("TETRIS", False, (b,r,g))
        seinfeldFont = forwhat.render("Seinfeld", False, (b,g,r))
        regularFont = forwhat.render("Regular", False, (g,b,r))
        r  = math.sin(0.5*i + 0) * 127 + 128;
        g = math.sin(0.5*i + 2) * 127 + 128;
        b  = math.sin(0.5*i + 4) * 127 + 128;
        i += 0.1
        if i == 32:
            i = 0 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                asd = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x , y = pygame.mouse.get_pos()
                    if rect.collidepoint(x,y):
                        main()
                    if seinfeldRect.collidepoint(x,y):
                        
                        musicChoice = "Seinfeld.mp3"
                    if regularRect.collidepoint(x,y):
                        musicChoice = "Regular.mp3"
        clock.tick(60)
        pygame.display.flip()

GameEnd()
