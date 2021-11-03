import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
bird=pygame.Rect(100,250,30,30)
groundx=0
speed=0
def movedown():
    global speed
    gravity=0.2
    speed=speed+gravity
    bird.y=bird.y+speed
def moveup():
    global speed
    speed=speed-10
# Define a function 'printspeed()' to print the speed

    # Print the value of 'speed'
    
while True:  
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-550:
      groundx=0
  screen.blit(images["ground"],[groundx,550])
  movedown()
  screen.blit(images["bird"],bird)
  
  # Call the function 'printspeed()'
  
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
  
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_UP:
            moveup()  
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
