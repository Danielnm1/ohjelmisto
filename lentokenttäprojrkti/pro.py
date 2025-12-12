import mysql.connector
from geopy.distance import geodesic

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1234',
    autocommit=True
)


from geopy.distance import geodesic

def get_airport_coordinates(icao_code):
    cursor = conn.cursor()
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    return result

def run_airport_distance():
    icao1 = input("Enter the first ICAO code: ").strip().upper()
    icao2 = input("Enter the second ICAO code: ").strip().upper()

    coord1 = get_airport_coordinates(icao1)
    coord2 = get_airport_coordinates(icao2)

    if coord1 and coord2:
        distance = geodesic((coord1[0], coord1[1]), (coord2[0], coord2[1])).kilometers
        print(f"Distance between airports is {round(distance, 2)} kilometers.")
    else:
        print("❌ One or both ICAO codes are invalid.")

    conn.close()

run_airport_distance()
