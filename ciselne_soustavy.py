# ciselne_soustavy.py 
# autor: Klara Novakova
ZAKLAD = 0
CIFRY  =  "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
cislo = 0


with open("vstup.dat") as f:
    ZAKLAD = int(f.readline())
    cislo = int(f.readline())
print(f"Zadal jsi cislo: {cislo:d} a zaklad: {ZAKLAD}")
puvodnicislo=cislo
vysledek = ""
if cislo < 0:
    cislo = abs(cislo)
    je_negativni = True
else:
    je_negativni = False

while cislo > 0:
    zbytek = cislo % ZAKLAD
    cifra = CIFRY[zbytek]
    vysledek = cifra + vysledek
    cislo = cislo // ZAKLAD

if je_negativni:
    vysledek="-"+ vysledek
####
# tisk výsledku
print(f"{puvodnicislo} v soustavě o základu {ZAKLAD} je {vysledek}")

#END




     