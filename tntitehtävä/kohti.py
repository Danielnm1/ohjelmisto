

print("Tervetuloa linnaan!")
print("Voit lisätä huoneita linnaan. Kun et halua enää lisätä, paina Enter.")
print("Tervetuloa linnaan!")
print("Voit lisätä huoneita linnaan. Kun et halua enää lisätä, paina Enter.")

huoneet = []

while True:
    huone = input("Anna huoneen nimi: ")
    if huone == "":
        break
    huoneet.append(huone)

print("\nVau, onpa se suuri linna!")
print("Siellä on nämä kaikki huoneet:")

for h in huoneet:
    print(h)