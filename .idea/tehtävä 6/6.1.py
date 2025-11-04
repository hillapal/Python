import random

def heitä_noppaa():
    return random.randint(1, 6)

# Pääohjelma
silmaluku = 0
while silmaluku != 6:
    silmaluku = heitä_noppaa()
    print(f"Nopasta tuli: {silmaluku}")