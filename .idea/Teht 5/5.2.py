luvut = []

while True:
    luku = input("Anna luku tai paina Enter lopettaaksesi: ")

    if luku == "":
        break

    luku = float(luku)
    luvut.append(luku)

luvut.sort(reverse=True)

viisi_suurinta = luvut[:5]

print("Viisi suurinta lukua:", viisi_suurinta)