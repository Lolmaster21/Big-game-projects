#initializes library
#slither written by Lukas Henriquez 1/28/2021
import pygame
import math
import random
pygame.init()

#Opens a window
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Slither buggo") 
clock = pygame.time.Clock()

#game variable
doExit= False

#player variable
xPos = 350 #X position
yPos = 200 #Y position
Vx = 1 #Horizontal speed
Vy = 1 #Vertical speed
#player 2 variable
xPos2 = 350 #X position
yPos2 = 200 #Y position
Vx2 = 1 #Horizontal speed
Vy2 = 1 #Vertical speed


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Tailseg:
  def __init__(self,xpos,ypos):
    self.xpos = xpos
    self. ypos = ypos
  def update(self,xpos,ypos):
    self.xpos = xpos
    self.ypos = ypos
  def draw(self):
    pygame.draw.circle(screen,(200,0,0),(self.xpos,self.ypos),12)  
  def collide(self,x,y):
    if math.sqrt((x-self.xpos)*(x-self.xpos)+(y-self.ypos)*(y-self.ypos)<6):
      return True  

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++
class pellet:
  def __init__(self,xpos,ypos,red,blue,green,radius):
    self.xpos= xpos
    self.ypos= ypos
    self.red= red
    self.blue= blue
    self.green= green
    self.radius= radius
  def draw(self):
    pygame.draw.circle(screen,(self.red,self.green,self.blue),(self.xpos,self.ypos),self.radius)
  def collide(self,x,y):
    if math.sqrt((x-self.xpos)*(x-self.xpos)+(y-self.ypos)*(y-self.ypos)) <self.radius + 6:
      self.xpos = random.randrange(0,400)
      self.ypos = random.randrange(0,400)
      self.red  = random.randrange(0,255)
      self.blue = random.randrange(0,255)
      self.green = random.randrange(0,255)
      self.radius = random.randrange(5,30)  
      return True
#end of pellet class++++++++++++++++++++++++++++++++++++
pelletBag= list()#It creates more lists of 
tail= list()
tail2 = list()
#pushing 10 pallets into the list

for i in range(10):
    pelletBag.append(pellet(random.randrange(0,400),random.randrange(0,400), random.randrange(1,255),random.randrange(1,255),random.randrange(1,255),random.randrange(5,30)))
oldx = 200
oldy = 200
oldx2 = 200
oldy2 = 200

counter = 0    


#gameloop##############################################
while not doExit:

#Event/input section----------------------------------
  clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      doExit = True
  if event.type == pygame.MOUSEMOTION:
    mousePos = event.pos  

    if mousePos[0]>xPos:
      Vx = 1
    else:
        Vx = -1
    if mousePos[1]>yPos:
      Vy = 1
    else:
        Vy = -1   

  #player 2 movement
  keys = pygame.key.get_pressed()
  if keys [pygame.K_LEFT]:
    xPos2 += -1
  if keys [pygame.K_RIGHT]:
    xPos2 -= -1 
  if keys [pygame.K_UP]:
    yPos2 -= 1
  if keys [pygame.K_DOWN]:
    yPos2 += 1           
#counter time--------------------------------------------
  counter+=1#update counter
  if counter == 20: #create a delay 
    counter = 0 #reset counter
    oldx = xPos
    oldy = yPos
    oldx2 = xPos2
    oldy2 = yPos2

    if(len(tail)>2):
      for i in range(len(tail)):
        tail[len(tail)-i-1].xpos = tail[len(tail)-i-2].xpos
        tail[len(tail)-i-1].ypos = tail[len(tail)-i-2].ypos
    if(len(tail2)>2):
      for i in range(len(tail2)):
        tail2[len(tail2)-i-1].xpos = tail2[len(tail2)-i-2].xpos
        tail2[len(tail2)-i-1].ypos = tail2[len(tail2)-i-2].ypos    
        

    if(len(tail)>0):
      tail[0].update(oldx,oldy)
    if(len(tail2)>0):
      tail2[0].update(oldx2,oldy2)  


#physics section--------------------------------------
  #updated circle position
  xPos += Vx
  yPos += Vy
  
  for i in range(10):
    if pelletBag[i].collide(xPos,yPos)==True:
      tail.append(Tailseg(oldx,oldy)) 
    if pelletBag[i].collide(xPos2,yPos2)==True:
      tail2.append(Tailseg(oldx2,oldy2))
  for i in range(len(tail2)):
    if tail2[i].collide(xPos,yPos) == True:
      print("Player 1 hit player 2!!!")
      doExit = True
  for i in range(len(tail)):     
    if tail[i].collide(xPos2,yPos2) == True:
      print("Player 2 hit player 1!!!")
      doExit = True         

#render section---------------------------------------
  screen.fill((0,0,0))
  
  for i in range(len(tail)):
    tail[i].draw()

  for i in range(len(tail2)):
    tail2[i].draw()  

  for i in range(10):
    pelletBag[i].draw()

  pygame.draw.circle(screen,(200,0,200),(xPos,yPos),12)

  pygame.draw.circle(screen,(200,0,200),(xPos2,yPos2),12)

  pygame.display.flip()


#end of game loop######################################
pygame.quit()
