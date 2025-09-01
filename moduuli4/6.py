import random
pisteita = int(input("Anna pisteiden määrä: "))
sisalla = 0
for _ in range(pisteita):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y < 1:
        sisalla += 1
pii = 4 * sisalla / pisteita
print("Piin likiarvo on:", pii)
