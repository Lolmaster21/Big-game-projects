import pygame
pygame.init()  
pygame.display.set_caption("Space Invaders")  # sets the window title
screen = pygame.display.set_mode((1000, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
SPACE = 2
shoot = False

#player variables
xpos = 430 #xpos of player
ypos = 750 #ypos of player
vx = 0 #x velocity of player
timer = 0;

keys = [False, False, False, False,False, False, False, False] #this list holds whether each key has been pressed
#this list holds whether each key has been pressed

class Bullet:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = False
    
    def move(self,xpos,ypos):
        if self.isAlive == True:
            self.ypos -= 5
        if self.ypos < 0:
            self.isAlive = False
            self.xpos = xpos
            self.ypos = ypos
            
    def draw(self):
        pygame.draw.rect(screen,(250,250,250),(self.xpos,self.ypos,3,20))


bullet = Bullet(xpos+28,ypos)

        
class Alien:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
        self.direction = 1
    
    def draw(self):
        if self.isAlive == True:
            pygame.draw.rect(screen,(250,250,250),(self.xpos,self.ypos, 40,40))
        
        if self.isAlive == False:
            return False
            print("dead")
            
    def move(self,time):
        
        if time % 800 == 0:
            self.ypos += 100
            self.direction *=-1
            return 0
    
        if timer %100 == 0:
            self.xpos += 35*self.direction
        
        return time
    
    def collide(self, BulletX, BulletY):
        if self.isAlive:
            if BulletX > self.xpos:
                if BulletX < self.xpos + 40:
                    if BulletY < self.ypos + 40:
                        if BulletY > self.ypos:
                            print("HIT")
                            self.isAlive = False
                            return False
        return True #otherwise  keep bullet alive
            
               

bob = []
for i in range(4):
    for j in range(10):
        bob.append(Alien(j*70+50, i*70+30))
        
   

while not gameover: #GAME LOOP------------------------------------------------
    clock.tick(100) #FPS
    timer += 1
    
    
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True

            if event.key == pygame.K_SPACE:
                keys[SPACE]=True
                shoot = True

            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
          
                    
# Input KEYUP
            
        #Player 1 Input
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=False

            if event.key == pygame.K_SPACE:
                keys[SPACE]= False
                shoot = False

            
   

  

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
    
    
    #Physics section--------------------------------------------------------------
    for i in range(len(bob)):
        bob[i].move(timer)     


  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    #Draws player
    bullet.draw()

    
    #Player 1
    pygame.draw.rect(screen, (0, 250,0), (xpos, 750, 60, 20))
    pygame.draw.rect(screen, (0, 250,0), (xpos+5, 745, 50, 20))
    pygame.draw.rect(screen, (0, 250,0), (xpos+25, 736, 10, 20))
    pygame.draw.rect(screen, (0, 250,0), (xpos+28, 732, 4, 20))

    
        
   #shoot bullet
    if shoot == True:
        bullet.isAlive = True
    
    if bullet.isAlive == True:
        bullet.move(xpos+28, ypos)
        if bullet.isAlive == True:
            
            for i in range (len(bob)):
                bullet.isAlive = bob[i].collide(bullet.xpos, bullet.ypos)
                if bullet.isAlive == False:
                    break
    else:
        bullet.xpos = xpos + 28
        bullet.ypos = ypos 
    
    


      

    #Enemy call function
    for i in range (len(bob)):
        bob[i].draw()

  

    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
