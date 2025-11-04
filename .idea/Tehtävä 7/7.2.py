class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        # Varmistetaan, ettei nopeus ylitä huippunopeutta
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        # Varmistetaan, ettei nopeus laske alle nollan
        elif self.nopeus < 0:
            self.nopeus = 0

auto = Auto("ABC-123", 142)

# Kiihdytetään auton nopeutta

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Auton nopeus kiihdytysten jälkeen: {auto.nopeus} km/h")

# Hätäjarrutus

auto.kiihdytä(-200)

# Tulostetaan nopeus jarrutuksen jälkeen
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")