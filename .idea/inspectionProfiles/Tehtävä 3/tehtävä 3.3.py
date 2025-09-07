sukupuoli = input("Anna biologinen sukupuolesi (nainen/mies): ").lower()

arvo = int(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "nainen":

    if arvo < 117:
        print("Hemoglobiiniarvo on alhainen.")

    elif arvo <= 175:
        print("Hemoglobiiniarvo on normaali.")

    else:
        print("Hemoglobiiniarvo on korkea.")

elif sukupuoli == "mies":

    if arvo < 134:
        print("Hemoglobiiniarvo on alhainen.")

    elif arvo <= 195:
        print("Hemoglobiiniarvo on normaali.")

    else:
        print("Hemoglobiiniarvo on korkea.")

else:
    print("Virheellinen sukupuoli.")