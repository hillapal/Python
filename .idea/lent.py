nimet = ["viivi", "ahmed", "pekka", "olga", " mary"]

names = []

nimi = input("anna eka nimi tai lopeta entterillä: ")

while nimi != "":
    names.append(nimi)
    nimi = input("anna seuraava nimi tai lopeta entterillä")

print(names)