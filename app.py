# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app)

@app.route('/order', methods=['GET'])
def order():
    # Retrieve the name from url parameter
    id = request.args.get("id", None)

    response = {}

    if not id:
        response["success"] = False
    else:
        headers = {
            "Content-Type": "application/json",
            "Host": "trackcourier.io",
            "Content-Length": '0'
        }
        
        r = requests.post(
            "https://trackcourier.io/api/v1/get_checkpoints_table/6f3ba1549efaeff8856afd99f9ddbfa1/professional-courier/{id}".format(id=id),
            headers=headers
        )
        response["success"] = True
        response["message"] = r.json()

    return jsonify(response)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h2 style='text-align:center;'>The Freaky Kart APIs Server</h2>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)