import json
from flask import Flask,Response
app = Flask(__name__)
@app.route('/square/<number>')
def square(number):
    try:
       number = float(number)
       square = number**2
       response ={
           'number_float': number,
           'square': square,
           'status' : 200
       }
       return response

    except ValueError:
        response = {
            'message': 'invalid input',
            'status':400
        }
        response_json = json.dumps(response)
        response_http = Response(response=response_json,status=400,mimetype='application/json')
        return response_http
if __name__ =='__main__':
    app.run(use_reloader =True, host='127.0.0.1',port = 5000)