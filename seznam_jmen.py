#seznam_jmen.py
#autor-Novakova Klara
from collections import Counter

with open("zaci.txt", "r", encoding="utf-8") as file:
    radky = file.readlines()

upraveny_seznam=[]
krestni_jmena=[]
nejvic_jmen=""
max_jmen=0


for radek in radky:
    jmena = radek.strip().split()  
    if len(jmena) < 2:
        continue
    prijmeni=jmena[-1]
    krestni=jmena[:-1]

    krestni_jmena.extend(krestni)

    if len(krestni)>max_jmen:
        max_jmen=len(krestni)
        nejvic_jmen = " ".join(jmena)

    formatovany_zaznam = f"{' '.join(f'*{jmeno}*' for jmeno in krestni)} -{prijmeni}-"
    upraveny_seznam.append(formatovany_zaznam)

jmena_counter=Counter(krestni_jmena)
nejoblibenejsi_jmeno, pocet_vyskytu = jmena_counter.most_common(1)[0]

for zaznam in upraveny_seznam:
    print(zaznam)

print(f"jméno {nejoblibenejsi_jmeno} se vyskytuje {pocet_vyskytu}")

# Výpis studenta s nejvíce křestními jmény
print(f"Student s nejvíce křestními jmény je {nejvic_jmen}")