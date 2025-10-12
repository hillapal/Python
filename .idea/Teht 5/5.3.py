luku = int(input("Anna kokonaisluku: "))

on_alkuluku = True

if luku < 2:
    on_alkuluku = False
else:
    for i in range(2, luku):
        if luku % i == 0:4
            on_alkuluku = False
            break

if on_alkuluku:
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku.")