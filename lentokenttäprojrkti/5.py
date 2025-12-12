import mysql.connector


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Daniel',
    password='DA10',
    autocommit=True
)

def pelaaja_haku_bensa(bensa_muutos):
    MAX_BENSA = 240000  # Maximum fuel capacity
    muutos = False

    # Get current fuel level from the database
    kursori = yhteys.cursor()
    kursori.execute("SELECT bensa FROM game WHERE id = 1")
    tulos = kursori.fetchone()


    if tulos is not None:
        while muutos == True:
            sql = "UPDATE game SET bensa = %s WHERE id = 1"
            kursori.execute(sql, (uusi_bensa, 1))
            yhteys.commit()
            muutos = True
            print(f"Fuel updated to: {uusi_bensa} liters")
            nykyinen_bensa = tulos[0]
            uusi_bensa = nykyinen_bensa + bensa_muutos

            if uusi_bensa < 0:
                print("minimi bensa määrä on 0")
                uusi_bensa = 0

        # Cap the fuel to MAX_BENSA
            elif uusi_bensa > MAX_BENSA:
                uusi_bensa = MAX_BENSA




    else:
        print("Player not found.")

pelaaja_haku_bensa(40000)