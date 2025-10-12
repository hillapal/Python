import random

#arpakuutioiden lukumäärä
lukumaara = int(input("Kuinka monta arpakuutiota heitetään? "))

summa = 0

# Heitetään arpakuutiot ja lasketaan silmälukujen summa
for i in range(lukumaara):
    heitto = random.randint(1, 6)
    summa += heitto

print("Silmälukujen summa on", summa)

