class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
    #kiihdytys
    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    # Kulje
    def kulje(self, tunnit):
        # Lisätään kuljettua matkaa = nopeus * aika
        self.kuljettu_matka += self.nopeus * tunnit

auto = Auto("ABC-123", 142)

# Kiihdytetään auton nopeutta
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Auton nopeus kiihdytysten jälkeen: {auto.nopeus} km/h")

# Hätäjarrutus
auto.kiihdytä(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.nopeus} km/h")

# uudelleen liikkeelle
auto.kiihdytä(60)
auto.kulje(1.5)    
print(f"Auton kuljettu matka: {auto.kuljettu_matka} km")