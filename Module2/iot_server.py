from flask import Flask
from flask_restful import reqparse
import datetime
app = Flask(__name__)


@app.route('/update', methods=['GET'])
def update():
    parser = reqparse.RequestParser()

    parser.add_argument('api_key', type=str)
    parser.add_argument('field', type=float)

    sensor_data = parser.parse_args()
    sensor_data['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(sensor_data['field'])

    return '200 OK'


if __name__ == '__main__':
    app.run(host='192.168.0.107')
