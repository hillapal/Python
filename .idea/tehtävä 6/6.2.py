import random

def heitä_noppaa(tahkot):
    return random.randint(1, tahkot)

# Pääohjelma
tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))

silmaluku = 0
while silmaluku != tahkojen_maara:
    silmaluku = heitä_noppaa(tahkojen_maara)
    print(f"Nopasta tuli: {silmaluku}")

print(f"Sait nopan maksimisilmäluku {tahkojen_maara} – peli päättyi!")