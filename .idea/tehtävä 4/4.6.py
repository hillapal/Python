import random

# Kysytään käyttäjältä pisteiden määrä
N = int(input("Anna arvottavien pisteiden määrä: "))

n = 0  # ympyrän sisälle osuvien pisteiden määrä

for _ in range(N):
    # Arvotaan piste neliön sisällä
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Tarkistetaan, onko piste yksikköympyrän sisällä
    if x ** 2 + y ** 2 < 1:
        n += 1

# Lasketaan piin likiarvo
pi_likiarvo = 4 * n / N

print(f"Piin likiarvo arvonnan perusteella: {pi_likiarvo}")