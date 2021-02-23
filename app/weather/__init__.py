from flask import Blueprint
from flask_cors import CORS

from app import request_handler, queue
from app.task import get_many_details
from app.models.city import City

weather = Blueprint("weather", __name__)
CORS(weather)

@weather.route('/<string:city_name>', methods=['GET'])
def get_by_city(city_name):
    rsp = request_handler.get_weather_city_name(city_name)
    print(rsp.get_sunrise_24h())
    print(rsp.get_sunset_24h())
    return rsp.get_json()

@weather.route('/', methods=['GET'])
def get_cities():
    job = queue.enqueue(get_many_details)
    return f"{job.id}", 200
