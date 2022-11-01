import pygame
import random
pygame.init()

screen= pygame.display.set_mode((700,500))
pygame.display.set_caption("Card game: War")
class card:
  def __init__(self,suit,number):
    self.suit = suit
    self.number = number
  def draw(self,x,y):
    pygame.draw.rect(screen,(255,255,255),(x,y,100,180))
    pygame.draw.rect(screen,(0,0,0),(x,y,100,180),3)
    font = pygame.font.Font('freesansbold.ttf',24)
    text = font.render(str(self.number),1,(0,0,0))
    text2 = font.render(str(self.suit),1,(250,0,0))
    screen.blit(text, (x+30, y+30))
    screen.blit(text2, (x+10, y+60))
#Card drawing---------------------------------------
 
 
 

#Deck----------------------------------------------
Deck = list()
for j in range(4):
  for i in range(13):
    Deck.append(card(j,i))

random.shuffle(Deck)

#breaks players hands
p1hand = list()
p2hand = list()
p1Discard = list()
p2Discard = list()

for i in range(26):
  p1hand.append(Deck[i])
for j in range(26,52):
  p2hand.append(Deck[j])




doExit = False
clock = pygame.time.Clock()
Turn = False

while not doExit: #Gameloop------------------

  clock.tick(60)
  
  event = pygame.event.wait()

  if event.type == pygame.QUIT: 
    doExit = True
  
  if event.type == pygame.MOUSEBUTTONDOWN:
    Turn = True
    print("mouse button down, turn true")
  if event.type == pygame.MOUSEBUTTONUP:
    Turn = False     
  if event.type == pygame.MOUSEMOTION:
    mousePos = event.pos  


  #Game logic--------------------------------------------
  if len(p1hand) <=0 or len(p2hand) <=0:
    if len(p1Discard)>len(p2Discard):
      print("Player 1 has won this round!!!")
    else:
      print("Player 2 has won this round!!!")
    doExit = True

  if Turn and len(p1hand)>0 and len(p2hand)>0:
    
    if p1hand[len(p1hand)-1].number>p2hand[len(p2hand)-1].number:
      print("Congrats Player 1 wins!!!")
      p1Discard.append(p1hand[len(p1hand)-1])
      p1Discard.append(p2hand[len(p2hand)-1])
      p1hand.pop(len(p1hand)-1)
      p2hand.pop(len(p2hand)-1)

    else:
      print("Congrats Player 2 wins!!!")
      p2Discard.append(p1hand[len(p1hand)-1])
      p2Discard.append(p2hand[len(p2hand)-1])
      p1hand.pop(len(p1hand)-1)
      p2hand.pop(len(p2hand)-1)

#Render section------------------  
  screen.fill((0,150,0))


  
  for i in range(0,len(p1hand)):
    p1hand[i].draw(400+4*i ,50)

  for i in range(0,len(p2hand)):
    p2hand[i].draw(400+4*i,250)

  for i in range(0,len(p1Discard)):
    p1Discard[i].draw(400,50) 

  for i in range(0,len(p2Discard)):
    p2Discard[i].draw(400,250)    
 

#Update the scren----------------------------
  pygame.display.flip()

pygame.quit()
