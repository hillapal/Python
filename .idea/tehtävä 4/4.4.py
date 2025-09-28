import random

# Tietokone arpoo luvun 1–10 väliltä
oikea_luku = random.randint(1, 10)

print("Arvaa luku väliltä 1..10!")

while True:
    try:
        arvaus = int(input("Anna arvauksesi: "))
    except ValueError:
        print("Anna kokonaisluku.")
        continue

    if arvaus < oikea_luku:
        print("Liian pieni arvaus.")
    elif arvaus > oikea_luku:
        print("Liian suuri arvaus.")
    else:
        print("Oikein!")
        break