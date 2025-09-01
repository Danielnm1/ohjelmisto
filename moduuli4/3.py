luvut = []

syote = input("Anna luku (tyhjä lopettaa): ")
while syote != "":
    luku = float(syote)
    luvut.append(luku)
    syote = input("Anna luku (tyhjä lopettaa): ")

if luvut:
    print("Pienin luku:", min(luvut))
    print("Suurin luku:", max(luvut))
else:
    print("Et antanut yhtään lukua.")

print("Ohjelma lopetettu.")


