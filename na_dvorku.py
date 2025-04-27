#autor-Klara Novakova

class Zvirata:
    def __init__(self, jmeno, druh, velikost, vek, pocet_nohou,  ):
        self.jmeno = jmeno
        self.druh = druh
        self.velikost = velikost
        self.vek = vek
        self.pocet_nohou = pocet_nohou


    def go_to(self, misto):
        print(f"{self.jmeno} jde k {misto}")
    
    def eat(self,jidlo):
        print(f"{self.jmeno} snědl {jidlo}")
    def make_sound(self,zvuk):
        print(f"{self.jmeno} : {self.zvuk}")

class Savci(Zvirata):
    pass
    
class Psi(Savci):
    pass
    def make_sound(self):
        print(f"{self.jmeno} : haf")

class Kocky(Savci):
    pass
    def make_sound(self):
        print(f"{self.jmeno} : mnau")

class Ptaci(Zvirata):
    pass
    
class Kur(Ptaci):
    pass
    def make_sound(self):
        print(f"{self.jmeno} : kokodak")
class Vrabci(Ptaci):
    pass
    def make_sound(self):
        print(f"{self.jmeno} : pip pip")
class Holubi(Ptaci):
    pass
    def make_sound(self):
        print(f"{self.jmeno} : vrku vrku")


kocka_domaci=Kocky ("Ťapina", "britská kočka", 25, 9, 4)
pes_domaci=Psi ("Bára", "australský ovčák", 50, 13, 4)
kur_domaci=Kur ("Nugetka", "leghornka", 45, 2, 2)
vrabec_domaci=Vrabci ("Lojza", "vrabec", 14, 1.5, 2)
holub_domaci=Holubi("Pepe", "holub", 44, 3, 2)

kocka_domaci.go_to("miska")
kocka_domaci.eat("voda")
pes_domaci.make_sound()
kocka_domaci.make_sound()
kocka_domaci.go_to("skrýš")