import mysql.connector

def get_airports_by_country(country_code):
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='1234',
        autocommit=True
    )
    cursor = conn.cursor()
    query = """
            SELECT type, COUNT(*) as count
            FROM airport
            WHERE iso_country = %s
            GROUP BY type
            ORDER BY type; \
            """
    cursor.execute(query, (country_code,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def run_country_program():
    print("Enter the country code (e.g., FI for Finland):")
    country_code = input().strip().upper()
    airports = get_airports_by_country(country_code)

    print()
    if airports:
        print(f"Airports in {country_code}:")
        for airport_type, count in airports:
            print(f"{count} {airport_type} airports")
    else:
        print(f"No airports found for country code '{country_code}' or database connection failed.")


run_country_program()


