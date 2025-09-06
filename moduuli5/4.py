kaupungit = []
for i in range(5):
    kaupunki = input("Syötä kaupungin nimi: ")
    kaupungit.append(kaupunki)
print()
print(f"\nSyöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)