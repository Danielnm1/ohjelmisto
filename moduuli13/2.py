from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def get_airport_by_icao(icao_code):

    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='Daniel',
        password='DA10',
        autocommit=True
    )
    cursor = conn.cursor(dictionary=True)  # Use dictionary=True for easy JSON conversion

    query = """
            SELECT ident AS ICAO, name AS Name, municipality AS Municipality
            FROM airport
            WHERE ident = %s; \
            """
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()  # Only one row expected

    cursor.close()
    conn.close()
    return result


@app.route('/kenttä/<icao>', methods=['GET'])
def airport_route(icao):
    icao = icao.upper()
    airport = get_airport_by_icao(icao)

    if airport:
        return jsonify(airport)
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
