import obj
import pygame

  
background_colour = (200,200,199)
phone_colour=(26,23,24)

pygame.init()

surface = pygame.display.set_mode((260, 520))
pygame.display.set_caption('Mobiles Endgerät')
  
surface.fill(background_colour)
  
pygame.display.flip()
  
running = True

pygame.draw.rect(surface, phone_colour, pygame.Rect(5, 0, 250, 490),0,10,10,10,10)
pygame.draw.circle(surface,phone_colour,(130,505),14)
pygame.display.flip()



istAn = False
meinHandy = obj.Handy()

while running:

    print()
  
    for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
            running = False

    print("""
[1] Betriebstaste
[2] Screensaver
    """)
    inp = input("Geben Sie Ihre gewünschte Funktion ein:\n>>> ").lower()
    if inp in ("1", "betriebstaste"):
        
        if istAn:
            maxi = meinHandy.ausschalten()
        else:
            maxi = meinHandy.einschalten()
        
        display_farbe = maxi[1]
        istAn = maxi[0]
        
        pygame.draw.rect(surface, display_farbe, pygame.Rect(5, 0, 250, 490),0,10,10,10,10)
    elif inp in ("2","bildschirmschoner"):
        hbs=obj.Bildschirmschoner()
        pygame.draw.rect(surface, hbs.aktivieren(), pygame.Rect(5, 0, 250, 490),0,10,10,10,10)
        for i in range(100):
            surface.fill(background_colour) 
            pygame.draw.rect(surface, hbs.aktivieren(), pygame.Rect(5, 0, 250, 490),0,10,10,10,10)
            pygame.draw.circle(surface,phone_colour,(130,505),14)  
            c1 = pygame.draw.circle(surface,hbs.blasen,(25,475-5*i),15)
            c2 = pygame.draw.circle(surface,hbs.blasen,(76,469-5*i),21)
            c3 = pygame.draw.circle(surface,hbs.blasen,(179,466-5*i),24)
            c4 = pygame.draw.circle(surface,hbs.blasen,(235,474-5*i),16)
            pygame.display.update()
            pygame.time.delay(250)
            
    elif inp in ("3", "telefonbuch"):
        buch = obj.Telefonbuch()
        print("""
[1] Hinzufügen
[2] Suchen
        """)
        inp = input("Geben Sie Ihre gewünschte Funktion ein:\n>>> ").lower()
        if inp in ("1", "hinzufügen"):
            
            buch.eingabe(name, nummer)
        elif inp in ("1", "suchen"):
            ...
    pygame.display.update()  
  