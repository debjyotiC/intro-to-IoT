from flask import Flask, request, render_template, jsonify
from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
app = Flask(__name__)

database = client['data-server']
collection = database['sensor-data']


def get_latest_sensor_data(query):
    # Query MongoDB for the latest sensor data matching the query
    # and return it as a dictionary
    return collection.find_one(query, sort=[('date', -1)])


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/update", methods=['POST'])
def update():
    data = request.json
    if data is None:
        return jsonify({"Response": "Provide JSON file"}), 400

    sensor_data = data.get("data")
    sensor_key = data.get("key")
    if sensor_data is None and sensor_key is None:
        return jsonify({"Response": "Invalid sensor data and key"}), 400
    data_packet = {
        "data": sensor_data,
        "key": sensor_key,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    collection.insert_one(data_packet)

    return jsonify({"Response": "Data saved"}), 200


@app.route('/feeds', methods=['GET'])
def feeds():
    key = request.args.get('key')

    # Ensure key is provided
    if key is None:
        return jsonify({"error": "Missing key parameter"}), 400

    # Query MongoDB for the latest sensor data with the given key
    sensor_data = get_latest_sensor_data({"key": key})

    # If no data is found for the given key, return an appropriate response
    if sensor_data is None:
        return jsonify({"error": "No data found for the given key"}), 404

    # Extract required fields and return as JSON
    response_data = {"data": sensor_data["data"], "date": sensor_data["date"]}
    return jsonify(response_data), 200


if __name__ == "__main__":
    app.run()
