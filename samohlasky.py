#samohlasky.py
#autor-Novakova Klara

from collections import Counter

def pocet_samohlasek(text):
    samohlasky=("a","á","e","é","ě","i","í","o","ó","u","ú","ů","y","ý")
    text=text.lower()
    pocet = Counter(char for char in text if char in samohlasky)
    return dict(pocet)

text=input("zadejte vetu: ")

for samohlaska, pocet in pocet_samohlasek(text).items():
    print(f"{samohlaska}: {pocet}")