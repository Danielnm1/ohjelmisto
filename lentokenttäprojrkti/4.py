def pelaaja_haku_bensa(bensa_muutos):
    MAX_BENSA = 240000  # Maximum fuel capacity

    # Get current fuel level from the database
    kursori = yhteys.cursor()
    kursori.execute("SELECT bensa FROM game WHERE id = 1")
    tulos = kursori.fetchone()

    if tulos is not None:
        nykyinen_bensa = tulos[0]
        uusi_bensa = nykyinen_bensa + bensa_muutos

        # Cap fuel to max value
        if uusi_bensa > MAX_BENSA:
            uusi_bensa = MAX_BENSA

        # Update fuel value
        sql = "UPDATE game SET bensa = %s WHERE id = 1"
        kursori.execute(sql, (uusi_bensa,))
        yhteys.commit()
        print(f"Fuel updated to: {uusi_bensa} liters")
    else:
        print("Player not found.")
