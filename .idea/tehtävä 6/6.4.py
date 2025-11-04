def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

# Pääohjelma
luvut = [3, 7, 2, 9, 5]
tulos = laske_summa(luvut)
print(f"Listan {luvut} lukujen summa on {tulos}.")