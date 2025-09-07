print("valitse mitä toimintoa haluat käyttää: \n A: yhteenlasku }n B: vähennyslasku \n c: kertolasku \n D: jakolasku")

valinta = input("valintasi (A - D): ")

a = float(input("anna ensimmäinen luku: ("))

b =float(input("anna toinen luku: ("))

if valinta == "A":
    print("yhteenlasku", a + b)
elif valinta == "B":
    print("vähennyslasku:" , a - b)
elif valinta == "c":
    print("kertolasku: ", a * b)
elif valinta == "D":
    print("jakolasku:", a / b)

