#auto.py
#autor - Novakova Klara

class Auto:
   
    def __init__(self, znacka, barva, prevodovka,):
        self.znacka=znacka
        self.barva=barva
        self.prevodovka=prevodovka
        self.rychlost=30

    def info(self):    
        print(f"{self.znacka}:")
        print(f"  barva auta:         {self.barva}:")
        print(f"  typ převodovky:     {self.prevodovka}:")
        print(f"  aktualní rychlost:  {self.rychlost}:")

    def start(self):
        self.nastartovano = True
        print(f"{self.znacka} nastartovano")
    
    def stop(self):
        self.nastartovano = False
        print(f"{self.znacka} bylo zabrzdeno")
    
    def zrychleni(self,):
        print(f"{self.znacka} zrychluje")
        if self.nastartovano:
            self.rychlost+=5
            print(f"rychlost {self.znacka} je {self.rychlost}")
        else:
            print(f"{self.znacka} není nastartované! Nemůže zrychlit.")



#hlavni program
auto1 = Auto("žigulik", "zelená", "manual" )
auto2 = Auto("cybertruck", "stříbrná", "automat")

auto1.info()
auto2.info()
auto1.start()
auto2.start()
auto1.zrychleni()
auto1.zrychleni()
auto2.stop()
auto2.zrychleni()