import obj
import pygame
import random

handy_x = obj.Handy()
button_color = handy_x.homefarbe
phone_color = handy_x.randfarbe
test_colour = handy_x.testfarbe

pygame.init()

surface = pygame.display.set_mode((260, 520))
pygame.display.set_caption('Mobiles Endgerät')
surface.fill(phone_color)
pygame.display.flip()

running = True

pygame.draw.rect(surface, phone_color, pygame.Rect(5, 0, 250, 490), 0, 10, 10,10, 10)
pygame.draw.rect(surface, phone_color, pygame.Rect(80, 0, 100, 20), 0, 0, 0,0,5, 5)
pygame.draw.circle(surface, button_color, (130, 505), 14)
pygame.display.flip()

istAn = False
meinHandy = obj.Handy()
print()
while running:

    # Überprüft, ob App geschlossen wird
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Zeigt Optionen und frägt nach einer Eingabe davon
    
    print("""
[1] Betriebstaste
[2] Bildschirmschoner
[3] Telefonbuch
    """)
    inp = input("Geben Sie Ihre gewünschte Funktion ein:\n>>> ").lower()
    obj.func.clearconsole()
    if inp in ("1", "betriebstaste"):

        # Schaltet Telefon ein bzw. aus
        # zeichnet das display als schwarzes bzw graues rechteck
        
        if istAn:
            maxi = meinHandy.ausschalten()
        else:
            maxi = meinHandy.einschalten()

        display_farbe = maxi[1]
        istAn = maxi[0]

        pygame.draw.rect(surface, display_farbe, pygame.Rect(5, 0, 250, 490),0, 10, 10, 10, 10)
        pygame.draw.rect(surface, phone_color, pygame.Rect(80, 0, 100, 20), 0, 0, 0,0,5, 5)
    elif inp in ("2", "bildschirmschoner") and istAn:
        hbs = obj.Bildschirmschoner()
        # Öffnet den Bildschirmschoner mit ruhigeren Farben und animierten Blasen, die sich nach oben bewegen
        for i in range(100):
            # Rechnung: startpunkt - multiplikator * xAchsec
            # die zufalligen ganzzahlen dienen dazu die blasen realistischer erscheinen zulassen  
            
            surface.fill(phone_color)
            pygame.draw.rect(surface, hbs.aktivieren(),pygame.Rect(5, 0, 250, 490), 0, 10, 10, 10, 10)
            pygame.draw.circle(surface, button_color, (130, 505), 14)
            pygame.draw.circle(surface, hbs.blasen, (random.randint(-5,5)+25, 475 - 5 * i+random.randint(-3,5)), 15)
            pygame.draw.circle(surface, hbs.blasen, (random.randint(-5,5)+76, 469 - 5 * i+random.randint(-3,5)), 21)
            pygame.draw.circle(surface, hbs.blasen, (random.randint(-5,5)+179, 466 - 5 * i+random.randint(-3,5)),24)
            pygame.draw.circle(surface, hbs.blasen, (random.randint(-5,5)+235, 474 - 5 * i+random.randint(-3,5)),16)
            pygame.draw.rect(surface, phone_color, pygame.Rect(80, 0, 100, 20), 0, 0, 0,0,5, 5)
            pygame.display.update()
            pygame.time.delay(150)

    elif inp in ("3", "telefonbuch") and istAn:
        buch = obj.Telefonbuch()
        
        # Sucht bzw. fügt je nach Eingabe Einträge hinzu
        
        print("""
[1] Hinzufügen
[2] Suchen
[3] Anrufen
        """)
        inp = input("Geben Sie Ihre gewünschte Funktion ein:\n>>> ").lower()
        obj.func.clearconsole()
        if inp in ("1", "hinzufügen"):
            name = input("Name der Person:\n>>> ")
            nummer = input("Telefonnummer der Person:\n>>> ")
            buch.eingabe(name, nummer)
        elif inp in ("2", "suchen"):
            print("""
[1] Nach Name suchen
[2] Nach Nummer suchen
            """)
            inp = input("Geben Sie Ihre gewünschte Funktion ein:\n>>> ").lower()
            obj.func.clearconsole()
            if inp in ("1", "nach name suchen"):
                inp = input("Name >>> ")
                lost = buch.suche(name=inp)
            elif inp in ("2", "nach nummer suchen"):
                inp = input("Telefonnummer >>> ")
                lost = buch.suche(nummer=int(inp))
            print(f"""
NAME: {lost[0]}
TELEFONNUMMER: {lost[1]}""")
        elif inp in ("3", "anrufen"):
            inp = input("Wen möchten Sie anrufen? (Name)\n>>> ").lower()
            zuanrufend = buch.suche(name=inp)
            if zuanrufend[0].lower() == "nicht vorhanden":
                print("\nPerson nicht gefunden")
                continue
            print(f"Rufe {zuanrufend[0]} an...")
            input("Auflegen O")
            obj.func.clearconsole()

    # Error Catcher falls Option 1 nicht gewählt

    elif inp == "":
        print("\nBitte geben Sie etwas ein")
    elif int(inp) > 3 or int(inp) < 1 or not inp in ("1","2","3","betriebstaste","bildschirmschoner","telefonbuch"):
        print("\nOption existiert nicht")
    else:
        print("\nTelefon muss erst angeschalten werden!")
    pygame.display.update()
