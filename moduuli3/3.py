biologinen_sukupuoli = input("Oletko nainen vai mies? ").lower()
kayttajan_hemoglobiiniarvo = float(input("Anna hemoglobiiniarvo (g/l): "))

if biologinen_sukupuoli == "nainen":
    if 117 <= kayttajan_hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    elif kayttajan_hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
elif biologinen_sukupuoli == "mies":
    if 134 <= kayttajan_hemoglobiiniarvo <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    elif kayttajan_hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
else:
    print("Virheellinen sukupuoli.")

