from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")

db = client['sensor_data_test']
collection = db['sensor_data']

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/update", methods=['POST'])
def update():
    data = request.json

    sensor_data = data.get("sensorData")
    auth_key = data.get("authKey")

    if sensor_data is None and auth_key is None:
        return jsonify({"Error": "Add data and key"}), 400

    data_packet = {
        "Data": sensor_data,
        "Key": auth_key,
        "UpdateDate": datetime.now().strftime("%d-%m-%y"),
        "UpdateTime": datetime.now().strftime("%H-%M-%S")
    }

    collection.insert_one(data_packet)

    return jsonify({"Response": "Data saved!"})



@app.route("/feeds", methods=['GET'])
def feeds():
    data = request.args.get('authKey')

    if data is None:
        return jsonify({"Error": "Add auth key"}), 400

    query_packet = {'Key':data}

    sensor_data_values = collection.find_one(query_packet)

    data_packet ={
        "Data": sensor_data_values['Data']
    }

    return jsonify(data_packet)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)