
import pygame
  
background_colour = (26,23,24)

screen = pygame.display.set_mode((300, 500))
pygame.display.set_caption('Mobiles Endgerät')
  
screen.fill(background_colour)
  
pygame.display.flip()
  
running = True
  

while running:
  for event in pygame.event.get():
      
    if event.type == pygame.QUIT:
      running = False