#arciboPIC.py
#autor - Klara Novakova
import random

with open("message.txt", "r") as soubor:
    zprava = soubor.read().strip()

sirka = 23
vyska = 73
zvetseni = 10  

# PBM soubor
with open("arecibo10.pbm", "w") as pbm:
    pbm.write(f"P1\n{sirka * zvetseni} {vyska * zvetseni}\n")
    for i in range(vyska):
        radek = zprava[i * sirka: (i + 1) * sirka]
        for _ in range(zvetseni):
            pbm.write(" ".join(("1" if pixel == "1" else "0") * zvetseni for pixel in radek) + "\n")

# PPM soubor
barva_1 = "  0   0 255 "    # Modrá 
barva_2 = "255 255   0 "  # Žlutá
pozadi = "  0   0   0 "       # Černá 

with open("arecibo.ppm", "w") as ppm:
    ppm.write(f"P3\n{sirka * zvetseni} {vyska * zvetseni}\n255\n")
    for i in range(vyska):
        radek = zprava[i * sirka: (i + 1) * sirka]
        n=random.randint(0,1)
        for _ in range(zvetseni):
            ppm.write(" ".join(((barva_1 if n == 0 else barva_2) if pixel=="1" else pozadi) * zvetseni for pixel in radek) + "\n")
