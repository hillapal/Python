import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    # Kiihdytys
    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    # Kulje
    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

autot = []
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = f"ABC-{i}"
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_kaynnissa = True
tunti = 0

while kilpailu_kaynnissa:
    tunti += 1
    for auto in autot:
        # Arvotaan nopeuden muutos
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)  # Auto liikkuu yhden tunnin ajan

        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break

print("\nKILPAILU PÄÄTTYI!")
print(f"Aikaa kului {tunti} tuntia.\n")
print(f"{'Rekisteri':<10}{'Huippu':<10}{'Nopeus':<10}{'Matka (km)':<15}")
print("-" * 45)
for auto in autot:
    print(f"{auto.rekisteritunnus:<10}{auto.huippunopeus:<10}{auto.nopeus:<10}{auto.kuljettu_matka:<15