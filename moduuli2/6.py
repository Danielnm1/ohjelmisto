import random

# Arvotaan kolmenumeroisen lukon koodi (numerot 0–9)
koodi1 = ""
for _ in range(3):
    koodi1 += str(random.randint(0, 9))

# Arvotaan nelinumeroisen lukon koodi (numerot 1–6)
koodi2 = ""
for _ in range(4):
    koodi2 += str(random.randint(1, 6))

# Tulostetaan molemmat koodit
print("Kolmenumeroisen lukon koodi (numerot 0–9):", koodi1)
print("Nelinumeroisen lukon koodi (numerot 1–6):", koodi2)


