from geopy.distance import geodesic
import mysql.connector
from bens import pelaaja_haku_bensa

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1234',
    autocommit=True
)



#from geopy.distance import geodesic

# Example aircraft data: real-world average burn per 100 km
aircraft_data = {
    "Cessna 172": 35,
    "Boeing 737": 2600,
    "Airbus A320": 2500,
    "Boeing 777": 7200,
    "ATR 72": 800
}

def get_airport_coordinates(icao_code):
    cursor = conn.cursor()
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    return result

def calculate_fuel_consumption(distance_km, fuel_burn_per_100km):
    return (distance_km / 100) * fuel_burn_per_100km

def run_airport_distance_and_fuel():
    icao1 = input("Enter the departure ICAO code: ").strip().upper()
    icao2 = input("Enter the destination ICAO code: ").strip().upper()

    # List available aircraft
    print("\nAvailable aircraft:")
    for i, plane in enumerate(aircraft_data.keys(), start=1):
        print(f"{i}. {plane}")

    # Ask user to choose one
    choice = input("Choose an aircraft by name: ").strip()

    if choice not in aircraft_data:
        print("❌ Invalid aircraft selected.")
        return

    fuel_burn = aircraft_data[choice]

    coord1 = get_airport_coordinates(icao1)
    coord2 = get_airport_coordinates(icao2)

    if coord1 and coord2:
        distance_km = geodesic((coord1[0], coord1[1]), (coord2[0], coord2[1])).kilometers
        fuel_used = calculate_fuel_consumption(distance_km, fuel_burn)

        print(f"\n🛫 Distance between {icao1} and {icao2}: {round(distance_km, 2)} km")
        print(f"✈️ Aircraft: {choice}")
        print(f"⛽ Estimated fuel consumption: {round(fuel_used, 2)} liters")
    else:
        print("❌ One or both ICAO codes are invalid.")

    conn.close()

run_airport_distance_and_fuel()

