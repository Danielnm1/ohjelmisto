import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1234',
    autocommit=True
)

cursor = conn.cursor()

icao_code = input("Enter the ICAO code of an airport: ")

cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao_code,))
result = cursor.fetchone()

if result:
    name, municipality = result
    print(f"Airport name: {name}")
    print(f"Location: {municipality}")
else:
    print(f"No airport found with ICAO code '{icao_code}'.")
