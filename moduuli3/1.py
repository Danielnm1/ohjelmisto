kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä: "))
alamitta = 37.0
if kuhan_pituus < alamitta:
    puuttuva = alamitta - kuhan_pituus
    print(f"Kuha on alamittainen. Laske se takaisin järveen. Pituudesta puuttuu {puuttuva:.2f} cm.")
else:
        print("Kuha on sallittua pyyntikokoa.")


