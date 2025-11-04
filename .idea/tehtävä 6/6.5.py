def poista_parittomat(luvut):
    karsittu = []
    for luku in luvut:
        if luku % 2 == 0:  # jos luku on parillinen
            karsittu.append(luku)
    return karsittu

# Pääohjelma
luvut = [3, 8, 5, 10, 15, 22, 7]
karsittu_lista = poista_parittomat(luvut)
print(f"Alkuperäinen lista: {luvut}")
print(f"Karsittu lista (vain parilliset): {karsittu_lista}")