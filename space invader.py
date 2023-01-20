import pygame
from math import *
import time
pygame.init()  
pygame.display.set_caption("Space Invaders")  # sets the window title
screen = pygame.display.set_mode((1000, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock


#CONSTANTS
LEFT=0
RIGHT=1

#player variables
xpos = 430 #xpos of player
ypos = 750 #ypos of player
vx = 0 #x velocity of player
keys = [False, False, False]




class Enemy:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isOnGround = False
        self.alive = True
    def draw(self):
        self.color = (138 +random.randint(-10,10), 23 +random.randint(-10,10), 17 +random.randint(-10,10))
        self.color2 = (138-22, 23-12, 17-10)
        if self.alive is True:
            pygame.draw.ellipse(screen, self.color, (self.xpos, self.ypos, 100, 80))
            pygame.draw.arc(screen, self.color2, (self.xpos+10, self.ypos-16, 110, 115), (5*math.pi)/6, (7*math.pi)/6, 5)
            pygame.draw.arc(screen, self.color2, (self.xpos+30, self.ypos-36, 110, 150), (5*math.pi)/6, (7*math.pi)/6, 5)
            pygame.draw.arc(screen, self.color2, (self.xpos-22, self.ypos-16, 110, 115), (11*math.pi)/6, (math.pi)/6, 5)
            pygame.draw.arc(screen, self.color2, (self.xpos-42, self.ypos-36, 110, 150), (11*math.pi)/6, (math.pi)/6, 5)
            pygame.draw.arc(screen, ((22, 100, 8)), (self.xpos+45, self.ypos-51, 110, 115), (5*math.pi)/6, (math.pi), 8)
            pygame.draw.ellipse(screen, ((0, 0, 0)), (self.xpos, self.ypos, 100, 80), 5)


while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True

            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
          
                    
# Input KEYUP
            
        #Player 1 Input
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
  

    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
        
  

    #RIGHT MOVEMENT
    elif keys[RIGHT]==True:
        vx=3
        direction = RIGHT

    #turn off velocity
    else:
        vx = 0

    #update player position
    xpos+=vx 
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    #Player 1
    pygame.draw.rect(screen, (0, 250,0), (xpos, ypos, 80, 20))
  

    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
