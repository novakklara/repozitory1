#zvirata.py
#autor-Klara Novakova

class Zvirata:
    def __init__(self, jmeno, druh, velikost, vek, pocet_nohou, ):
        self.jmeno = jmeno
        self.druh = druh
        self.velikost = velikost
        self.vek = vek
        self.pocet_nohou = pocet_nohou

    def go_to(self, misto):
        print(f"{self.jmeno} jde do {misto}")
    
    def eat(self,jidlo):
        print(f"{self.jmeno} snědl {jidlo}")

class Savci(Zvirata):
    pass
class Psi(Savci):
    pass
class Kocky(Savci):
    pass

class Ptaci(Zvirata):
    pass
class Kur(Ptaci):
    pass
class Vrabci(Ptaci):
    pass
class Holubi(Ptaci):
    pass


kocka_domaci=Kocky ("Ťapina", "britská kočka", 25, 9, 4)
pes_domaci=Psi ("Bára", "australský ovčák", 50, 13, 4)
kur_domaci=Kur ("Nugetka", "leghornka", 45, 2, 2)
vrabec_domaci=Vrabci ("Lojza", "vrabec", 14, 1.5, 2)
holub_domaci=Holubi("Pepe", "holub", 44, 3, 2)

kur_domaci.go_to("kurnik")
kocka_domaci.go_to("kurnik")
kocka_domaci.eat(f"{kur_domaci.jmeno}")
pes_domaci.go_to("pelech")
pes_domaci.eat("kosticka")
vrabec_domaci.go_to("hrst")
holub_domaci.go_to("střecha")

