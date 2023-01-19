import pygame
from math import *
import time
pygame.init()  
pygame.display.set_caption("Space Invaders")  # sets the window title
screen = pygame.display.set_mode((1000, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock

#player
keys = [False, False, False]
#CONSTANTS
LEFT=0
RIGHT=1


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

class spaceship:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.alive = True
        self.vx = 0

    def move(self):
        if keys[0]==True:
            vx=3
        elif keys[1]==True:
            vx =-3
        else:
            vx = 0

        xpos+=vx
            
    def draw(self):
        if self.alive is True:
            pygame.draw.rect(screen, (0, 255,0), (self.xpos,self.ypos, 100, 20))

#instantiate a spaceship object from the class
idk = spaceship(450,750)

while True:  
    clock.tick(60)

    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True

            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True

                #Player 1 Input
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

                
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False 

    #physics section-------------------------------------------


    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    idk.draw()
    
    

    pygame.display.flip()#this actually puts the pixel on the screen
    
pygame.quit()
