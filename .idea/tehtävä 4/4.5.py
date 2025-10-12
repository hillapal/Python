TUNNUS = "python"
SALASANA = "rules"

yritykset = 0
max_yritykset = 5

while yritykset < max_yritykset:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus g
    and salasana == OIKA_SALASANA:
        print("Tervetuloa")
        break
    else:
        print("Väärä tunnus tai salasana.")
        yritykset += 1

if yritykset == max_yritykset:
    print("Pääsy evätty")