# jednadvacet.py
# autor - Klara Novakova
############
import random
import time

# třídy
class Karta(object):
    # metody
    def zobraz(self):
        if self._barva != None and self._hodnota != None:
            print(self._barva + self._hodnota)
        else:
            print("Špatně vytisklá karta!!!")

### definice trid
class Karta(object):
    '''
        Objekt "Karta" 
        Atributy: "barva"   ... barva karty
                  "hodnota" ... nominální hodnota karty
    '''
    # Attributy třídy
    SEZNAM_BAREV = ("T","P","K","S") 
    BARVA_MAP = { "T":"♣", "P":"♠", "S":"♥", "K":"♦"}
    SEZNAM_HODNOT = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    SEZNAM_VAH = { "A":11, 
                  "2":2,
                  "3":3,
                  "4":4,
                  "5":5,
                  "6":6,
                  "7":7,
                  "8":8,
                  "9":9,
                  "10":10,
                  "J":10,
                  "Q":10,
                  "K":10
    }
    # konstruktor
    def __init__(self,barva:str, hodnota: str):
        self._barva = None
        self._hodnota = None
        if barva in Karta.SEZNAM_BAREV:
            self._barva = barva
        if hodnota in Karta.SEZNAM_HODNOT:
            self._hodnota = hodnota

    def __str__(self):
        '''
          Řetězcová (textová) reprezentace objektu
        '''
        return str(Karta.BARVA_MAP[self._barva]) + str(self._hodnota)

    def zobraz(self):
        '''
          Zobrazení karty
        '''
        print (str(self) , end = ' ')

    def get_vaha(self):
        '''
          Získání číselné hodnoty (váhy) jedné karty
        '''
        return Karta.SEZNAM_VAH[self._hodnota]

class Hrac(object):
    '''
        Objekt "Hrac" 
        Atributy: "_hand" ... ruka s kartami a "_name" ... jméno hráče
    '''
    def __init__(self, name):
        self._name = name
        self._hand = [] # seznam karet (prazdný)

    def pridej(self,karta):
        '''
         Přidání karty "karta" do ruky hráče
        '''
        self._hand.append(karta)

    def secti(self):
        '''
          Sečení číselných hodnot (vah) všech karet v ruce
        '''
        soucet = 0
        ## tady se provede součet
        for karta in self._hand:
            soucet = soucet + karta.get_vaha()
        return soucet

    def get_name(self):
        return self._name

    def show(self):
        '''
         Zobrazení všech karet v ruce
        '''
        print (f"> {self._name}\n-------------")
        ### tady se provede tisk všech karet v ruce
        for karta in self._hand:
            karta.zobraz()
        print ("\n-------------")


class Balicek(object):
    '''
        Objekt "Balicek" ... reprezentuje balíček karet v karetní hře 
        Atributy: 
    '''
    def __init__(self):
        self._deck = []
        for barva in Karta.SEZNAM_BAREV:
            for hodnota in Karta.SEZNAM_HODNOT:
                karta = Karta(barva, hodnota)
                self._deck.append(karta) ### přidání hodnoty do seznamu (karty do balíčku)

    def zamichat(self):
        '''
          Zamíchání karet v balíčku
        '''
        random.shuffle(self._deck)

    def sejmi(self):
        '''
          Navrátí první kartu z balíčku karet. 
          Po sejmutí již není karta součástí balíčku
        '''
        karta = self._deck.pop() ### doplnit fukčnost
        return karta

class Game(object):
    def __init__(self, jmeno_hrace):
        self._player = Hrac(jmeno_hrace)
        self._computer = Hrac("Počítač")
        self._balicek = Balicek()
        self._balicek.zamichat()
        
    ### metoda
    def run(self):
        print(f" Na začátku dostaneš ty i počítač dvě karty. Jako první hraješ ty a snažíš se dosáhnout co nejvyšího součtu bodových hodnot\n !NESMÍŠ ALE PŘESÁHNOUT 21! \n po tobě hraje počítač pro který platí stejná pravida \n kdo se nejvíc priblíži 21 vyhrává ")
        self._player.pridej(self._balicek.sejmi())
        self._player.pridej(self._balicek.sejmi())
        self._player.show()
        time.sleep(0.5)
        while True:
            odpoved = input("chces dalsi kartu? ano/ne  ")
            if odpoved.lower() =="ano":
                self._player.pridej(self._balicek.sejmi())
                self._player.show()
            else:
                break
        self._computer.pridej(self._balicek.sejmi())
        self._computer.pridej(self._balicek.sejmi())
        self._computer.show()
        time.sleep(0.5)

        while True:
            soucet= self._computer.secti()
            if soucet<15:
                print("počitač si líže další kartu")
                self._computer.pridej(self._balicek.sejmi())
                self._computer.show()
            elif 15<=soucet<=18:
                if random.choice([True,False]):
                    print("počítač si líže další kartu")
                    self._computer.pridej(self._balicek.sejmi())
                    self._computer.show()
                    time.sleep(0.5)

                else:
                    break
            else:
                break
        
        ### VYHODNOCENI
        hrac = self._player.secti()
        pocitac = self._computer.secti()
        
        if hrac > 21 and pocitac<21:
            print ("přetahl jsi 21! PROHRAL JSI ")
        elif pocitac>21 and hrac>21:
            print (" počítač i ty jste přetáhlI! NIKDO NEVYHRÁVÁ")
        elif pocitac>21:
            print ("počítač přetáhl 21! VYHRÁL JSI")
        elif pocitac>hrac:
            print (f"máš {hrac} bodu a počítač ma {pocitac} bodu POČÍTAČ VYHRÁL")
        elif hrac>pocitac:
            print (f"máš {hrac} bodu a počítač ma {pocitac} bodu VYHRÁL JSI")
        else:
            print("remiza")
###### Hlavní program     
hra = Game("skibidak")
hra.run()
###### KONEC