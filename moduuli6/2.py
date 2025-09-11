import random
def roll_dice(nopan_tahkojen_määrä):
    return random.randint(1,nopan_tahkojen_määrä)
nopan_tahkojen_määrä = int(input("Anna nopan_tahkojen_määrä: "))
while True:
    result = roll_dice(nopan_tahkojen_määrä)
    print(result)
    if result==nopan_tahkojen_määrä:
        break