#parseCSV.py
#autor- Klara Novakova

filename="data.csv"

vysledky={}
pocet_kol=0
pocet_bodu={}
with open(filename, "r",  encoding="UTF=8") as soubor:
    for line in soubor:
        line=line.strip()
        jmeno, cislo=line.split(";")
        cislo = float(cislo)
        pocet_kol+=1
        
        
        if jmeno not in vysledky.keys():
            vysledky[jmeno]=cislo
            pocet_bodu[jmeno]=(1 if cislo>0 else 0)
        else:
            vysledky[jmeno]=vysledky[jmeno]+cislo
            if cislo:
                pocet_bodu[jmeno]+=1
                
    nejlepsi_hrac=max(vysledky, key=vysledky.get)
    nejlepsi_body=vysledky[nejlepsi_hrac]
    
    # vypis slovníku
    print("hráči:              celkový počet bodů:   počet výher:")
    for jmeno,body in vysledky.items():
        print(f"{jmeno:20} {body:10.2f} {pocet_bodu[jmeno]:15}")
    
    nejlepsi_prumer_hrac = max(vysledky, key=lambda hrac: vysledky[hrac] / pocet_bodu[hrac])
    nejlepsi_prumer = vysledky[nejlepsi_prumer_hrac] / pocet_bodu[nejlepsi_prumer_hrac]
    print(f"hrac s nejlepsim průměrným poctem  bodu je {nejlepsi_prumer_hrac} s {nejlepsi_prumer:10.2f} body")
    print(f"nejlepší hráč podle bodů je {nejlepsi_hrac} s {nejlepsi_body:10.2f} body")
    print("Počet hráčů je ", len(vysledky))
    print(f"počet kol je {pocet_kol}") # vytiskne slovník
