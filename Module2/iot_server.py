from flask import Flask
from flask_restful import reqparse
import datetime
import pymongo

app = Flask(__name__)

# MongoDB stuff
mongo_clinet = pymongo.MongoClient("mongodb://localhost:27017/")
db_connect = mongo_clinet["iot_server"]  # database name
db_collection = db_connect["sensor_data"]  # collection name


# REST API to get sensor data
@app.route('/update', methods=['GET'])
def update():
    parser = reqparse.RequestParser()

    parser.add_argument('api_key', type=str)
    parser.add_argument('field', type=float)

    sensor_data = parser.parse_args()
    sensor_data['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    db_collection.insert_one(sensor_data)  # store sensor data on MongoDB
    return '200 OK'


# REST API to show sensor data
@app.route('/feeds.json', methods=['GET'])
def feeds():
    parser = reqparse.RequestParser()
    parser.add_argument('api_key', type=str)

    api_key_given = parser.parse_args()
    db_reply = [i for i in db_collection.find(api_key_given)][-1]
    reply = {"Data": db_reply['field'], "Date": db_reply['date']}

    return reply


if __name__ == '__main__':
    app.run(host='192.168.0.107')
