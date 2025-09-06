import random
nopan_maara = int(input("How many dice to roll? "))
roll = 0
summa = 0
for n in range(nopan_maara):
    roll = random.randint(1,6)
    summa+= roll
print(f"Sum of the dice: {summa} ")






