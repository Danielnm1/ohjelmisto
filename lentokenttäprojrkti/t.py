import random


def noppa_peli(pisteet):
    while True:
        syote = input("Haluatko heittää noppia? (y/n): ").lower()

        if syote == "y":
            # Generate independent rolls for player and computer
            pelaaja_noppa1 = random.randint(1, 6)
            pelaaja_noppa2 = random.randint(1, 6)
            tietokone_noppa1 = random.randint(1, 6)
            tietokone_noppa2 = random.randint(1, 6)

            # Display results
            print(f"Tietokone heitti: {tietokone_noppa1} ja {tietokone_noppa2}")
            print(f"Sinun heittosi: {pelaaja_noppa1} ja {pelaaja_noppa2}")

            # Check win condition (e.g., matching both dice)
            if (pelaaja_noppa1, pelaaja_noppa2) == (tietokone_noppa1, tietokone_noppa2):
                palkinto = random.randint(1, 20)
                print(f"Onnittelut! Heitot täsmäsivät, saat {palkinto} rahaa!")
                pisteet += palkinto
            else:
                print("Heitot eivät täsmänneet!.")

            return pisteet
        elif syote == "n":
            print("Et halunnut heittää noppia, peli päättyi.")
            return pisteet
        else:
            print("Väärä syöte, anna 'y' tai 'n'.")


def main():
    Raha = 0
    Raha = noppa_peli(Raha)
    print(f"rahavoitto: {Raha}")


if __name__ == "__main__":
    main()
