from flask import Blueprint
from flask_cors import CORS

from app import request_handler

weather = Blueprint("weather", __name__)
CORS(weather)

@weather.route('/city/<string:city_name>', methods=['POST'])
def get_by_city(city_name):
    return request_handler.get_weather_city_name(city_name)