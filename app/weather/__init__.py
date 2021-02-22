from flask import Blueprint
from flask_cors import CORS

from app import request_handler, queue
from app.task import get_many_details
weather = Blueprint("weather", __name__)
CORS(weather)

@weather.route('/city/<string:city_name>', methods=['POST'])
def get_by_city(city_name):
    return request_handler.get_weather_city_name(city_name)

@weather.route('/cities', methods=['GET'])
def get_cities():
    job = queue.enqueue(get_many_details)
    return f"{job.id}", 200
