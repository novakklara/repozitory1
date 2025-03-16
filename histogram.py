#histogram.py
#autor/ Novakova Klara

import random
import time
from collections import Counter

def cislo():
    while True:
        try:
            N=int(input("zadejte hodnotu od 100 do 1000000: "))
            if N<100 or N<1000000:
                return N
            else:
                print("spatna hodnota")
        except ValueError:
            print("spatna hodnota")
N=cislo()

def nahod_cila(N):
    print("generuji nahodna cisla")
    time.sleep(1)
    num=[random.randint(1,1000) for _ in range (N)]
    return num
nahod_cisla2=nahod_cila(N)

def histogram(num):
    frekvence=Counter(num)
    for number, count in sorted(frekvence.items()):  # Procházíme čísla v pořadí
        print(f"{number:4}: {count:5} {'*' * min(count, 50)}") 
histogram(nahod_cisla2)
