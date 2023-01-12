import json
import os

"""
Das Handy an sich mit veränderbarer Farbe als randfarbe:rgb
"""
class Handy(object):
    def __init__(self, randfarbe=(26,23,24)):
        self.randfarbe = randfarbe
        self.anfarbe = (200,200,199)
        self.ausfarbe = (0,0,0)

    def einschalten(self):
        return True, self.anfarbe

    def ausschalten(self):
        return False, self.ausfarbe

    def entsperren(self, passwortInput:str):
        passwort = os.environ["passwort"]
        if passwortInput == passwort:
            return True
        return False


class Bildschirmschoner(object):
    def __init__(self, hintergrund=(0,94,131), blasen=(0,137,182)):
        # Farben des Hintergrundes und der Blasen
        self.hintergrund = hintergrund
        self.blasen = blasen

    def aktivieren(self):
        return self.hintergrund

class Telefonbuch(object):
    def __init__(self):
        self.tbpath = "/Mobi/telefonbuch.json"

    def suche(self, name=None, nummer=None):
        with open(self.tbpath, "r") as f:
            con = json.load(f)
        for i in con["nummern"]:
            if i[0] == name or i[1] == nummer:
                return i
        return None, None

    def eingabe(self, name, nummer):
        with open(self.tbpath, "r") as f:
            con = json.load(f)
        con["nummern"].append((name, nummer))
        with open(self.tbpath, "w") as f:
            json.dump(con, f)