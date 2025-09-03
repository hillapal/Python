from ipaddress import summarize_address_range

kokonaisluku1 = float(input("mikä on kokonaisluku1?"))

kokonaisluku2 = float(input("mikä on kokonaisluku2?"))

kokonaisluku3 = float(input("mikä on kokonaisluku3"))

summa = kokonaisluku1 + kokonaisluku2 + kokonaisluku3
tulo = kokonaisluku1 * kokonaisluku2 * kokonaisluku3
keskiarvo = (kokonaisluku1 + kokonaisluku2 + kokonaisluku3) / 3

print(f" summa on {summa}")
print(f" tulo on {tulo}")
print(f"keskiarvo on {keskiarvo}")
