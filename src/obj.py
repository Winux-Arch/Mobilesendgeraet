import json
import os
import sys
import time

# Das Handy an sich mit:
# - veränderbarer Farbe als randfarbe:rgb

class Handy(object):
    def __init__(self):
        self.randfarbe = (26,23,24)
        self.anfarbe = (200,200,199)
        self.ausfarbe = (0,0,0)
        self.homefarbe = (200, 200, 199)
      
    
    # Gibt benötigte Werte die beim Einschalten verwendet werden.
    
    def einschalten(self):
        return True, self.anfarbe

    
    # Gibt benötigte Werte die beim Ausschalten verwendet werden.
    
    def ausschalten(self):
        return False, self.ausfarbe

# Gibt benötigte Funktionen und Attribute für den Bildschirmschoner im Handy

class Bildschirmschoner(object):
    def __init__(self):
        
        # Farben des Hintergrundes und der Blasen
    
        self.hintergrund =(0,94,131)
        self.blasen = (0,137,182)
    
    
    # Farbe des Hintergrundes wird zurückgegeben
    
    def aktivieren(self):
        return self.hintergrund


# Telefonbuch, welches im Handy verwendet werden kann

class Telefonbuch(object):
    def __init__(self):
        self.tbpath = "telefonbuch.json"
    

    
    # Funktionierendes Durchsuchen des Telefonbuches

    def suche(self, name=None, nummer=None):
        with open(self.tbpath, "r") as f:
            con = json.load(f)
        for i in con["nummern"]:
            try:
                if i[0].lower() == name.lower():
                    return i
            except:
                if i[1] == nummer:
                    return i
        return "Nicht gefunden", "N/A"

    
    # Eingabe neuer Werte ins Telefonbuch

    def eingabe(self, name, nummer):
        with open(self.tbpath, "r") as f:
            con = json.load(f)
        con["nummern"].append((name, nummer))
        with open(self.tbpath, "w") as f:
            json.dump(con, f, indent=1)

class func:
    # Schreibt Text langsam und jeden Buchstaben einzeln
    def slowprint(text:str, typing_speed:int):
        for l in text:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(500)
        print()

    # Leert die Konsole
    def clearconsole():
        os.system("cls")
