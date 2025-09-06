laskuri = 0
while laskuri < 5:
    kayttaja_tunnus = input("Anna kayttajatunnuksesi: ")
    salasana = input("Anna salasanasi: ")

    if kayttaja_tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    else:
        print("Virheellinen kayttajatunnus tai salasana.")
        laskuri += 1

if laskuri == 5:
    print("Pääsy evätty")
