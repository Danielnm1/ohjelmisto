import json
from flask import Flask, Response

app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False
    else:
        is_prime = True
        for n in range(2, number):
            if number % n == 0:
                is_prime = False
                break
        return is_prime

@app.route('/prime_number/<number>')
def prime_number(number):
    try:
        number = int(number)

        result = is_prime(number)

        response = {
            "Number": number,
            "is_prime": result
        }

        return response

    except ValueError:
        response = {
            "Number": number,
            "status": 400,
            "message": "Invalid number"
        }
        json_response = json.dumps(response)
        return Response(response=json_response, status=400, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
