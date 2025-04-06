## ukázka OOP
class Hrdina(object):
    """
      Třída hrdina
    """
    ## KONSTRUKTOR
    def __init__(self, name, strength):
        # uložení attribututů tvořené instance
        self.jmeno = name
        self.zdravi = 100 # 100%
        self.sila = strength

    ## deklarace metod
    def rekni(self, veta):
        print(f"{self.jmeno}: {veta}")

    def pozdrav(self, pozdraveni = "Ahoj"):
        self.rekni(f"{pozdraveni}!")

    def info(self):    
        print(f"{self.jmeno}:")
        print(f"   Z: {self.zdravi}:")
        print(f"   S: {self.sila}:")
    
    def fight(self, other):
        print(f"{self.jmeno} fights {other.jmeno}")
        if self.sila > other.sila:
            print(f"{self.jmeno} WON!")
            other.zdravi -= 10
            if other.zdravi <= 0:
                other.zdraví = 0
                print(f"{other.jmeno} DIED!")
        else:
            print(f"{other.jmeno} WON!")
            self.zdravi -= 20
            if self.zdravi <= 0:
                self.zdraví = 0
                print(f"{self.jmeno} DIED!")


### Hlavní program
# tvoříme instance třídy
rakostnicek = Hrdina("Rákostníček", 70)
ferda = Hrdina("Ferda Mravenec", 90)
# použijeme metody třídy
rakostnicek.info()
ferda.info()
# -------------------
rakostnicek.pozdrav("Čau")
ferda.pozdrav()
rakostnicek.rekni("Ahoj Ferdo, jak se vede?")
ferda.rekni("Je mi dobře, sluníčko svítí, Beruška nezlobí!")
rakostnicek.fight(ferda)
rakostnicek.fight(ferda)
rakostnicek.fight(ferda)
rakostnicek.fight(ferda)
rakostnicek.fight(ferda)
rakostnicek.fight(ferda)
#print(rakostnicek.jmeno, ferda.jmeno)
rakostnicek.info()
ferda.info()