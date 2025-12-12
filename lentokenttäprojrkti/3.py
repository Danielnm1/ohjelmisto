import random

airport = "Lontoo"  # lentokenttä
TREASURES = ["€10 seteli", "€20 seteli", "koru", "matkamuisto"]

# AARTEET TAI RYÖSTÖ
def airport_event():
    treasure_chance = 0.15  # 15% mahdollisuus löytää aarre
    robbed_chance = 0.10    # 10% mahdollisuus tulla ryöstetyksi

    roll = random.random()
    if roll < treasure_chance:
        item = random.choice(TREASURES)
        return f"Löysit aarteen: {item}!"
    elif roll < treasure_chance + robbed_chance:
        return "Ryöstö! Menetit jotain arvokasta."
    else:
        return "Ei tapahtumaa aarteen osalta."

# HUOLTO TAI TANKKAUS
def airport_service_event():
    service_chance = 0.4   # 40% huolto
    refuel_chance  = 0.4   # 40% tankkaus

    roll = random.random()
    if roll < service_chance:
        return "Huolto: Lentokoneesi on tarkastettu ja korjattu."
    elif roll < service_chance + refuel_chance:
        return "Tankkaus: Lentokoneesi on tankattu."
    else:
        return "Ei tapahtumaa huollon osalta."

# ---------- PÄÄOHJELMA ----------

print(f"Saavuit lentokentälle: {airport}")

# Suoritetaan molemmat tapahtumat
tapahtuma1 = airport_event()
tapahtuma2 = airport_service_event()

# Tulostetaan molemmat
print(f"Tapahtuma 1: {tapahtuma1}")
print(f"Tapahtuma 2: {tapahtuma2}")
