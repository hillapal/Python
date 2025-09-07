pituus = int(input("Anna kuhan pituus senttimetreinä: "))

alamitta = 37

if pituus < alamitta:
    puuttuu = alamitta - pituus

    print(f"Kuha on alamittainen, laske se takaisin järveen! Pituudesta puuttuu {puuttuu} cm.")
else:
    print("Kuha on sallitun mittainen, voit ottaa sen saaliiksi.")